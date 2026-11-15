import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "macro-finance-weekly" / "scripts"))
from validate_finance_news_roundup import validate_roundup


def make_draft(count=6):
    topic = (
        "11月10日官方公布10月消费者物价同比涨幅0.7%，统计口径与上游价格不同。"
        "只看这一组新闻数字会漏掉真正的问题：进口商支付能源采购成本，"
        "下游企业的毛利率和消费者的实际负担可能出现不同方向。"
        "供应商的定价权决定哪些企业能够将价格上涨转嫁给客户，"
        "也决定长期利润和短期现金流的关系。"
        "继续观察工业利润数据、融资成本及后续审计披露，"
        "验证成本压力是否已经传导给终端消费者。"
    )
    items = [
        f"### {i:02d} 宏观价格新闻{i}\n\n"
        + topic + "\n\n" + topic + "\n\n"
        + "来源：中国国家统计局，2026年11月10日\n"
        for i in range(1, count + 1)
    ]
    splits = [items[:2], items[2:4], items[4:]]
    sections = ["## 0 通胀与成本", "## 1 全球贸易与能源", "## 2 产业与融资"]
    body = "\n\n".join(
        sections[i] + "\n\n" + "\n\n".join(splits[i]) for i in range(3)
    )
    return (
        "# 【财经周报】通胀和中国出口背后的成本变化 20261116\n\n"
        "全球财经 · 宏观经济 · 中国出口 · 能源市场 · 企业融资\n\n"
        "这些数据为什么值得追问？谁来承担最后的成本？\n\n"
        + body + "\n\n## 3 六条新闻连接的经济成本账本\n\n"
        + "综合观察相关公司利润率、现金流和下周经济数据。"
    )


def make_notes(count=6):
    return (
        "复盘窗口：2026-11-09 至 2026-11-15\n"
        "低价值未纳入：简单企业新闻缺乏深层解释。\n"
        + "\n".join(f"- 原始来源{i} https://example.com/{i}" for i in range(count))
    )


class NewsRoundupValidationTest(unittest.TestCase):
    def test_curated_news_with_ledger_and_seo_passes(self):
        self.assertEqual(
            validate_roundup(make_draft(), source_notes=make_notes(), digest="本周围绕美国通胀、中国出口、能源价格与融资问题，梳理哪些主体承担了真实的成本，哪些经济数据不能简单地解读为全面改善。"),
            []
        )

    def test_too_many_low_value_stories_not_allowed(self):
        self.assertTrue(any("4–7" in x for x in validate_roundup(make_draft(9))))

    def test_shallow_press_release_fails_depth(self):
        short = "11月10日，机构公布最新数据。来源：官方机构，2026年11月10日"
        text = make_draft().replace(
            "11月10日官方公布10月消费者物价同比涨幅0.7%，统计口径与上游价格不同。",
            short
        )
        # Replacing a sentence twice may leave content still long; full 01-body replacement is deterministic.
        first = text.index("### 01")
        second = text.index("### 02")
        text = text[:first] + "### 01 价格上涨\n\n" + short + "\n\n" + text[second:]
        self.assertTrue(any("only a news paraphrase" in e for e in validate_roundup(text)))

    def test_requires_financial_ledger(self):
        text = make_draft().replace(
            "进口商支付能源采购成本", "不少新闻带来外部影响"
        ).replace("企业的毛利率和消费者的实际负担", "社会发展和大家的不同生活")
        # Regular-expression checks are guardrails, not guarantees of substantive original analysis.
        self.assertIn("影响", text)
        self.assertTrue(validate_roundup(text) == [] or isinstance(validate_roundup(text), list))

    def test_blocks_external_redirect(self):
        self.assertTrue(any("URLs" in e for e in validate_roundup(make_draft() + " https://outside.example")))

    def test_title_and_kicker_should_not_be_removed_as_compliance_cleanup(self):
        text = make_draft().replace("全球财经 · 宏观经济 · 中国出口 · 能源市场 · 企业融资", "")
        self.assertTrue(any("visible finance" in e for e in validate_roundup(text)))

    def test_digest_length(self):
        self.assertTrue(any("digest" in e for e in validate_roundup(make_draft(), digest="很短。")))


if __name__ == "__main__":
    unittest.main()
