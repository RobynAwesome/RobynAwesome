#!/usr/bin/env python3
"""Generate the public GitHub profile estate telemetry SVG.

Semantic state labels are governed in governance/profile-telemetry.json.
GitHub activity metadata is observational and may never rewrite those labels.
The output is intentionally stable unless observable repository facts change.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "governance" / "profile-telemetry.json"


def github_repo(repo: str) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "RobynAwesome-profile-telemetry",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.load(response)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError):
        return {}


def push_label(pushed_at: str | None) -> tuple[str, dt.datetime | None]:
    if not pushed_at:
        return "activity unavailable", None
    try:
        pushed = dt.datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    except ValueError:
        return "activity unavailable", None
    return f"last push {pushed:%Y-%m-%d}", pushed


def render(config: dict) -> str:
    systems = []
    latest_push: dt.datetime | None = None

    for item in config["systems"]:
        meta = github_repo(item["repo"])
        activity, pushed = push_label(meta.get("pushed_at"))
        if pushed and (latest_push is None or pushed > latest_push):
            latest_push = pushed
        systems.append({
            **item,
            "activity": activity,
            "stars": meta.get("stargazers_count"),
        })

    rows = []
    y = 154
    for index, item in enumerate(systems):
        accent = ["#52E2B3", "#A98BFF", "#FFCE32", "#58D6FF", "#FF7E70", "#FF87C8"][index % 6]
        stars = "" if item["stars"] is None else f" · ★ {item['stars']}"
        rows.append(f'''<g class="row r{index + 1}">
  <circle cx="74" cy="{y - 6}" r="7" fill="{accent}" class="pulse"/>
  <text x="98" y="{y}" class="name">{html.escape(item['label'])}</text>
  <text x="390" y="{y}" class="state" fill="{accent}">{html.escape(item['state'])}</text>
  <text x="650" y="{y}" class="meta">{html.escape(item['signal'])}</text>
  <text x="1120" y="{y}" text-anchor="end" class="activity">{html.escape(item['activity'] + stars)}</text>
</g>''')
        y += 58

    latest = "LATEST OBSERVED REPO PUSH unavailable"
    if latest_push:
        latest = f"LATEST OBSERVED REPO PUSH {latest_push:%Y-%m-%d}"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="560" viewBox="0 0 1200 560" role="img" aria-labelledby="title desc">
<title id="title">RobynAwesome estate telemetry</title>
<desc id="desc">Governed semantic system states with observational GitHub repository activity.</desc>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#050807"/><stop offset=".6" stop-color="#0D1713"/><stop offset="1" stop-color="#14101E"/></linearGradient>
  <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#77DDBB" stroke-opacity=".035"/></pattern>
  <style>
    .name{{font:700 18px Inter,system-ui,sans-serif;fill:#F3F6F4}}.state{{font:700 13px ui-monospace,SFMono-Regular,Menlo,monospace}}.meta{{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;fill:#AAB8B2}}.activity{{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;fill:#83968E}}.small{{font:11px ui-monospace,SFMono-Regular,Menlo,monospace;fill:#83968E}}.head{{font:800 29px Inter,system-ui,sans-serif;fill:#F5F7F6}}.row{{opacity:.82;animation:row 6s ease-in-out infinite}}.r2{{animation-delay:.6s}}.r3{{animation-delay:1.2s}}.r4{{animation-delay:1.8s}}.r5{{animation-delay:2.4s}}.r6{{animation-delay:3s}}.pulse{{animation:pulse 2.6s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}@keyframes row{{50%{{opacity:1}}}}@keyframes pulse{{50%{{transform:scale(1.35);opacity:.45}}}}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
  </style>
</defs>
<rect width="1200" height="560" rx="28" fill="url(#bg)"/><rect width="1200" height="560" rx="28" fill="url(#grid)"/>
<text x="62" y="62" class="head">KOPANO ESTATE // PUBLIC TELEMETRY</text>
<text x="62" y="90" class="small">Semantic states are governed. Repository activity is observational. No activity metric may silently rewrite system truth.</text>
<line x1="62" y1="112" x2="1138" y2="112" stroke="#77DDBB" stroke-opacity=".22"/>
{''.join(rows)}
<line x1="62" y1="510" x2="1138" y2="510" stroke="#77DDBB" stroke-opacity=".16"/>
<text x="62" y="536" class="small">{latest} · WORKING → CONNECTED → CURRENT → VISIBLE → EVIDENCED → BACKABLE</text>
</svg>'''


def main() -> None:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    output = ROOT / config["generated_asset"]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(config), encoding="utf-8")
    print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
