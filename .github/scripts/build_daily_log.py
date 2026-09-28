#!/usr/bin/env python3
"""Draft a daily Data Engineering log from public GitHub activity and the user's study goal."""
import json
import os
import re
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

OWNER = "JoyInBytes"
TZ = ZoneInfo("Asia/Manila")
TODAY = datetime.now(TZ).date()
TEMPLATE_PATH = "templates/daily-log.md"
LOG_PATH = f"daily-logs/{TODAY.isoformat()}.md"
API_URL = f"https://api.github.com/users/{OWNER}/events?per_page=100"
CERT_FOCUS = "Databricks Data Engineer Associate certification preparation (October 17, 2026)"
STUDY_FOCUS = "Databricks and DataCamp Data Engineering learning"

def fetch_events():
    req = urllib.request.Request(
        API_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ftw-de-daily-log",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

def event_summary(event):
    kind = event.get("type", "")
    payload = event.get("payload", {})
    repo = event.get("repo", {}).get("name", "")
    when = datetime.fromisoformat(event["created_at"].replace("Z", "+00:00")).astimezone(TZ).date()
    if when != TODAY:
        return None
    if kind == "PushEvent":
        messages = [c.get("message", "").splitlines()[0] for c in payload.get("commits", [])]
        details = "; ".join(m for m in messages if m) or "pushed code"
        return repo, f"Pushed changes: {details}"
    if kind == "PullRequestEvent":
        pr = payload.get("pull_request", {})
        return repo, f"{payload.get('action', 'updated')} pull request: {pr.get('title', 'title unavailable')}"
    if kind == "IssuesEvent":
        issue = payload.get("issue", {})
        return repo, f"{payload.get('action', 'updated')} issue: {issue.get('title', 'title unavailable')}"
    if kind == "IssueCommentEvent":
        issue = payload.get("issue", {})
        return repo, f"commented on issue: {issue.get('title', 'title unavailable')}"
    if kind == "PullRequestReviewEvent":
        pr = payload.get("pull_request", {})
        return repo, f"reviewed pull request: {pr.get('title', 'title unavailable')}"
    if kind == "CreateEvent":
        return repo, f"created {payload.get('ref_type', 'repository item')}: {payload.get('ref') or repo}"
    if kind == "ReleaseEvent":
        release = payload.get("release", {})
        return repo, f"published release: {release.get('name') or release.get('tag_name', 'release')}"
    return None

def remove_emojis(text):
    """Keep generated logs free of emoji, including copied activity titles."""
    return re.sub(
        r"[\U0001F000-\U0001FAFF\u2600-\u27BF\u2300-\u23FF\u2B00-\u2BFF"
        r"\u200D\u20E3\uFE0E\uFE0F\U000E0020-\U000E007F\u00A9\u00AE\u203C\u2049\u2122\u2139\u3030\u303D\u3297\u3299]",
        "",
        text,
    )


def render(template, replacements):
    for key, value in replacements.items():
        template = template.replace("{{" + key + "}}", value)
    return template

def main():
    if os.path.exists(LOG_PATH):
        print(f"Log already exists at {LOG_PATH}; leaving it unchanged.")
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
            out.write("created=false\n")
        return
    events = fetch_events()
    items = []
    for event in events:
        if event.get("actor", {}).get("login", "").lower() != OWNER.lower():
            continue
        item = event_summary(event)
        if item:
            items.append(item)
    items = list(dict.fromkeys(items))[:20]
    study_line = "- **Study goal:** Prepare for the Databricks Data Engineer Associate exam on October 17, 2026, while learning through Databricks, DataCamp, and FTW. This goal does not confirm a lesson was completed today."
    if items:
        work = "\n".join(f"- **{repo}:** {detail}" for repo, detail in items) + "\n\n" + study_line
        topics = ["GitHub project activity", "Ongoing Databricks exam preparation"]
    else:
        work = "No public GitHub activity was found for this date. Class activities, private work, and offline study may be missing.\n\n" + study_line
        topics = ["Ongoing Data Engineering study goal", "Databricks exam preparation"]
    learned = "A specific lesson has not been recorded yet. Add what you learned and a simple example."
    challenge = "**Problem:** Not recorded yet.\n\n**Solution:** Not recorded yet. Add the steps you actually tried and whether they worked."
    next_step = "- [ ] Add the exact lesson or project task completed.\n- [ ] Review one exam topic and answer practice questions.\n- [ ] Record any problem and the steps used to fix it."
    reflection = "Not recorded yet. Write what became clearer or what you still need to practice."
    assumptions = "- This is an automatic draft based on public GitHub activity and the ongoing study goal.\n- GitHub activity does not show every task or prove what was learned.\n- Explain technical terms in plain language, keep useful details, and do not use emojis."
    date_title = TODAY.strftime("%B %-d, %Y")
    content = render(open(TEMPLATE_PATH, encoding="utf-8").read(), {
        "DATE": date_title,
        "TOPICS": "\n".join(f"- {topic}" for topic in topics),
        "WORKED_ON": work,
        "LEARNED": learned,
        "CHALLENGE_FIX": challenge,
        "ASSUMPTIONS": assumptions,
        "NEXT_STEP": next_step,
        "REFLECTION": reflection,
    })
    content = remove_emojis(content)
    os.makedirs("daily-logs", exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
        out.write("created=true\n")
    print(f"Created {LOG_PATH} from public GitHub activity and the confirmed study goal.")

if __name__ == "__main__":
    main()
