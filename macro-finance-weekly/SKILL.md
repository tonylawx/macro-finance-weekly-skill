---
name: macro-finance-weekly
description: Curate, fact-check, and draft Monday's Global Macro & US Equities Weekly Wrap (全球宏观与美股周报). Use when the user requests generating a weekly financial recap, analyzing US equity indices (S&P 500, Nasdaq), dissecting bond yields and currency movements, previewing the economic and earnings calendar, or building bull/base/bear scenario game plans.
---

# Macro & Finance Weekly (全球宏观与美股周报)

Use this skill to produce Monday's pre-market **Global Macro & US Equities Weekly Wrap**. This workflow replaces emotional stock tips and speculative forecasts with institutional-grade market tape review, liquidity analysis, and event-driven scenario planning.

## Core Directives

1. **Review the Previous Binder (开篇合订本复盘)**:
   - Always open Section 0 by auditing the prior week's market calls against reality.
   - Acknowledge when a move exceeded or defied the model; explain the mechanism delta instead of rationalizing.
2. **Follow Liquidity & Capital Flow (资金与机制穿透)**:
   - Price action is driven by balance sheets and flows, not mere media narratives.
   - Evaluate the benchmark yields (US 10Y, 2Y), DXY (Dollar Index), Fed RRP/TGA liquidity, and equity volatility (VIX, Gamma flips).
3. **Multi-Branch Scenario Tree (三套情景推演)**:
   - For incoming catalysts (CPI, FOMC rate decisions, mega-cap earnings):
     - Never issue a single deterministic prediction.
     - Build three distinct branches: **Bullish Case**, **Base Case**, and **Bearish Case**, specifying the exact trigger threshold and asset reaction chain.
4. **Conclusion → Evidence → Mechanism → Trading Implication**:
   - Every substantive claim must clearly delineate the conclusion, observable data, economic transmission mechanism, and practical portfolio implication.
5. **Chart Support**:
   - Integrate fenced ```chart JSON (bars, levels, or kline) for key price levels or asset comparisons.

## Structural Template (Fixed Four-Part Architecture)

- **Draft Title**: Clear, trend-oriented but measured, ending with `YYYYMMDD` (e.g., `非农超预期但降息逻辑未变：美股前瞻与期权推演 20261026`).
- **`## 0 盘面复盘与上期合订本校验`**:
  - Weekly return stats across major indices (`**SPY**`, `**QQQ**`, `**IWM**`), 10Y Treasury yield, and commodities.
  - Transparent retrospective on last week's game plan.
- **`## 1 核心矛盾与资金流动性`**:
  - The prevailing macro tug-of-war (e.g., growth resilience vs. sticky inflation, valuation multiple vs. risk-free rate).
  - Quantitative metrics: Treasury yield curve, Dollar index trend, credit spreads.
- **`## 2 本周前瞻：重磅事件与财报雷达`**:
  - Key economic calendar releases (time, consensus estimate, prior print).
  - High-impact corporate earnings releases with implied volatility metrics.
- **`## 3 市场情景树与应对推演 (Game Plan)`**:
  - Scenario A (Bull), Scenario B (Base), Scenario C (Bear).
  - Explicit falsification levels (e.g., "S&P 500 support breaks below \$5,680 triggers defensive hedging").
  - Core thesis summary suitable for copy-ready X post with cashtags.

## Workflow

1. **Review Past Notes**: Ingest previous week's closing notes and calculate actual returns.
2. **Calendar Ingestion**: Gather verified dates and consensus estimates for macro releases and corporate earnings.
3. **Drafting**: Write the complete Markdown following `templates/macro-weekly-template.md`.
4. **Validation**: Run `python3 macro-finance-weekly/scripts/validate_macro_weekly.py` on the draft.
5. **Handoff**: Pass the verified Chinese draft to downstream humanizers (`humanizer-zh`), translation editors (`financial-english-editor`), and renderers.
