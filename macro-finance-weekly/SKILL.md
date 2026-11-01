---
name: macro-finance-weekly
description: Curate, fact-check, and draft Monday's Global Macro & US Equities Weekly Wrap (全球宏观与美股周报). Use when the user requests generating a weekly financial recap, analyzing US equity indices (S&P 500, Nasdaq), dissecting bond yields and currency movements, previewing the economic and earnings calendar, or building bull/base/bear scenario game plans.
---

# Macro & Finance Weekly (全球宏观与美股周报)

Use this skill to produce Monday's pre-market **Global Macro & US Equities Weekly Wrap**. This workflow replaces emotional stock tips and speculative forecasts with institutional-grade market tape review, liquidity analysis, and event-driven scenario planning based strictly on verified historical facts from the preceding week.

## 核心原则：真实收集总结，严禁凭空捏造 (Strict News Gathering, Zero Hallucination)

周报的核心价值在于对**上一周已经发生的真实宏观与盘面事实**进行严谨收集、交叉核验与穿透算账，严禁任何形式的虚构、模糊推测或年份穿越：
1. **固定时间窗口边界 (Strict Time Window Boundary)**:
   - 周报发布于周一清晨（基准日 $T$，如 `2026-10-26`）。
   - **上周复盘窗口 (Review Window)**：严格限定在**上周一至上周日（$[T-7, T-1]$，即 10-19 至 10-25）**。盘面数据覆盖上周五个交易日（周一至周五，$[T-7, T-3]$），宏观事件覆盖至周日。
   - **本周前瞻窗口 (Outlook Window)**：严格限定在**本周一至周五（$[T, T+4]$，即 10-26 至 10-30）**。
   - **检索纪律**：搜索背景资料时，**必须强制加上当期年份与月份（如 `2026年10月` 或 `October 2026`）**，严禁使用宽泛无时间约束的搜索词，更严禁把历史年份（如 2024 年）当作当期事实。
2. **强制交代具体日期与权威信源 (Mandatory Source & Date Attribution)**:
   - 正文 `## 0` 和 `## 1` 中，凡提及的核心指数收盘价、美债收益率变动、宏观数据公布、官方决策，**必须明确写清具体日期（如 `10月23日` 或 `上周五`）及权威信源出处（如 `据美国劳工统计局公布`、`彭博社数据显示`、`路透社报道`、`美联储官方声明`）**。
   - 严禁出现“日前”、“最近”、“前段时间”、“据悉”、“传闻”等无具体日期和无出处的模糊表述。
3. **研究底稿台账化 (`source_notes.md`)**:
   - 必须在运行目录中保留 `source_notes.md`，开头必须写清复盘窗口与前瞻窗口。
   - 逐条罗列每起宏观事件的名称、发生具体日期（YYYY-MM-DD）和权威信源出处链接/机构名。
4. **严禁引用零售券商软件 (Strictly No Retail Broker Attribution)**:
   - 严禁在正文、图表注释或底稿中出现“长桥”、“长桥数据”、“长桥日线”、“富途”、“老虎证券”等零售券商或炒股软件字样。
   - 盘面收盘数据、技术形态与均线指标，必须归属到公共市场、官方交易所或彭博社、路透社等专业终端口径（如“据公开市场交易所数据”、“彭博社收盘数据显示”、“技术面日线走势显示”）。
   - 财报日历归属到上市公司官方披露公告或《巴伦周刊》等权威周历，杜绝引用零售券商日历。
5. **正文完全独立自洽，严禁预设读者已知往期上下文 (Self-Contained Standalone Writing, Zero Prior Context Assumption)**:
   - 每期周报都是面向全网读者的独立深度分析，**严禁预设读者读过上期、严禁把作者个人视角的合订本纠错或备忘录写进面向读者的正文**：
   - **杜绝作者个人自纠元叙述**：严禁出现“上期把...设为观察线”、“上期写下的...也应收回”、“上期日历把...应更正为...”、“正如上期所言”等把内部回溯暴露给读者的行文。
   - **点位与结构直接陈述**：对关键分水岭点位，直接客观剖析其盘面技术意义（例如：“7580点作为近期多空关键分水岭，周五收盘几乎压线……”），而不写成“上期设定的观察线”。
   - **预期偏差与逻辑证伪直接分析市场传导**：不向读者交代作者个人往期研判，而是分析全市场共识机制的演化（例如：“此前市场普遍预期...然而随着...现实走势打破了线性推导”）。
   - **前瞻日历直接列出最新权威官方排期**：日历部分清晰交代本周权威发布的事件与具体时间，严禁声称“更正上期的错误”。

## Core Directives

1. **Review the Previous Tape & Model (开篇复盘，对账前瞻)**:
   - Always open Section 0 by auditing the prior week's market calls and price action against reality with verified Friday closing numbers.
   - Acknowledge when a move exceeded or defied the model; explain the mechanism delta instead of rationalizing.
