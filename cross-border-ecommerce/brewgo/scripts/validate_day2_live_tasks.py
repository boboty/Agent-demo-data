#!/usr/bin/env python3
"""Validate BrewGo Day2 Live Tasks classroom assets and generated workspaces."""
from __future__ import annotations

import json
import statistics
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
CLASSROOM = ROOT / "classroom" / "day2-live-tasks"
WORKSPACES = ROOT / "workspaces" / "codex" / "day2-live-tasks"
INSTRUCTOR = ROOT / "instructor"
TASKS = (
    "01-amazon-competitor-discovery",
    "02-instagram-lead-discovery",
    "03-data-analysis-dashboard",
)
errors: list[str] = []
passes: list[str] = []


class AuditHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: Counter[str] = Counter()
        self.attrs: list[tuple[str, dict[str, str]]] = []
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        self.tags[tag] += 1
        self.attrs.append((tag, values))

    def handle_data(self, data: str) -> None:
        self.text.append(data)


def check(condition: bool, message: str) -> None:
    if condition:
        passes.append(message)
    else:
        errors.append(message)


def parse_html(path: Path) -> AuditHTMLParser:
    parser = AuditHTMLParser()
    try:
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
    except Exception as exc:  # noqa: BLE001 - validation should aggregate failures
        errors.append(f"HTML parse failed: {path}: {exc}")
    return parser


def external_dependencies(parser: AuditHTMLParser) -> list[str]:
    external: list[str] = []
    for tag, attrs in parser.attrs:
        if tag not in {"script", "link", "img", "iframe"}:
            continue
        value = attrs.get("src") or attrs.get("href") or ""
        if urlparse(value).scheme in {"http", "https"}:
            external.append(value)
    return external


def validate_local_links(path: Path, parser: AuditHTMLParser) -> None:
    for tag, attrs in parser.attrs:
        if tag != "a":
            continue
        href = attrs.get("href", "")
        parsed = urlparse(href)
        if not href or href.startswith("#") or parsed.scheme in {"http", "https", "mailto"}:
            continue
        target = (path.parent / parsed.path).resolve()
        check(target.is_file(), f"local link resolves: {path.name} -> {href}")


def validate_source_and_workspaces() -> None:
    check(CLASSROOM.is_dir(), "classroom/day2-live-tasks exists")
    check(WORKSPACES.is_dir(), "generated Day2 workspace root exists")
    check(tuple(sorted(path.name for path in WORKSPACES.iterdir() if path.is_dir())) == TASKS, "three generated workspaces match whitelist")
    rules = (CLASSROOM / "WORKSPACE_RULES.md").read_text(encoding="utf-8")
    check("不得覆盖" in rules and "只写入 `outputs/`" in rules, "common rules protect original inputs and constrain outputs")
    check("Live 数据与 Offline 教学数据必须明确区分" in rules, "common rules separate Live and Offline modes")

    for task in TASKS:
        source = CLASSROOM / task
        workspace = WORKSPACES / task
        for name in ("README.md", "RAW_REQUEST.md", "AGENTS.md", "input", "outputs", "workspace-manifest.json"):
            check((workspace / name).exists(), f"{task} workspace has {name}")
        check(not (workspace / "INSTRUCTOR_GUIDE.md").exists(), f"{task} excludes instructor guide")
        check(not list(workspace.rglob("SKILL.md")) and not list(workspace.rglob(".agents")), f"{task} has no preinstalled final Skill")
        output_entries = [path.name for path in (workspace / "outputs").iterdir() if path.name != ".gitkeep"]
        check(not output_entries, f"{task} workspace outputs initially empty")
        source_output_entries = [path.name for path in (source / "outputs").iterdir() if path.name != ".gitkeep"]
        check(not source_output_entries, f"{task} source outputs initially empty")
        manifest = json.loads((workspace / "workspace-manifest.json").read_text(encoding="utf-8"))
        check(manifest.get("outputs_initially_empty") is True and manifest.get("instructor_assets_excluded") is True, f"{task} manifest records isolation contract")
        for source_input in sorted((source / "input").rglob("*")):
            if source_input.is_file():
                relative = source_input.relative_to(source / "input")
                target = workspace / "input" / relative
                check(target.is_file() and target.read_bytes() == source_input.read_bytes(), f"{task} input copied without mutation: {relative}")


