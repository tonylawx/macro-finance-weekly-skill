import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "macro-finance-weekly" / "scripts"))
from validate_finance_news_roundup import validate_roundup


def make_draft(num=9):
    items = []
    for i in range(1, num + 1):
        items.append(
            f"### {i:02d} 测试新闻{i}\n\n"
            "11月10日官方公布价格和经济数据，新数据需要结合统计口径理解。"
            "相关部门的公开披露说明了具体规模，也指出了部分限制。"
            "这一变化主要涉及企业成本和消费支出，对未来结果不作保证。\n\n"
            "信息来源：中国国家统计局，2026年11月10日\n"
        )
    sections = ["## 0 经济新闻", "## 1 国际贸易", "## 2 企业融资", "## 3 下周日历"]
    return (
        "# 【财经周报】全球财经9条重要新闻 20261116\n\n"
        "过去一周有不少全球财经新闻。\n\n"
        + sections[0] + "\n\n"
        + "\n".join(items[:3])
        + "\n" + sections[1] + "\n\n"
        + "\n".join(items[3:6])
        + "\n" + sections[2] + "\n\n"
        + "\n".join(items[6:])
        + "\n" + sections[3] + "\n\n"
        "11月17日将公布下一批经济数据，时间以官方日程为准。"
    )


class NewsRoundupValidationTest(unittest.TestCase):
    def test_valid_news_roundup(self):
        self.assertEqual(validate_roundup(make_draft()), [])

    def test_rejects_shallow_us_stock_tape_instead_of_news(self):
        text = make_draft().replace("11月10日官方公布价格和经济数据，新数据需要结合统计口径理解。", "QQQ阻力位已到。")
        self.assertTrue(validate_roundup(text))

    def test_rejects_ungrounded_story_count(self):
        self.assertTrue(any("8–14" in x for x in validate_roundup(make_draft(7))))

    def test_blocks_external_link(self):
        self.assertTrue(any("URLs" in x for x in validate_roundup(make_draft() + " https://example.com")))


if __name__ == "__main__":
    unittest.main()