2. **Follow Liquidity & Capital Flow (资金与机制穿透)**:
   - Price action is driven by balance sheets and flows, not mere media narratives.
   - Evaluate benchmark yields (US 10Y, 2Y), DXY (Dollar Index), Fed policy rate, and commodity inflation pressures (e.g. Brent crude).
3. **Strategic Game Plan & Risk Management (后市博弈与关键分水岭)**:
   - For incoming catalysts (CPI, FOMC rate decisions, mega-cap earnings):
     - Identify clear market pivot levels and portfolio defensive boundaries in a cohesive narrative.
     - Strictly avoid mechanical, formulaic branch enumeration (do NOT use "其一乐观、其二基准、其三悲观"). Provide clear falsification criteria and asset reactions naturally.
4. **Conclusion → Evidence → Mechanism → Trading Implication**:
   - Every substantive claim must clearly delineate the conclusion, observable data, economic transmission mechanism, and practical portfolio implication.
5. **Chart Support**:
   - Integrate fenced ```chart JSON (bars, levels, or kline) for key price levels or asset comparisons.

## Title & Structural Hard Rules (标题与结构硬性规范)

1. **Main Title (大标题 / H1)**:
   - **带有栏目标识 (Branded Column Prefix)**: 中文大标题开头必须使用栏目标识 `【财经周报】`。
   - **单点聚焦，选最重的一条 (Single Lead Theme)**: 严禁将两三起不同事件用逗号并列拼接在主标题中。必须从全周宏观博弈中筛选出最具决定性、最牵动全球资产定价的**唯一起核心矛盾**作为主线。
   - **抓人眼球，突出硬核冲突 (Eye-Catching & Conflict-Driven)**: 标题必须极具吸引力，直击预期与现实的反差，杜绝平铺直叙的公文式汇报。
   - **严禁使用冒号 (Strictly No Colons)**: **大标题严禁使用冒号（无论是全角 `：` 还是半角 `:`）**！杜绝 `A：B` 模板，采用连贯自然、张力十足的叙事长句或逗号短语。
   - 归档与草稿末尾保留 `YYYYMMDD` 日期戳。

2. **Subheadings (小标题 / H2)**:
   - `## 0`, `## 1`, `## 2`, `## 3` 采用连贯自然的叙事实体短语，**严禁使用冒号（`:` 或 `：`）或 `xxx:xxx` 的套路化模板**。

3. **Natural Forward Outlook (自然前瞻，无内部黑话与刻板分支)**:
   - 最后一节（`## 3`）写清晰的交易应对与防守逻辑（Game Plan），**严禁在面向读者的正文中机械枚举“其一乐观、其二基准、其三悲观”，严禁出现“长期合订本推演：”或“后续由事实合订本核对检验”等内部工程术语**。以连贯的深度报道笔触剖析多空博弈胜负手。

4. **Numeral Formatting (标题与小标题数字规范)**:
   - **一律使用阿拉伯数字 (Always Use Arabic Numerals)**: 大标题和小标题中的利率、百分比、点位、基点与时间周期，**一律使用标准的阿拉伯数字**（例如 `5%`、`7620点`、`50基点`、`6周`），**严禁在标题中拼写为汉字大写或汉字数字**。

## Structural Template (Fixed Four-Part Architecture)

- **Draft Title**: `【财经周报】[聚焦最重矛盾 + 强吸引力 + 无冒号自然标题] 2026MMDD`
- **`## 0 [盘面复盘与关键点位检验，无冒号]`**:
   - 上周收盘统计（截至上周五，注明日期与行情源），包含核心指数（`**SPY**`、`**QQQ**`、`**IWM**`）、十年期美债、美元与大宗商品。
   - 对账上期策略，客观评价预期差。
- **`## 1 [核心宏观矛盾与资金面博弈，无冒号]`**:
   - 剖析上周最核心的宏观冲突（如大宗暴涨引发通胀重估、高息环境下估值挤压）。
   - 交代具体发布日期与官方出处，穿透流动性与资产负债表机制。
- **`## 2 [本周前瞻重磅事件与财报雷达，无冒号]`**:
   - 梳理本周（周一至周五，标明具体日期与周几）重磅宏观日程（如 FOMC、PCE、非农）及核心财报。
- **`## 3 [后市博弈焦点与核心防线，无冒号]`**:
   - 提炼关键多空分水岭点位与仓位防御纪律。
   - 给出适合发布在 X 上的观点提要与互动问题。

## Workflow

1. **Verify Timeline & Anchor Window**: Define $T$ and restrict review window to $[T-7, T-1]$.
2. **Collect Real Data & Populate `source_notes.md`**: Query verified market quotes and macro releases for the target window, logging specific dates and sources.
3. **Drafting**: Write complete Markdown adhering to `templates/macro-weekly-template.md`.
4. **Validation**: Run `python3 .codex/skills/macro-finance-weekly/scripts/validate_macro_weekly.py <file>`.
5. **Handoff**: Pass the verified draft to humanizer, translation editor, and blog/WeChat renderers.
