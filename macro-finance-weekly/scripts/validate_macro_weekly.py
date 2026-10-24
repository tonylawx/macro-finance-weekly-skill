#!/usr/bin/env python3
"""Validation script for Macro & Finance Weekly wrap draft."""

import re
import sys
from pathlib import Path

FORBIDDEN_WORDS = [
    "主播", "视频", "节目", "录音", "转录", "字幕", "原文",
    "上述内容", "这期", "本期节目", "文中提到", "作者提到",
    "他说", "她说", "暴富", "无脑做多", "无脑做空", "内幕消息",
]

REQUIRED_SECTIONS = [
    r"^## 0\s+",
    r"^## 1\s+",
    r"^## 2\s+",
    r"^## 3\s+",
]


def validate_text(text: str) -> list[str]:
    errors = []
    lines = text.strip().splitlines()

    # 1. Check Title (H1)
    h1_lines = [line for line in lines if line.startswith("# ")]
    if not h1_lines:
        errors.append("Missing H1 title (# Title).")
    else:
        title = h1_lines[0].strip()
        if not re.search(r"\b20\d{6}\b", title):
            errors.append(f"H1 title must end with target date in YYYYMMDD format (got: {title})")

    # 2. Check Required Sections
    for pattern in REQUIRED_SECTIONS:
        if not any(re.search(pattern, line) for line in lines):
            errors.append(f"Missing required section header matching: {pattern}")

    # 3. Check Forbidden words
    for word in FORBIDDEN_WORDS:
        count = text.count(word)
        if count > 0:
            errors.append(f"Found forbidden or unprofessional word '{word}' ({count} times).")

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

    # 6. Length check
    char_count = len(re.sub(r"\s+", "", text))
    if char_count < 1200:
        errors.append(f"Article is too terse: {char_count} characters (minimum 1200 recommended).")

    return errors


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_macro_weekly.py <markdown_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")
    errors = validate_text(content)

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
