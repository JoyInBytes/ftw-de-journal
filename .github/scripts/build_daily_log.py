#!/usr/bin/env python3
"""Build a conservative daily learning-log draft from public GitHub events.

Only public GitHub events are available here. This script does not inspect private
repositories, Databricks, classes, or offline study; prompts mark those gaps.
"""
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
    topics = []
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
    return topics or ["GitHub project activity (review the activity list below)"]

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
    # Keep the draft concise and remove duplicate event summaries.
    items = list(dict.fromkeys(items))[:20]
    if items:
        work = "\n".join(f"- **{repo}:** {detail}" for repo, detail in items)
        learned = "- GitHub records the work listed above. Add one takeaway you can now explain or do."
        challenge = "- **Challenge:** Not reliably inferable from a GitHub event. Add it if one occurred; otherwise write “None recorded.”\n- **Fix:** Add the actual fix or write “None recorded.”"
        next_step = "- [ ] Review this activity, add class/Databricks/offline work, and choose one specific next action."
        reflection = "This draft captures public GitHub activity from today. Add what felt difficult and what progress means to you."
        assumptions = "- This draft uses public GitHub events only; private repositories and work outside GitHub may be missing."
        topics = infer_topics(items)
    else:
        work = "- No public GitHub activity for today was found in the recent activity feed."
        learned = "- Add one thing studied or practiced today; GitHub cannot infer class, Databricks, or offline learning."
        challenge = "- **Challenge:** Not recorded in public GitHub activity. Add it if one occurred; otherwise write “None today.”\n- **Fix:** Add the actual fix or write “None today.”"
        next_step = "- [ ] Add today's learning outside GitHub, then choose one small next action."
        reflection = "No public GitHub activity was found for today. Add a short note about any learning that happened elsewhere."
        assumptions = "- No public GitHub events were returned for this date; private or offline work may still have happened."
        topics = ["No public GitHub activity found; add class, Databricks, or offline topics if applicable."]
    date_title = TODAY.strftime("%B %-d, %Y")
    content = render(open(TEMPLATE_PATH, encoding="utf-8").read(), {
        "DATE": date_title,
        "TOPICS": "\n".join(f"- {t}" for t in topics),
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
    print(f"Created {LOG_PATH} from today's public GitHub activity.")

if __name__ == "__main__":
    main()
