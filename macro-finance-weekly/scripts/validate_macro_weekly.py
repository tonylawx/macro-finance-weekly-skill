#!/usr/bin/env python3
"""Validation script for Macro & Finance Weekly wrap draft."""

import datetime
import re
import sys
from pathlib import Path

FORBIDDEN_WORDS = [
    "主播", "视频", "节目", "录音", "转录", "字幕", "原文",
    "上述内容", "这期", "本期节目", "文中提到", "作者提到",
    "他说", "她说", "暴富", "无脑做多", "无脑做空", "内幕消息",
    "震撼发布", "彻底颠覆", "史诗级", "吊打",
    "长桥", "富途", "老虎证券", "雪盈证券",
    "上期把", "上期设", "上期写", "上期提到", "上期文章", "上期日历",
    "上期的说法", "应更正为", "应予收回", "应收回", "正如上期",
]

RETAIL_BROKER_KEYWORDS = ["长桥", "富途", "老虎证券", "雪盈证券"]

ASSUMED_CONTEXT_PATTERNS = [
    r"上期(?!度)",
    r"上期把",
    r"上期设",
    r"上期写",
    r"上期提到",
    r"上期文章",
    r"上期日历",
    r"上期的?[说判研预测推]",
    r"应更正为",
    r"应收回",
    r"应予收回",
    r"正如上期",
]

VAGUE_TIME_WORDS = [
    "日前", "前不久", "最近一段时间", "前段时间",
]

REQUIRED_SECTIONS = [
    r"^## 0\s+",
    r"^## 1\s+",
    r"^## 2\s+",
    r"^## 3\s+",
]

SOURCE_KEYWORDS = [
    "报道", "公布", "披露", "通报", "发布", "数据显示", "报告显示",
    "声明", "消息", "统计局", "劳工部", "商务部", "美联储", "财政部",
    "能源信息署", "标普", "彭博", "路透", "华尔街日报", "金融时报",
    "财报", "文件", "官方", "协议", "公告", "知情人士", "调研", "评级",
]

HISTORICAL_COMPARISON_MARKERS = [
    "对比", "相比", "较", "同比", "环比", "历史", "回顾", "早在",
    "参考", "上一轮", "财年", "周期",
]


def extract_target_date(h1_title: str) -> datetime.date | None:
    match = re.search(r"\b(20\d{2})(\d{2})(\d{2})\b", h1_title)
    if not match:
        return None
    year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
    try:
        return datetime.date(year, month, day)
    except ValueError:
        return None


