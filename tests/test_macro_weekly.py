import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "macro-finance-weekly" / "scripts"))
import validate_macro_weekly as macro_val


# Synthetic fixture for checking structure and attribution.
SAMPLE_VALID_MACRO = """# 【财经周报】示例利率上升后市场如何定价 20261026

## 0 示例指数回顾

据彭博社 10 月 23 日数据显示，示例指数收跌。对比 2024 年同期的降息预期，示例收益率走高。

## 1 示例利率观察

根据示例机构 10 月 23 日公布的数据显示，收益率走高。

## 2 示例财报日历

周三盘后有一项示例财报。

## 3 示例支撑位和风险

示例仅用于测试。
""" + ("\n示例仅用于测试。" * 180)


class WeeklyValidatorTest(unittest.TestCase):
    def test_valid_macro_weekly_passes(self):
            errors = macro_val.validate_text(SAMPLE_VALID_MACRO)
            self.assertEqual(errors, [])

    def test_macro_weekly_stale_year_fails(self):
            bad_text = SAMPLE_VALID_MACRO.replace("对比 2024 年同期的降息预期", "美联储在 2024 年宣布全面降息")
            errors = macro_val.validate_text(bad_text)
            self.assertTrue(any("Mentions past year 2024" in err for err in errors))

    def test_macro_weekly_missing_date_fails(self):
            bad_text = SAMPLE_VALID_MACRO.replace("10 月 23 日", "某日")
            errors = macro_val.validate_text(bad_text)
            self.assertTrue(any("Section ## 0 lacks specific dates" in err for err in errors))

    def test_macro_weekly_vague_time_fails(self):
            bad_text = SAMPLE_VALID_MACRO.replace("10 月 23 日公布的数据显示", "日前公布的数据显示")
            errors = macro_val.validate_text(bad_text)
            self.assertTrue(any("Found vague temporal phrase '日前'" in err for err in errors))

    def test_macro_weekly_retail_broker_fails(self):
            bad_text = SAMPLE_VALID_MACRO.replace("据彭博社 10 月 23 日数据显示", "据长桥 10 月 23 日数据显示")
            errors = macro_val.validate_text(bad_text)
            self.assertTrue(any("Found retail broker reference '长桥'" in err for err in errors))

    def test_macro_weekly_assumed_context_fails(self):
            bad_text = SAMPLE_VALID_MACRO.replace("据彭博社 10 月 23 日数据显示，示例指数收跌", "上期把示例点位设为观察线，据彭博社 10 月 23 日数据显示，示例指数收跌")
            errors = macro_val.validate_text(bad_text)
            self.assertTrue(any("Found assumed prior-issue context" in err for err in errors))

    def test_source_notes_validation(self):
            valid_notes = """# 周报研究底稿与信源台账
    - **发布基准日**: 2026-10-26
    - **复盘窗口**: 2026-10-19 至 2026-10-25
    - **核心数据**: 2026-10-23 示例指数 (彭博社发布数据)
    """
            self.assertEqual(macro_val.validate_source_notes(valid_notes), [])

            missing_window_notes = """# 周报研究底稿
    - **核心数据**: 2026-10-23 示例指数 (彭博社发布数据)
    """
            self.assertTrue(len(macro_val.validate_source_notes(missing_window_notes)) > 0)