def validate_offline_snapshots() -> None:
    amazon_root = WORKSPACES / TASKS[0] / "input" / "offline"
    amazon_html = sorted(amazon_root.rglob("*.html"))
    check(len(amazon_html) == 13, "Amazon Offline contains one search page and 12 detail pages")
    amazon_search = parse_html(amazon_root / "amazon-search-results.html")
    validate_local_links(amazon_root / "amazon-search-results.html", amazon_search)
    amazon_text = " ".join(amazon_search.text)
    search_cards = sum(1 for tag, attrs in amazon_search.attrs if tag == "article" and "card" in attrs.get("class", "").split())
    check(search_cards == 15, "Amazon teaching search page has 15 candidate cards")
    check("FICTIONAL / TEACHING SNAPSHOT" in amazon_text, "Amazon search page visibly labels teaching snapshot")
    for path in amazon_html:
        parser = parse_html(path)
        validate_local_links(path, parser)
        check("FICTIONAL / TEACHING SNAPSHOT" in " ".join(parser.text), f"Amazon snapshot labeled: {path.name}")
        check(not external_dependencies(parser), f"Amazon snapshot has no external runtime dependency: {path.name}")

    instagram_root = WORKSPACES / TASKS[1] / "input" / "offline"
    instagram_html = sorted(instagram_root.rglob("*.html"))
    check(len(instagram_html) == 19, "Instagram Offline contains one search page and 18 Profile pages")
    instagram_search = parse_html(instagram_root / "search-results.html")
    validate_local_links(instagram_root / "search-results.html", instagram_search)
    instagram_text = " ".join(instagram_search.text)
    profile_cards = sum(1 for tag, attrs in instagram_search.attrs if tag == "article" and "card" in attrs.get("class", "").split())
    check(profile_cards == 18, "Instagram teaching search page has 18 candidate cards")
    check("FICTIONAL / TEACHING SNAPSHOT" in instagram_text, "Instagram search page visibly labels teaching snapshot")
    for path in instagram_html:
        parser = parse_html(path)
        validate_local_links(path, parser)
        check("FICTIONAL / TEACHING SNAPSHOT" in " ".join(parser.text), f"Instagram snapshot labeled: {path.name}")
        check(not external_dependencies(parser), f"Instagram snapshot has no external runtime dependency: {path.name}")

    instagram_readme = (WORKSPACES / TASKS[1] / "README.md").read_text(encoding="utf-8")
    check(all(phrase in instagram_readme for phrase in ("不自动关注", "不自动私信", "不做批量营销", "不访问私人内容")), "Instagram task explicitly forbids follow, DM, bulk marketing, and private access")


def read_data_rows() -> list[dict[str, object]]:
    workbook = WORKSPACES / TASKS[2] / "input" / "business-performance.xlsx"
    wb = load_workbook(workbook, read_only=True, data_only=True)
    check(wb.sheetnames == ["README", "business_performance"], "data workbook has README and business_performance sheets")
    check("FICTIONAL / TEACHING DATASET" in str(wb["README"]["A1"].value), "data workbook visibly labels teaching dataset")
    ws = wb["business_performance"]
    values = ws.iter_rows(values_only=True)
    headers = next(values)
    rows = [dict(zip(headers, row)) for row in values]
    check(len(rows) == 421 and len(headers) == 15, "data workbook has 421 rows and 15 fields")
    return rows


