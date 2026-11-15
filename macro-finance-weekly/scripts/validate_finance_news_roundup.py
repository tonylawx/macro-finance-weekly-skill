#!/usr/bin/env python3
"""Check curated global finance weekly structure, depth and editorial SEO.

This gate cannot determine whether news is true or the analysis is valuable:
source verification and human editing remain mandatory before publishing.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TITLE_RE = re.compile(r"^#\s+【财经周报】.+\s(20\d{6})\s*$", re.M)
SECTION_RE = re.compile(r"^##\s+\d+\s+(.+)$", re.M)
ITEM_RE = re.compile(r"^###\s+(\d{2})\s+(.+)$", re.M)
BANNED_TRADING_JARGON = (
    "看涨情景", "看跌情景", "做多信号", "做空信号",
    "入场点位", "止损点位", "标普技术位", "QQQ阻力",
)
PROMO_MARKERS = (
    "长按识别二维码", "关注后查看", "阅读原文查看完整版",
    "扫码进群", "私信领取", "点击阅读原文",
)
LEDGER_CUES = (
    "成本", "账", "资金", "利润", "现金流", "融资", "贷款", "负债", "债务", "利息",
    "股东", "消费者", "供应", "采购", "保险", "汇率", "价格", "供应链", "毛利",
)
VERIFICATION_CUES = (
    "验证", "核对", "观察", "跟踪", "接下来", "下周", "后续", "届时",
    "未来", "应该看", "再看", "下一步", "判断", "指标",
)
SEO_TOPIC_TERMS = ("通胀", "CPI", "PPI", "出口", "贸易", "经济", "能源", "油价", "债务", "企业", "融资", "汇率", "消费", "半导体")


def han_count(text: str) -> int:
    return len(re.findall(r"[\u3400-\u9fff]", text))


def validate_roundup(text: str, *, source_notes: str = "", digest: str = "") -> list[str]:
    errors: list[str] = []
    title = text.splitlines()[0].strip() if text.strip() else ""
    if not TITLE_RE.search(text):
        errors.append("H1 must start with 【财经周报】 and end in YYYYMMDD.")
    elif ":" in title or "：" in title:
        errors.append("H1 title must not contain colons.")

    sections = list(SECTION_RE.finditer(text))
    if len(sections) < 3:
        errors.append("A news synthesis needs at least 3 thematic ## sections.")

    items = list(ITEM_RE.finditer(text))
    if not 4 <= len(items) <= 7:
        errors.append(f"Curate 4–7 high-value sourced events, without padding; found {len(items)}.")

    numbers = [int(m.group(1)) for m in items]
    if numbers and numbers != list(range(1, len(items) + 1)):
        errors.append("News numbers must be consecutive starting at 01.")

    for i, item in enumerate(items):
        start = item.end()
        end = min(
            items[i + 1].start() if i + 1 < len(items) else len(text),
            min((s.start() for s in sections if s.start() > start), default=len(text)),
        )
        body = text[start:end]
        if han_count(body) < 230:
            errors.append(f"Story {item.group(1)} is only a news paraphrase; develop the financial ledger (min 230 Han characters).")
        if not re.search(r"(?:信息)?来源[：:].+(?:20\d{2}|\d{1,2}月\d{1,2}日)", body):
            errors.append(f"Story {item.group(1)} needs a named dated source.")
        if not re.search(r"\d+(?:\.\d+)?\s*(?:%|美元|日元|港元|亿|万|元|股|月|日)", body):
            errors.append(f"Story {item.group(1)} needs a verifiable numeric anchor.")
        if not any(cue in body for cue in LEDGER_CUES):
            errors.append(f"Story {item.group(1)} needs a cash/cost/incentive analysis, not only headline data.")
        if not any(cue in body for cue in VERIFICATION_CUES):
            errors.append(f"Story {item.group(1)} needs an observable future verification test.")

    if not any(term in title for term in SEO_TOPIC_TERMS):
        errors.append("SEO title should name an actual financial topic, not generic 'X headlines'.")
    first_screen = text[:420]
    if "美股 · 期权 · 资讯 · 观点" not in first_screen:
        errors.append("WeChat first screen must retain the immutable 美股 · 期权 · 资讯 · 观点 brand line.")
    if digest and (han_count(digest) < 40 or han_count(digest) > 170):
        errors.append("Wechat digest must be concise and topical (normally 70–130 Chinese characters).")

    if any(x in text for x in PROMO_MARKERS):
        errors.append("WeChat native content cannot include follow/redirect promotions.")
    if any(x in text for x in BANNED_TRADING_JARGON):
        errors.append("Weekly digest must not turn into US-equity trading signals.")
    if re.search(r"https?://|www\.", text, flags=re.I):
        errors.append("WeChat body must not embed off-platform URLs; retain research links in source notes.")

    if source_notes:
        if "复盘窗口" not in source_notes:
            errors.append("Source notes must declare dated review window.")
        urls = re.findall(r"https?://\S+", source_notes)
        if len(urls) < len(items):
            errors.append("Source notes need an attributable URL for each selected story.")
        if "未纳入" not in source_notes and "排除" not in source_notes:
            errors.append("Source notes should record which candidate news stories were excluded and why.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--source-notes", type=Path)
    parser.add_argument("--meta", type=Path)
    args = parser.parse_args()
    article = args.markdown.read_text(encoding="utf-8")
    notes_path = args.source_notes or args.markdown.with_name("source_notes.md")
    notes = notes_path.read_text(encoding="utf-8") if notes_path.is_file() else ""
    meta_path = args.meta or args.markdown.with_name("meta.json")
    digest = ""
    if meta_path.is_file():
        digest = str(json.loads(meta_path.read_text(encoding="utf-8")).get("digest") or "")
    problems = validate_roundup(article, source_notes=notes, digest=digest)
    if problems:
        for problem in problems:
            print("ERROR:", problem)
        return 1
    print("PASS: curated global finance weekly (structure, ledger cues and SEO)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