def validate_text(text: str) -> list[str]:
    errors = []
    lines = text.strip().splitlines()

    # 1. Check Title (H1)
    h1_lines = [line for line in lines if line.startswith("# ")]
    target_dt = None
    if not h1_lines:
        errors.append("Missing H1 title (# Title).")
    else:
        title = h1_lines[0].strip()
        target_dt = extract_target_date(title)
        if not target_dt:
            errors.append(f"H1 title must end with valid target date in YYYYMMDD format (got: {title})")

        # Column prefix check
        if not re.search(r"^#\s*【(全球宏观周报|美股周报|财经周报)】", title):
            errors.append(f"H1 title must begin with column brand prefix like 【全球宏观周报】 or 【财经周报】 (got: {title})")

        # No colons check
        if ":" in title or "：" in title:
            errors.append(f"H1 title must not contain colons (got: {title})")

    # 2. Check Required Sections & Subheading Rules
    for pattern in REQUIRED_SECTIONS:
        if not any(re.search(pattern, line) for line in lines):
            errors.append(f"Missing required section header matching: {pattern}")

    for line in lines:
        if line.startswith("## "):
            if ":" in line or "：" in line:
                errors.append(f"Subheading must not contain colons: {line.strip()}")

    # 3. Check Forbidden words
    for word in FORBIDDEN_WORDS:
        count = text.count(word)
        if count > 0:
            errors.append(f"Found forbidden or unprofessional word '{word}' ({count} times).")

    # Check Vague time words
    for word in VAGUE_TIME_WORDS:
        count = text.count(word)
        if count > 0:
            errors.append(f"Found vague temporal phrase '{word}' ({count} times). Specify exact event dates (e.g. '10月23日') instead.")

    # Check Retail broker keywords
    for broker in RETAIL_BROKER_KEYWORDS:
        if broker in text:
            errors.append(
                f"Found retail broker reference '{broker}'. "
                "Use institutional market sources (e.g. 交易所官方数据, 彭博社, 公开市场行情, 标普道琼斯) instead of retail brokerage apps."
            )

    # Check Assumed prior context / meta-self-correction phrases
    for pat in ASSUMED_CONTEXT_PATTERNS:
        matches = re.findall(pat, text)
        if matches:
            errors.append(
                f"Found assumed prior-issue context or self-correction phrase matching pattern '{pat}' ({len(matches)} times). "
                "Weekly articles must be self-contained and standalone. Never assume readers read past issues or expose author correction notes (如 '上期把...设为观察线', '上期写下的...应收回', '上期日历排错更正为')."
            )

    # 4. First-person limit
    first_person_count = text.count("我") + text.count("我们")
    if first_person_count > 12:
        errors.append(f"First-person pronoun count exceeds limit: {first_person_count} > 12.")

    # 5. Check forward-looking trading & risk management terms in section 3
    sec3_match = re.search(r"## 3.*", text, re.DOTALL)
    if sec3_match:
        sec3_content = sec3_match.group(0)
        outlook_keywords = ["支撑", "防守", "阻力", "分水岭", "防线", "仓位", "博弈", "风险", "纪律"]
        if not any(kw in sec3_content for kw in outlook_keywords):
            errors.append("Section 3 must contain forward-looking risk management terms (支撑/防守/阻力/分水岭/防线/仓位/博弈).")
        if re.search(r"(其一|其二|其三|乐观情景|悲观情景|基准情景)", sec3_content):
            errors.append("Section 3 must not use formulaic branch enumeration (其一/其二/其三/乐观情景/悲观情景); write a cohesive, natural narrative.")

    # 6. Length & Richness check
    char_count = len(re.sub(r"\s+", "", text))
    if char_count < 2200:
        errors.append(f"Article is too terse for an industrial-grade macro weekly wrap: {char_count} characters (minimum 2200 required, 3200~5000 recommended).")

    # Section Paragraph Richness check
    sections = re.split(r"(?m)^##\s+", text)
    if len(sections) >= 5:  # preamble + 4 sections
        for idx, sec in enumerate(sections[1:], start=0):
            sec_lines = sec.strip().splitlines()
            sec_title = sec_lines[0] if sec_lines else f"Section {idx}"
            clean_sec = re.sub(r"```chart[\s\S]*?```", "", sec)
            paragraphs = [p.strip() for p in re.split(r"\n\s*\n", clean_sec)[1:] if len(p.strip()) > 50]
            if len(paragraphs) < 2:
                errors.append(f"Section '## {sec_title}' lacks depth: found {len(paragraphs)} substantial paragraphs (minimum 2 paragraphs required for industrial depth).")

    # Quantitative Metrics Density check
    metrics_found = re.findall(r"\d+(?:\.\d+)?%|\$\d+(?:\.\d+)?|\b\d+(?:\.\d+)?(?:点|基点|bps|亿|万|美元|桶)\b", text)
    if len(metrics_found) < 6:
        errors.append(f"Insufficient quantitative market data density: found only {len(metrics_found)} specific metric occurrences (minimum 6 required to substantiate accounting claims).")

    # 7. Check Arabic numerals in headings
    for line in lines:
        if line.startswith("# ") or line.startswith("## "):
            if re.search(r"[一二三四五六七八九十]+点[一二三四五六七八九十]|[一二三四五六七八九十百千]+点|[一二三四五六七八九十百千]+基点|[一二三四五六七八九十]+点[一二三四五六七八九十]+%|[一二三四五六七八九十]+%", line):
                errors.append(f"Heading contains spelled-out Chinese numerals for metrics/points; use Arabic numerals (e.g. 4.2%、5770点、50基点): {line.strip()}")

    # 8. Time Window & Stale Year Detection
    if target_dt:
        target_year = target_dt.year
        sentences = re.split(r"[。\n]", text)
        for past_yr in range(2020, target_year):
            pattern = rf"\b{past_yr}\b"
            for sentence in sentences:
                if re.search(pattern, sentence):
                    has_marker = any(marker in sentence for marker in HISTORICAL_COMPARISON_MARKERS)
                    if not has_marker:
                        errors.append(
                            f"Mentions past year {past_yr} without explicit historical comparison markers "
                            f"(如 '对比{past_yr}年' / '较{past_yr}年同期'). Weekly report must focus on past week events: {sentence.strip()[:60]}"
                        )

    # 9. Source & Date Attribution in Event Sections (## 0, ## 1, ## 2)
    section_splits = re.split(r"(^## \d\s+[^\n]+)", text, flags=re.MULTILINE)
    sections_dict = {}
    for i in range(1, len(section_splits), 2):
        sec_header = section_splits[i].strip()
        sec_body = section_splits[i + 1] if i + 1 < len(section_splits) else ""
        sec_num_match = re.match(r"^## (\d)", sec_header)
        if sec_num_match:
            sections_dict[sec_num_match.group(1)] = sec_body

    date_patterns = [
        r"\d{1,2}\s*月\s*\d{1,2}\s*日",
        r"周[一二三四五六日]",
        r"上周[一二三四五六日]",
        r"\b20\d{2}-\d{2}-\d{2}\b",
    ]

    for sec_num in ("0", "1"):
        if sec_num in sections_dict:
            sec_text = sections_dict[sec_num]
            has_date = any(re.search(pat, sec_text) for pat in date_patterns)
            has_source = any(kw in sec_text for kw in SOURCE_KEYWORDS)
            if not has_date:
                errors.append(f"Section ## {sec_num} lacks specific dates (e.g. '10月23日' / '上周五'). Events must be anchored to specific dates.")
            if not has_source:
                errors.append(f"Section ## {sec_num} lacks data/news source attribution (e.g. '据彭博社报道' / '劳工部公布' / '美联储数据显示').")

    if "2" in sections_dict:
        sec_text = sections_dict["2"]
        has_calendar_dates = any(re.search(pat, sec_text) for pat in (r"周[一二三四五]", r"\d{1,2}\s*月\s*\d{1,2}\s*日"))
        if not has_calendar_dates:
            errors.append("Section ## 2 (Forward Calendar) must state specific upcoming weekdays or dates (e.g. '周二盘后' / '10月28日').")

    return errors


