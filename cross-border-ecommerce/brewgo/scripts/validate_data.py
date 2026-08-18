#!/usr/bin/env python3
"""Dependency-free structural and relationship validation for BrewGo V1 data."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from datetime import date, datetime
from pathlib import Path
from xml.etree import ElementTree as ET

SOURCE_ROOT = Path(__file__).resolve().parents[1]
VALID_AS_OF = date(2026, 8, 8)
REQUIRED = {
    "products.xlsx", "listing_current.md", "search_terms.xlsx", "supplier_quotes.xlsx",
    "reviews.csv", "customer_service.csv", "orders.xlsx", "inventory.xlsx", "cost_parameters.xlsx",
}
HEADERS = {
    "products.xlsx": {"sku", "asin", "product_name", "variation", "color", "material", "dimensions", "weight", "unit", "purchase_cost", "selling_price", "supplier", "status"},
    "search_terms.xlsx": {"date_range", "campaign", "ad_group", "sku", "search_term", "match_type", "impressions", "clicks", "spend", "orders", "sales", "ctr", "cvr", "acos"},
    "supplier_quotes.xlsx": {"supplier", "scope", "unit_price", "currency", "MOQ", "lead_time_days", "payment_terms", "packaging", "inspection", "shipping_terms", "notes"},
    "orders.xlsx": {"order_id", "order_date", "sku", "quantity", "unit_price", "sales_total", "status", "fulfillment", "ship_days", "refund_amount", "customer_region", "note"},
    "inventory.xlsx": {"sku", "current_stock", "inbound", "reserved", "avg_daily_sales", "lead_time_days", "safety_stock", "stock_cover_days", "risk_status", "notes"},
    "cost_parameters.xlsx": {"sku", "selling_price", "purchase_cost", "inbound_freight", "amazon_fee_rate", "fba_fee", "advertising_cost", "return_rate", "exchange_rate", "other_cost", "parameter_status", "note"},
}
CSV_HEADERS = {
    "reviews.csv": {"review_id", "review_date", "sku", "rating", "title", "review_text", "verified_purchase", "helpful_votes", "topic_hint"},
    "customer_service.csv": {"ticket_id", "opened_date", "order_id", "sku", "channel", "customer_message", "category", "risk_level", "agent_note"},
}
ROW_RANGES = {
    "products.xlsx": (15, 25), "search_terms.xlsx": (80, 150), "supplier_quotes.xlsx": (3, 5),
    "orders.xlsx": (100, 200), "reviews.csv": (60, 100), "customer_service.csv": (30, 50),
}

DEMO06_STAGE = "06-competitor-listing-optimization"
DEMO06_COMPETITOR_FILES = tuple(
    f"competitor_{letter}_{kind}.{extension}"
    for letter in "abc"
    for kind, extension in (("listing", "md"), ("reviews", "csv"))
)
DEMO06_REVIEW_HEADERS = {
    "review_id", "review_date", "competitor_id", "rating", "title",
    "review_text", "verified_purchase", "topic_hint", "data_notice",
}


def normalized_sku(value: str) -> str:
    return value.strip().upper()


def col_letters(cell_ref: str) -> str:
    match = re.match(r"[A-Z]+", cell_ref)
    if not match:
        raise ValueError(f"invalid cell reference: {cell_ref}")
    return match.group(0)


def read_xlsx_rows(path: Path) -> list[list[str]]:
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
        if "xl/worksheets/sheet1.xml" not in names:
            raise ValueError("worksheet 1 is missing")
        shared: list[str] = []
        if "xl/sharedStrings.xml" in names:
            shared_root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for item in shared_root.findall(f"{ns}si"):
                shared.append("".join(node.text or "" for node in item.iter(f"{ns}t")))
        sheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
        rows: list[list[str]] = []
        for row in sheet.findall(f".//{ns}sheetData/{ns}row"):
            values: dict[int, str] = {}
            max_col = -1
            for cell in row.findall(f"{ns}c"):
                index = 0
                for letter in col_letters(cell.attrib.get("r", "A1")):
                    index = index * 26 + ord(letter) - 64
                index -= 1
                max_col = max(max_col, index)
                value = cell.findtext(f"{ns}v", default="")
                if cell.attrib.get("t") == "s" and value:
                    value = shared[int(value)]
                elif cell.attrib.get("t") == "inlineStr":
                    value = "".join(node.text or "" for node in cell.findall(f".//{ns}t"))
                values[index] = value
            rows.append([values.get(i, "") for i in range(max_col + 1)])
        return rows


def xlsx_dicts(path: Path) -> list[dict[str, str]]:
    rows = read_xlsx_rows(path)
    if len(rows) < 2:
        raise ValueError("must contain a header and at least one data row")
    headers = rows[0]
    return [dict(zip(headers, row + [""] * (len(headers) - len(row)))) for row in rows[1:]]


def csv_dicts(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def number(value: str) -> float:
    return float(value) if value not in ("", None) else 0.0


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_demo06(project_root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    source_root = project_root / "classroom" / DEMO06_STAGE
    competitor_root = source_root / "input" / "competitors"
    for relative in ("README.md", "task.md"):
        if not (source_root / relative).is_file():
            errors.append(f"classroom/{DEMO06_STAGE}: missing {relative}")
    for filename in DEMO06_COMPETITOR_FILES:
        path = competitor_root / filename
        if not path.is_file():
            errors.append(f"classroom/{DEMO06_STAGE}: missing competitor file {filename}")
            continue
        if filename.endswith("_listing.md"):
            text = path.read_text(encoding="utf-8")
            if "FICTIONAL TEACHING DATA" not in text:
                errors.append(f"{filename}: missing fictional teaching data notice")
            if "seller claims" not in text:
                errors.append(f"{filename}: missing seller-claim evidence notice")
        else:
            try:
                rows = csv_dicts(path)
            except Exception as exc:
                errors.append(f"{filename}: cannot read ({exc})")
                continue
            fields = set(rows[0]) if rows else set()
            absent = DEMO06_REVIEW_HEADERS - fields
            if absent:
                errors.append(f"{filename}: missing fields {', '.join(sorted(absent))}")
            if len(rows) < 4:
                errors.append(f"{filename}: requires at least 4 review rows")
            for row_number, row in enumerate(rows, start=2):
                if row.get("data_notice") != "Fictional teaching data":
                    errors.append(f"{filename} row {row_number}: missing fictional teaching data notice")

    workspace = project_root / "workspaces" / "codex" / DEMO06_STAGE
    if not workspace.exists():
        warnings.append(f"Demo 06 workspace not built: {workspace}")
        return errors, warnings
    manifest_path = workspace / "workspace-manifest.json"
    if not manifest_path.is_file():
        errors.append("Demo 06 workspace: missing workspace-manifest.json")
        return errors, warnings
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Demo 06 workspace: invalid manifest ({exc})")
        return errors, warnings
    if manifest.get("stage") != DEMO06_STAGE:
        errors.append("Demo 06 workspace: manifest stage mismatch")
    generated = manifest.get("generated_files", {})
    required_generated = {
        "AGENTS.md", "project-context.md", "task.md", "outputs/.gitkeep",
        "input/listing_current.md", "input/product_profile_g2.md", "input/products.xlsx",
        "input/reviews.csv",
        *(f"input/competitors/{name}" for name in DEMO06_COMPETITOR_FILES),
    }
    missing_generated = required_generated - set(generated)
    if missing_generated:
        errors.append(f"Demo 06 workspace manifest: missing {', '.join(sorted(missing_generated))}")
    for relative, expected_hash in generated.items():
        path = workspace / relative
        if not path.is_file():
            errors.append(f"Demo 06 workspace: missing generated file {relative}")
        elif file_sha256(path) != expected_hash:
            errors.append(f"Demo 06 workspace: hash mismatch for {relative}")
    for filename in DEMO06_COMPETITOR_FILES:
        source = competitor_root / filename
        copied = workspace / "input" / "competitors" / filename
        if source.is_file() and copied.is_file() and source.read_bytes() != copied.read_bytes():
            errors.append(f"Demo 06 workspace: competitor copy differs for {filename}")
    business_outputs = [path for path in (workspace / "outputs").iterdir() if path.name != ".gitkeep"] if (workspace / "outputs").is_dir() else []
    if business_outputs:
        errors.append("Demo 06 workspace: outputs contains pre-generated business answers")
    return errors, warnings


def parse_date_range(value: str) -> tuple[date, date]:
    text = value.strip().replace("–", "-")
    match = re.match(r"^(\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})$", text)
    if match:
        return tuple(datetime.strptime(part, "%Y-%m-%d").date() for part in match.groups())
    match = re.match(r"^([A-Za-z]{3} \d{2})-([A-Za-z]{3} \d{2}), (\d{4})$", text)
    if match:
        first, second, year = match.groups()
        return datetime.strptime(f"{first} {year}", "%b %d %Y").date(), datetime.strptime(f"{second} {year}", "%b %d %Y").date()
    match = re.match(r"^(\d{4}/\d{2}/\d{2})-(\d{4}/\d{2}/\d{2})$", text)
    if match:
        return tuple(datetime.strptime(part, "%Y/%m/%d").date() for part in match.groups())
    raise ValueError(f"unrecognized date range: {value}")


def validate(project_root: Path, include_work: bool) -> tuple[list[str], list[str]]:
    raw = project_root / "data" / "raw"
    expected = project_root / "data" / "expected"
    errors: list[str] = []
    warnings: list[str] = []
    directories = [raw, expected]
    if include_work:
        directories.append(project_root / "data" / "work")
    for directory in directories:
        present = {path.name for path in directory.iterdir()} if directory.is_dir() else set()
        missing = REQUIRED - present
        if missing:
            errors.append(f"{directory}: missing {', '.join(sorted(missing))}")
    if errors:
        return errors, warnings

    for name in REQUIRED:
        if (raw / name).read_bytes() != (expected / name).read_bytes():
            errors.append(f"data/expected/{name} differs from data/raw/{name}")

    xlsx_rows: dict[str, list[dict[str, str]]] = {}
    for name, needed in HEADERS.items():
        try:
            rows = xlsx_dicts(raw / name)
            xlsx_rows[name] = rows
            absent = needed - set(rows[0])
            if absent:
                errors.append(f"{name}: missing fields {', '.join(sorted(absent))}")
            if name in ROW_RANGES and not ROW_RANGES[name][0] <= len(rows) <= ROW_RANGES[name][1]:
                errors.append(f"{name}: row count {len(rows)} outside {ROW_RANGES[name]}")
        except Exception as exc:
            errors.append(f"{name}: cannot read ({exc})")

    csv_rows: dict[str, list[dict[str, str]]] = {}
    for name, needed in CSV_HEADERS.items():
        try:
            rows = csv_dicts(raw / name)
            csv_rows[name] = rows
            absent = needed - (set(rows[0]) if rows else set())
            if absent:
                errors.append(f"{name}: missing fields {', '.join(sorted(absent))}")
            if not ROW_RANGES[name][0] <= len(rows) <= ROW_RANGES[name][1]:
                errors.append(f"{name}: row count {len(rows)} outside {ROW_RANGES[name]}")
        except Exception as exc:
            errors.append(f"{name}: cannot read ({exc})")

    if errors:
        return errors, warnings

    products = xlsx_rows["products.xlsx"]
    product_skus = {normalized_sku(row["sku"]) for row in products if row["sku"].strip()}
    if len(product_skus) != len([row for row in products if row["sku"].strip()]):
        warnings.append("products.xlsx intentionally contains one normalized duplicate SKU")
    for name in ("search_terms.xlsx", "orders.xlsx", "inventory.xlsx", "cost_parameters.xlsx"):
        for row in xlsx_rows[name]:
            sku = normalized_sku(row["sku"])
            if sku and sku not in product_skus:
                errors.append(f"{name}: unknown SKU {sku}")
    for name in ("reviews.csv", "customer_service.csv"):
        for row in csv_rows[name]:
            sku = normalized_sku(row["sku"])
            if sku and sku not in product_skus:
                errors.append(f"{name}: unknown SKU {sku}")

    for row_number, row in enumerate(xlsx_rows["search_terms.xlsx"], start=2):
        impressions, clicks, orders = number(row["impressions"]), number(row["clicks"]), number(row["orders"])
        spend, sales = number(row["spend"]), number(row["sales"])
        if clicks > impressions or orders > clicks:
            errors.append(f"search_terms.xlsx row {row_number}: impossible funnel counts")
        expected_ctr = clicks / impressions if impressions else 0
        expected_cvr = orders / clicks if clicks else 0
        if abs(number(row["ctr"]) - expected_ctr) > 1e-9 or abs(number(row["cvr"]) - expected_cvr) > 1e-9:
            errors.append(f"search_terms.xlsx row {row_number}: CTR/CVR mismatch")
        if sales == 0 and row["acos"] not in ("", None):
            errors.append(f"search_terms.xlsx row {row_number}: ACoS must be blank when sales is zero")
        if sales and abs(number(row["acos"]) - spend / sales) > 1e-9:
            errors.append(f"search_terms.xlsx row {row_number}: ACoS mismatch")
        _, end = parse_date_range(row["date_range"])
        if end > VALID_AS_OF:
            errors.append(f"search_terms.xlsx row {row_number}: date range ends after {VALID_AS_OF}")

    product_price = {}
    for row in products:
        product_price.setdefault(normalized_sku(row["sku"]), number(row["selling_price"]))
    order_by_id = {}
    for row_number, row in enumerate(xlsx_rows["orders.xlsx"], start=2):
        sku = normalized_sku(row["sku"])
        order_by_id[row["order_id"]] = sku
        if abs(number(row["sales_total"]) - number(row["quantity"]) * number(row["unit_price"])) > 0.005:
            errors.append(f"orders.xlsx row {row_number}: sales_total mismatch")
        if abs(number(row["unit_price"]) - product_price[sku]) > 0.005:
            errors.append(f"orders.xlsx row {row_number}: unit_price differs from product master")

    review_content = [(row["title"].strip().lower(), row["review_text"].strip().lower()) for row in csv_rows["reviews.csv"]]
    if len(set(review_content)) != len(review_content):
        errors.append("reviews.csv: exact duplicate title/review_text content found")
    messages = [row["customer_message"].strip().lower() for row in csv_rows["customer_service.csv"]]
    if len(set(messages)) != len(messages):
        errors.append("customer_service.csv: exact duplicate customer_message found")
    for row in csv_rows["customer_service.csv"]:
        if row["order_id"] not in order_by_id:
            errors.append(f"customer_service.csv: unknown order_id {row['order_id']}")
        elif normalized_sku(row["sku"]) != order_by_id[row["order_id"]]:
            errors.append(f"customer_service.csv: SKU mismatch for {row['ticket_id']} / {row['order_id']}")

    for row_number, row in enumerate(xlsx_rows["inventory.xlsx"], start=2):
        if row["risk_status"] == "Slow moving" and row["notes"].strip().lower() == "normal.":
            errors.append(f"inventory.xlsx row {row_number}: risk status conflicts with notes")
    demo06_errors, demo06_warnings = validate_demo06(project_root)
    errors.extend(demo06_errors)
    warnings.extend(demo06_warnings)
    return errors, warnings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=SOURCE_ROOT, help="BrewGo source or Demo project root")
    parser.add_argument("--include-work", action="store_true", help="also require data/work files")
    args = parser.parse_args()
    errors, warnings = validate(args.project_root.resolve(), args.include_work)
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("VALIDATION PASSED")
    print(f"project_root={args.project_root.resolve()}")
    for warning in warnings:
        print(f"WARNING: {warning}")


if __name__ == "__main__":
    main()