def validate_dataset() -> None:
    rows = read_data_rows()
    keys = [tuple(row.values()) for row in rows]
    duplicates = sum(count - 1 for count in Counter(keys).values() if count > 1)
    check(duplicates == 1, "dataset contains exactly one exact duplicate")
    check(sum(row["sessions"] is None for row in rows) == 4, "dataset contains four missing sessions values")
    check(sum(row["inventory"] is None for row in rows) == 3, "dataset contains three missing inventory values")
    revenue = [float(row["revenue"]) for row in rows]
    check(max(revenue) > statistics.median(revenue) * 5, "dataset contains a detectable high revenue outlier")

    unique: list[dict[str, object]] = []
    seen: set[tuple[object, ...]] = set()
    for row in rows:
        key = tuple(row.values())
        if key not in seen:
            unique.append(row)
            seen.add(key)
    ads = defaultdict(lambda: {"spend": 0.0, "orders": 0})
    cream = defaultdict(float)
    regions = defaultdict(lambda: {"returns": 0, "units": 0})
    for row in unique:
        month = row["date"].strftime("%Y-%m")
        if row["channel"] == "Amazon Ads":
            ads[month]["spend"] += float(row["ad_spend"])
            ads[month]["orders"] += int(row["orders"])
        if row["sku"] == "BG-G2-CRM":
            cream[month] += float(row["revenue"])
        regions[row["region"]]["returns"] += int(row["returns"])
        regions[row["region"]]["units"] += int(row["units"])
    check(ads["2026-03"]["spend"] > ads["2026-02"]["spend"] and ads["2026-03"]["orders"] <= ads["2026-02"]["orders"], "Amazon Ads spend rises from February to March without order growth")
    check(cream["2026-03"] < cream["2026-01"] * 0.6, "BG-G2-CRM shows a material sales decline by March")
    return_rates = {region: values["returns"] / values["units"] for region, values in regions.items()}
    check(max(return_rates, key=return_rates.get) == "South" and return_rates["South"] > 0.1, "South has the highest and materially elevated return rate")


def validate_instructor_assets() -> None:
    runbook = INSTRUCTOR / "day2-live-tasks-runbook.md"
    acceptance = INSTRUCTOR / "day2-live-tasks-acceptance.md"
    skill = INSTRUCTOR / "amazon-skill-reference.md"
    control = INSTRUCTOR / "day2-live-tasks-control.html"
    dashboard = INSTRUCTOR / "day2-data-dashboard-reference.html"
    for path in (runbook, acceptance, skill, control, dashboard):
        check(path.is_file(), f"instructor asset exists: {path.name}")
    runbook_text = runbook.read_text(encoding="utf-8")
    check(runbook_text.count("【原始需求】") == 3 and runbook_text.count("【一句收口】") == 3, "runbook uses required compact sections for all three tasks")
    check(all(title in runbook_text for title in ("【如何进入 Skill Lab】", "【第二关键词怎么选】", "【Skill 验收重点】")), "Amazon runbook contains Skill Lab sections")
    skill_text = skill.read_text(encoding="utf-8")
    required_skill_sections = ("## Trigger", "## Inputs", "## Scope", "## Discovery workflow", "## Sponsored handling", "## Deduplication", "## Field extraction", "## Evidence rules", "## Missing-data rules", "## Output contract", "## Human review", "## Self-check")
    check(all(section in skill_text for section in required_skill_sections), "Amazon instructor Skill Plan B covers complete method contract")
    forbidden_results = ("TCH-A001", "$59.99", "portable coffee grinder")
    check(not any(value in skill_text for value in forbidden_results), "Amazon Skill reference does not hardcode first-run result or keyword")

    control_parser = parse_html(control)
    validate_local_links(control, control_parser)
    control_text = " ".join(control_parser.text)
    tab_buttons = sum(1 for tag, attrs in control_parser.attrs if tag == "button" and "tab" in attrs.get("class", "").split())
    check(tab_buttons == 3, "control page has three independent task tabs")
    check(all(label in control_text for label in ("原始需求", "澄清", "第一次执行", "Skill", "新关键词复跑", "验收")), "control page shows complete Amazon learning flow")
    check(not external_dependencies(control_parser), "control page has no external runtime dependency")

    dashboard_parser = parse_html(dashboard)
    dashboard_text = " ".join(dashboard_parser.text)
    chart_articles = sum(1 for tag, attrs in dashboard_parser.attrs if tag == "article" and "card" in attrs.get("class", "").split()) - 1
    check(chart_articles >= 4, "reference Dashboard contains at least four business charts")
    check("关键数字追溯" in dashboard_text and "同步变化不能证明因果" in dashboard_text, "reference Dashboard includes traceability and causality boundary")
    check(not external_dependencies(dashboard_parser), "reference Dashboard is single-file with no online runtime dependency")


def main() -> None:
    validate_source_and_workspaces()
    validate_offline_snapshots()
    validate_dataset()
    validate_instructor_assets()
    print(f"PASS {len(passes)} checks")
    for message in passes:
        print(f"  PASS {message}")
    if errors:
        print(f"FAIL {len(errors)} checks")
        for message in errors:
            print(f"  FAIL {message}")
        raise SystemExit(1)
    print("ALL DAY2 LIVE TASK CHECKS PASSED")


if __name__ == "__main__":
    main()