def validate_source_notes(notes_text: str, target_dt: datetime.date | None = None) -> list[str]:
    """Validate source_notes.md for time window bounds and source-date attribution."""
    errors = []
    if not re.search(r"(复盘窗口|Review Window|时间窗口)", notes_text, re.IGNORECASE):
        errors.append("source_notes.md must explicitly declare review window (复盘窗口: YYYY-MM-DD 至 YYYY-MM-DD).")

    has_dates = bool(re.search(r"\b20\d{2}[-/]\d{1,2}[-/]\d{1,2}\b|\d{1,2}\s*月\s*\d{1,2}\s*日", notes_text))
    if not has_dates:
        errors.append("source_notes.md must contain explicit dates for each listed news item/indicator.")

    has_sources = any(kw in notes_text for kw in SOURCE_KEYWORDS)
    if not has_sources:
        errors.append("source_notes.md must document credible news/data sources for the entries.")

    return errors


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_macro_weekly.py <markdown_file> [--source-notes <notes_file>]")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")
    errors = validate_text(content)

    source_notes_path = None
    if "--source-notes" in sys.argv:
        idx = sys.argv.index("--source-notes")
        if idx + 1 < len(sys.argv):
            source_notes_path = Path(sys.argv[idx + 1])
    else:
        sibling_notes = file_path.parent / "source_notes.md"
        if sibling_notes.exists():
            source_notes_path = sibling_notes

    if source_notes_path and source_notes_path.exists():
        notes_content = source_notes_path.read_text(encoding="utf-8")
        target_dt = extract_target_date(content.splitlines()[0] if content else "")
        note_errors = validate_source_notes(notes_content, target_dt)
        errors.extend(note_errors)

    if errors:
        print("Validation FAILED with the following errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("Validation PASSED successfully.")
        sys.exit(0)


if __name__ == "__main__":
    main()
