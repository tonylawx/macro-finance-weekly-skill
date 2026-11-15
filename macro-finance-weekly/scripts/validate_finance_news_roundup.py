#!/usr/bin/env python3
"""Validate the factual news-roundup format of the weekly 财经周报.

This is a deterministic editorial gate, not independent verification that a
claim is true or that a WeChat post meets every platform requirement.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TITLE_RE = re.compile(r"^#\s+【财经周报】.+\s(20\d{6})\s*$", re.M)
SECTION_RE = re.compile(r"^##\s+\d+\s+(.+)$", re.M)
ITEM_RE = re.compile(r"^###\s+(\d{2})\s+(.+)$", re.M)
BANNED_ANALYSIS_SCAFFOLD = (
    "看涨情景", "看跌情景", "做多信号", "做空信号",
    "入场点位", "止损点位", "标普技术位", "QQQ阻力",
)
PROMO_MARKERS = (
    "长按识别二维码", "关注后查看", "阅读原文查看完整版",
    "扫码进群", "私信领取", "点击阅读原文",
)


def validate_roundup(text: str, *, source_notes: str = "") -> list[str]:
    errors: list[str] = []
    match = TITLE_RE.search(text)
    if not match:
        errors.append("H1 must start with 【财经周报】 and end in YYYYMMDD.")
    elif ":" in text.splitlines()[0] or "：" in text.splitlines()[0]:
        errors.append("H1 title must not contain colons.")

    sections = list(SECTION_RE.finditer(text))
    if len(sections) < 3:
        errors.append("News digest needs thematic groups (at least 3 ## sections).")

    items = list(ITEM_RE.finditer(text))
    if not 8 <= len(items) <= 14:
        errors.append(f"News digest needs 8–14 independently sourced items; got {len(items)}.")

    numbers = [int(m.group(1)) for m in items]
    if numbers and numbers != list(range(1, len(items) + 1)):
        errors.append("News item numbers must be consecutive starting at 01.")

    for i, match in enumerate(items):
        start = match.end()
        next_item = items[i + 1].start() if i + 1 < len(items) else len(text)
        next_section = min((s.start() for s in sections if s.start() > start), default=len(text))
        body = text[start:min(next_item, next_section)]
        count = len(re.findall(r"[\u3400-\u9fff]", body))
        if count < 65:
            errors.append(f"Item {match.group(1)} lacks a sufficiently informative factual summary.")
        if not re.search(r"信息来源[：:].+20\d{2}|信息来源[：:].+\d{1,2}月\d{1,2}日", body):
            errors.append(f"Item {match.group(1)} must name a source and its date.")

    if any(marker in text for marker in PROMO_MARKERS):
        errors.append("WeChat roundup must not contain follow/redirect promotions.")
    if any(marker in text for marker in BANNED_ANALYSIS_SCAFFOLD):
        errors.append("Weekly digest must not become a stock-trading playbook.")
    if re.search(r"https?://|www\.", text, flags=re.I):
        errors.append("WeChat public copy must not include off-platform URLs; use source notes.")

    if source_notes:
        if "复盘窗口" not in source_notes:
            errors.append("source_notes.md must declare a dated review window.")
        urls = re.findall(r"https?://\S+", source_notes)
        if len(urls) < max(1, len(items) - 2):
            errors.append("source_notes.md must retain source links for nearly all news items.")

    return errors


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("markdown", type=Path)
    p.add_argument("--source-notes", type=Path)
    args = p.parse_args()

    article = args.markdown.read_text(encoding="utf-8")
    source_path = args.source_notes or args.markdown.with_name("source_notes.md")
    notes = source_path.read_text(encoding="utf-8") if source_path.is_file() else ""
    problems = validate_roundup(article, source_notes=notes)
    if problems:
        for problem in problems:
            print("ERROR:", problem)
        return 1
    print("PASS: global finance news roundup editorial structure")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
