#!/usr/bin/env python3
"""Draft a daily Data Engineering log from public GitHub activity and the user's study goal."""
import json
import os
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

def infer_topics(items):
    corpus = " ".join((repo + " " + detail) for repo, detail in items).lower()
    topics = [STUDY_FOCUS, CERT_FOCUS]
    rules = [
        (("nyc", "taxi", "mobility"), "NYC Mobility data pipeline"),
        (("oulad",), "OULAD dimensional modeling"),
        (("databricks", "delta", "lakehouse"), "Databricks and Lakehouse engineering"),
        (("great expectations", "data quality", "quality"), "Data quality validation"),
        (("api", "ingestion", "scrap"), "API ingestion"),
        (("ci/cd", "workflow", "actions"), "GitHub Actions and CI/CD"),
        (("doc", "readme"), "Technical documentation"),
        (("sql", "warehouse", "model"), "SQL and data modeling"),
    ]
    for needles, label in rules:
        if any(n in corpus for n in needles):
            topics.append(label)
    return list(dict.fromkeys(topics))

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
    study_line = "- **Ongoing study focus:** Continue Databricks/DataCamp/FTW learning and preparation for the October 17, 2026 Databricks Data Engineer Associate exam."
    if items:
        work = "\n".join(f"- **{repo}:** {detail}" for repo, detail in items) + "\n" + study_line
        learned = "- Connect today's project activity to the certification concepts you are studying; add the exact lesson or takeaway from today's session."
        challenge = "- **Challenge:** Not inferable from a GitHub event; record the actual blocker if one occurred, or write “None recorded.”\n- **Fix:** Add the real fix or write “None recorded.”"
        next_step = "- [ ] Review one Associate exam topic, answer practice questions, and add class or offline work not visible on GitHub."
        reflection = "I am building my Data Engineering skills through Databricks, DataCamp, FTW learning, and hands-on projects while preparing for the October 17 certification."
        assumptions = "- This draft uses public GitHub events only; private repositories and work outside GitHub may be missing."
        topics = infer_topics(items)
    else:
        work = study_line + "\n- **Project activity:** No public GitHub event was returned today; add NYC, class, Databricks, or offline work here if applicable."
        learned = "- Record today's Databricks/DataCamp concept in your own words and connect it to the Associate exam objectives."
        challenge = "- **Challenge:** Not inferable from today's public GitHub events; add a real blocker if one occurred, or write “None today.”\n- **Fix:** Add the actual fix or write “None today.”"
        next_step = "- [ ] Review one Associate exam topic, complete practice questions, and note any class or offline study."
        reflection = "I am steadily preparing for the October 17 Databricks Data Engineer Associate certification while continuing my Data Engineering learning journey."
        assumptions = "- This draft includes the ongoing study focus you confirmed. No public GitHub events were returned; private or offline work may also have happened."
        topics = [STUDY_FOCUS, CERT_FOCUS, "Add today's specific lesson or project topic."]
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
    os.makedirs("daily-logs", exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
        out.write("created=true\n")
    print(f"Created {LOG_PATH} from public GitHub activity and the confirmed study goal.")

if __name__ == "__main__":
    main()
