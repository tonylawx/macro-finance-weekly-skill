import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "macro-finance-weekly" / "scripts"))
import validate_macro_weekly as macro_val


# Synthetic fixture for checking structure, richness, and attribution.
SAMPLE_VALID_MACRO = """# 【财经周报】示例利率上升后市场如何定价 20261026

## 0 示例指数与大盘复盘

据彭博社 10 月 23 日数据显示，标普500指数全周跌0.56%收报5780点，周内盘中一度跌破支撑位。对比 2024 年同期的降息预期，示例收益率走高，资金追高意愿受挫。

从盘面资金分化来看，大盘 ETF SPY 下跌0.56%，而纳指100 ETF QQQ 下跌1.97%，半导体板块抛压明显放大。虽然全周累计跌幅看似温和，但资金追涨意愿表现出明显的犹豫与分歧。

技术指标显示，关键支撑位并未形成稳固企稳形态。成交量能放大伴随高位回落，市场宽度呈现结构性收窄，需要等待盘面逐级确认。

## 1 示例宏观矛盾与流动性账本

根据美联储官方声明与劳工统计局 10 月 23 日公布的数据显示，基准收益率走高至4.94%，全周上涨6个基点。尽管通胀读数维持在3.1%，但货币当局依然维持紧缩姿态，降息窗口面临延后。

深入流动性账本测算，美联储逆回购 RRP 水位已降至2000亿美元关口，财政部 TGA 账户回补将直接消耗银行间超额准备金。企业在5%的高息环境下，现金流折现压力持续反噬估值乘数。

从利益博弈角度看，财政部发债诉求与债权人要求的期限溢价形成对立。高企的债务利息支出对财政政策构成刚性掣肘，折现率的边际上升加剧了长久期资产的波动。

## 2 示例重磅前瞻与财报雷达

周三盘后有一项核心科技巨头财报披露，官方公告显示市场预期营收增速为15%，重点关注 CapEx 资本开支能否转化为实际经营现金流。

按官方日程，周四北京时间21时30分将公布初请失业金人数，周五将公布关键月度非农就业报告，市场一致预期新增就业16.5万人。

劳动力市场温和降速利好宽松预期，但若失业率快速跳升则可能引发衰退与盈利双杀，事件密集期应警惕隔夜跳空风险。

## 3 示例后市博弈焦点与核心防线

盘面上，标普500指数的关键多空分水岭在5750点，若收盘失守该防线，下行防守区间将进一步移至5700点整数关口。

科技股内部结构呈现明显分化，均线指标显示纳指现价仍在200日均线上方运行，多头需要观察能否重返支撑位上方，防守纪律上必须控制单次风险敞口。

在宏观数据落地与财报密集披露期，若长端利率重新上行突破5%，博弈逻辑将更加偏向防御，仓位管理应以确定性为首要原则。市场在5700点至5800点区间内博弈，核心防御线不容有失。
""" + ("\n宏观分析保持客观严谨，跟踪盘面指标确认多空分水岭，支撑位在5720点，收益率维持在4.8%区间震荡。" * 30)


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
        bad_text = SAMPLE_VALID_MACRO.replace("据彭博社 10 月 23 日数据显示", "上期把示例点位设为观察线，据彭博社 10 月 23 日数据显示")
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


if __name__ == "__main__":
    unittest.main()
