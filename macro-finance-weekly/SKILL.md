---
name: macro-finance-weekly
description: Curate, fact-check, and draft Monday's Global Macro & US Equities Weekly Wrap (全球宏观与美股周报). Use when the user requests generating a weekly financial recap, analyzing US equity indices (S&P 500, Nasdaq), dissecting bond yields and currency movements, previewing the economic and earnings calendar, or building bull/base/bear scenario game plans.
---

# Macro & Finance Weekly (全球宏观与美股周报)

Use this skill to produce Monday's pre-market **Global Macro & US Equities Weekly Wrap**. This workflow replaces emotional stock tips and speculative forecasts with institutional-grade market tape review, liquidity analysis, and event-driven scenario planning.

## Core Directives

1. **Review the Previous Tape & Model (开篇复盘，对账前瞻)**:
   - Always open Section 0 by auditing the prior week's market calls and price action against reality.
   - Acknowledge when a move exceeded or defied the model; explain the mechanism delta instead of rationalizing.
2. **Follow Liquidity & Capital Flow (资金与机制穿透)**:
   - Price action is driven by balance sheets and flows, not mere media narratives.
   - Evaluate benchmark yields (US 10Y, 2Y), DXY (Dollar Index), Fed RRP/TGA liquidity, and equity volatility (VIX, Gamma flips).
3. **Multi-Branch Scenario Tree (三套情景推演)**:
   - For incoming catalysts (CPI, FOMC rate decisions, mega-cap earnings):
     - Never issue a single deterministic prediction.
     - Build three distinct branches: **Bullish Case**, **Base Case**, and **Bearish Case**, specifying the exact trigger threshold and asset reaction chain.
4. **Conclusion → Evidence → Mechanism → Trading Implication**:
   - Every substantive claim must clearly delineate the conclusion, observable data, economic transmission mechanism, and practical portfolio implication.
5. **Chart Support**:
   - Integrate fenced ```chart JSON (bars, levels, or kline) for key price levels or asset comparisons.

## Title & Structural Hard Rules (标题与结构硬性规范)

1. **Main Title (大标题 / H1)**:
   - **单点聚焦，选最重的一条 (Single Lead Theme)**: 严禁将两三起不同事件用逗号并列拼接在主标题中。必须从全周宏观博弈中筛选出最具决定性、最牵动全球资产定价的**唯一起核心矛盾**作为主线。
   - **抓人眼球，突出硬核冲突 (Eye-Catching & Conflict-Driven)**: 标题必须极具吸引力，直击预期与现实的反差（如流动性拐点、非农与通胀数据打架、美债异动冲击纳指等），杜绝平铺直叙的公文式汇报。
   - **严禁使用冒号 (Strictly No Colons)**: **大标题严禁使用冒号（无论是全角 `：` 还是半角 `:`）**！杜绝 `A：B` 模板，采用连贯自然、张力十足的叙事长句或逗号短语。
   - 归档与草稿末尾保留 `YYYYMMDD` 日期戳（如 `非农超预期未能打破降息定价，美股高位分歧开始加速暴露 20261026`）。

2. **Subheadings (小标题 / H2)**:
   - `## 0`, `## 1`, `## 2`, `## 3` 采用连贯自然的叙事实体短语，**严禁使用冒号（`:` 或 `：`）或 `xxx:xxx` 的套路化模板**。

3. **Natural Forward Outlook (自然前瞻，无内部黑话)**:
   - 最后一节（`## 3`）写清晰的情景分支与应对推演（Game Plan），**严禁在面向读者的正文中出现“长期合订本推演：”或“后续由事实合订本核对检验”等内部工程术语**。

## Structural Template (Fixed Four-Part Architecture)

- **Draft Title**: `[聚焦最重矛盾 + 强吸引力 + 无冒号自然标题] 2026MMDD`
- **`## 0 [盘面复盘与关键点位检验，无冒号]`**:
  - Weekly return stats across major indices (`**SPY**`, `**QQQ**`, `**IWM**`), 10Y Treasury yield, and commodities.
  - Transparent retrospective on last week's game plan.
- **`## 1 [核心宏观矛盾与资金面博弈，无冒号]`**:
  - The prevailing macro tug-of-war (e.g., growth resilience vs. sticky inflation, valuation multiple vs. risk-free rate).
  - Quantitative metrics: Treasury yield curve, Dollar index trend, credit spreads.
- **`## 2 [本周前瞻重磅事件与财报雷达，无冒号]`**:
  - Key economic calendar releases (time, consensus estimate, prior print).
  - High-impact corporate earnings releases with implied volatility metrics.
- **`## 3 [三套市场情景树与应对推演，无冒号]`**:
  - Scenario A (Bull), Scenario B (Base), Scenario C (Bear).
  - Explicit falsification levels (e.g., "S&P 500 support breaks below \$5,680 triggers defensive hedging").
  - Core thesis summary suitable for copy-ready X post with cashtags.

## Workflow

1. **Review Past Notes**: Ingest previous week's closing notes and calculate actual returns.
2. **Calendar Ingestion**: Gather verified dates and consensus estimates for macro releases and corporate earnings.
3. **Drafting**: Write the complete Markdown following `templates/macro-weekly-template.md`.
4. **Validation**: Run `python3 macro-finance-weekly/scripts/validate_macro_weekly.py` on the draft.
5. **Handoff**: Pass the verified Chinese draft to downstream humanizers (`humanizer-zh`), translation editors (`financial-english-editor`), and renderers.
