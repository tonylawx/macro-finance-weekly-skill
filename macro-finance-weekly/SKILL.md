---
name: macro-finance-weekly
description: Curate, fact-check, and draft Monday's Global Macro & US Equities Weekly Wrap (全球宏观与美股周报). Use when the user requests generating a weekly financial recap, analyzing US equity indices (S&P 500, Nasdaq), dissecting bond yields and currency movements, previewing the economic and earnings calendar, or building bull/base/bear scenario game plans following industrial media standards.
---

# Macro & Finance Weekly (全球宏观与美股周报)

Use this skill to produce Monday's pre-market **Global Macro & US Equities Weekly Wrap (全球宏观与美股周报)**. 
This workflow replaces speculative forecasts and emotional tips with institutional-grade market tape review, sovereign balance-sheet auditing, liquidity tracking, and event-driven scenario planning based strictly on verified historical facts from the preceding week.

---

## Default editorial routing — high-value global finance news with industrial-media analysis (2026-11-16)

**When the request is simply「财经周报」, this section overrides the old US-stock weekly-market-analysis format below.** The user already publishes US-equity market recaps every day, so the weekly edition is a **curated global finance news synthesis with original explanatory value**, not another SPY/QQQ technical review and not a newsroom bulletin board.

### A. Choose consequential stories, NOT a fixed news count

- Usually choose **4–7 truly important events**, never add filler to hit a number. Start from verified dated events in the preceding week, then rate *breadth and durability of impact*, *who earns/loses/pays*, *quality of primary evidence*, and *incremental explanation beyond generic press releases* (each 0–5).
- Retain only stories with both strong evidence and an identifiable economic mechanism. When two stories share a cause, merge them into one stronger story (e.g. CPI+PPI, exports+factory margins). Avoid low-incremental quarterly headlines and duplicate coverage from the separate tech weekly.
- Cover relevant developments across China, North America, Europe, global energy, currencies, trade and corporate balance sheets; **do not enforce artificial geography quotas**, but never let US stock-price action crowd out real global financial news.
- Explain omitted candidates in `source_notes.md` to make the curation decision inspectable. The score is a *qualitative editorial filter*, not a statistical prediction.

### B. Ma-Dugong-style reporting discipline — report + ask who pays

The durable intellectual standard is in [industrial-media-methodology.md](references/industrial-media-methodology.md). Apply it in *natural journalistic paragraphs*, not by literally printing A/B/C or rigid labels in the reader-facing article.

1. **Start from a concrete, attributable event** — what changed, exact date, number and comparison baseline. Do not silently equate a year-on-year rate with a monthly rate or a proposal with a completed transaction.
2. **Reconstruct the cash ledger** — source of funding, buyers and suppliers, profits vs revenue, debt vs equity, operating and financing costs, and the actual unit that bears the expense. When estimating, show arithmetic and explicit assumptions rather than presenting a sensitivity as disclosed cash cost.
3. **Map actors' incentives and constraints** — who gains bargaining power, who has to fund the outcome, who is left holding a maturity or margin problem. Avoid moralizing and conspiratorial claims about motives.
4. **Make two cognitive turns when justified by facts** — common interpretation → counterintuitive ledger observation → structural trade-off. No invented twists and no unsupported causal certainty.
5. **Close with an observable falsification test** — company margin, actual disbursement, shipping/insurance quote, audited profit, real policy action date, debt refinancing outcome, or later economic release. State what would weaken the interpretation.
6. **Cross-story synthesis** — choose one legitimate shared tension if present. Half-tree: selected news items feed into a clear common conclusion. Do not force unrelated stories into a universal thesis.

Prefer 2–4 substantial paragraphs per chosen event (usually **300–600 Chinese characters**), and typically **2,800–4,800 Chinese characters** total. A single dense, source-supported analysis beats ten 100-character press-release paraphrases. Do not reuse empty boilerplate like “未来值得继续关注”.

### C. WeChat search discoverability and safe platform operation BOTH matter

Compliance prohibits *bait and unsafe promotions*, not normal editorial discovery. **Never strip legitimate SEO content as a side effect of eliminating a QR code.**

- **Searchable, truthful H1 title:** `【财经周报】[1–3 important naturally phrased news topics + a real tension] YYYYMMDD`; no forced “全球X条新闻” or bait (“震惊/暴赚/一定”), no colons, no keyword-stuffing.
- **Concise 70–130-character WeChat digest** describing the major events and why reading is worthwhile; carry it into `meta.json.digest`.
- **IMMUTABLE RhinoFinance SEO masthead** at the top of every Chinese WeChat draft: exact visible line `美股 · 期权 · 资讯 · 观点` (English: `US Stocks · Options · News · Views`). Do not derive it from the article, replace it with weekly topic tags, or change its typography. News-specific discoverability belongs in factual H1, digest, sections and article body, not in this fixed brand line.
- **Semantic topic headings and natural long-tail terms** (e.g. 美国CPI/PPI、中国出口、国际油价、港企融资), accurate dates, original subheadings and self-contained facts. Indexable blog version retains the canonical URL and structured metadata on its own channel; WeChat's title, digest and body must stand alone.
- **IMMUTABLE WeChat style + heading hierarchy**: use the current `tonylawx/us-stock-analyst/templates/wechat-daily-four-part-minimal.html` as canonical rendering contract. Preserve its blue `#2763e9` line, `0 · LABEL` through `3 · LABEL`, 22px four `## 0..3` chapter titles, 16px readable body, standard paragraph spacing, fixed headline levels, and normal disclaimer. Weekly content curation does **not** authorize changing these UI/layout details. Group 4–7 important events into the four approved sections; their working-source `### 01` subheads are not additional large WeChat H3 headline blocks. In published HTML, use only subdued, factual **inline bold cues** for each event, not fabricated two-line labels, numerous large question headings or a new article-card design. No promo QR/header advert.
- **Source provenance** in `source_notes.md` with primary URLs and dated source labels visible in the article. Only remove real external-marketing redirects/QR/contact baits; retaining SEO does *not* require a click-through or a static follow banner.
- Draft creation may use the existing WeChat `draft/add` or `draft/update` path; **never auto-publish**. Native account card is added through the official editor after human review, until the platform's real card markup has been confirmed with draft/get + mobile preview. Ads/AI/rights and sensitive finance claims require actual editor verification.

### D. Quality gates

- Use `templates/finance-news-roundup-template.md` and `scripts/validate_finance_news_roundup.py`. The validator checks story count, number/date/source, explanatory ledger/incentive/falsification cues, and SEO lead metadata. **Passing a regex cannot certify accurate reporting, valuable synthesis, legal advice or WeChat recommendation eligibility.** Human review is mandatory.
- Preserve the legacy long-form macro template + `validate_macro_weekly.py` **only when the user explicitly asks for 宏观深度/美股周度策略/ETF 技术分析**.

## Core Mission: Building World Models & Avoiding Speculative Hype

The fundamental objective of this weekly wrap is **to help investors construct simplified, accurate macroeconomic world models, establish disciplined risk boundaries, and drastically lower the cognitive cost of market decision-making**.
Every edition represents an end-to-end industrial execution: **Empirical Tape Audit $\to$ Capital Ledger & Liquidity Penetration $\to$ Conflict Mapping & Historical Mirroring $\to$ Natural Forward Outlook & Invalidation Planning**.

### Methodological Pillars

1. **Follow the Capital Ledger & Real Costs (替普通人算账)**:
   - Audit real liquidity and sovereign debt dynamics beyond green/red closing ticks:
     - **Liquidity Reservoir Depletion**: Track the remaining Fed Reverse Repo (RRP) buffer, Treasury General Account (TGA) cash rebuilding, and bank reserve drainage.
     - **Sovereign & Corporate Debt Overhead**: Evaluate the impact of annualized federal interest outlays exceeding \$1 trillion and corporate debt rollover at 4.5%–5.0% benchmark rates.
     - **Headline GDP vs Real Purchasing Power**: Contrast headline growth metrics against contractions in real disposable income and consumer purchasing power.
2. **Structure of Conflicts over Moralizing (关注利益冲突)**:
   - Map structural frictions between economic agents rather than passing moral judgment:
     - **Treasury Borrowing Needs vs Creditor Term Premium Demands**: Treasury debt supply colliding with investor demands for higher term premiums to hedge sticky inflation.
     - **Restrictive Monetary Policy vs High-Multiple Asset Valuation**: Central bank hawkishness pushing against market hopes for rapid liquidity easing.
     - **Mega-Cap Breadth Distortion vs Broad Market Bleed**: Trillion-dollar tech weights masking underlying weakness across the equal-weight index.
3. **The Cognitive Ladder (70% Familiarity + 30% Hardcore Increment)**:
   - **70% Familiarity On-Ramp**: Anchor the introduction around broadly recognized market events (e.g. index testing a major round number, rate decision votes, Friday close).
   - **30% Hardcore Institutional Increment**: Deliver unique depth (Term Premium decomposition, Treasury QRA issuance maturity schedules, options gamma pinning).
4. **The Two-Turn Cognitive Hook (二次转折黄金认知阶梯)**:
   - Execute the 2-turn progression:
     - **Layer 0 (Consensus Narrative / Expectation A)**: Index appears range-bound, and yields edged slightly lower.
     - **Turn 1 (Ledger Reversal B)**: Micro-tape reveals semiconductor ETFs crashing 8% in a single session, real consumer purchasing power shrinking, and energy prices refusing to retreat.
     - **Turn 2 (Systemic Deadlock C)**: Heavy Treasury auction supply combined with rigid interest obligations caps discount-rate relief, proving that minor rate drops cannot offset earnings multiple compression.
5. **Historical Mirroring (打通历史与现实)**:
   - Benchmark present asset repricing against historical analogues (e.g. 1995 Greenspan preventive easing curve steepening, or 1980s stagflation episodes).
6. **The Half-Tree Rule & Road Transition Curves**:
   - Maintain the Half-Tree Principle: begin with the core tape audit and causal transmission chain, then branch concurrently into cross-asset impacts and calendar setups.
   - Embed connective logic bridges at section transitions to ensure smooth reading.
7. **The Binder Protocol (欢迎合订本)**:
   - Maintain self-contained, independent prose. Provide explicit pivot levels, observation horizons, and falsification criteria.
   - Internal auditing stays in working notes; **never expose author self-correction or assume readers read past editions**.

---

## Volume & Richness Mandate

To eliminate thin, superficial bullet points, the wrap enforces strict depth standards:

1. **Total Length**:
   - The Chinese draft (excluding chart JSON code) must achieve **3200 ~ 5000 characters** (minimum 2200 characters required).
2. **Paragraph Density & Progression**:
   - Each `##` section must contain **3 to 5 substantive paragraphs** (150–280 characters per paragraph). Single-paragraph sections are prohibited.
   - Advance through the standard sequence:
     - *Paragraph 1 (Tape Facts & Closes)*: Exact closing numbers, dates, and official exchange/terminal sources.
     - *Paragraph 2 (Capital Ledger Penetration)*: Real rates, interest expenses, TGA/RRP cash drains, and earnings multiples.
     - *Paragraph 3 (Conflict & Incentive Breakdown)*: Treasury vs creditors, hawkish Fed vs tech multiples.
     - *Paragraph 4 (Historical Analogies & Deadlocks)*: Mirroring historical easing/tightening cycles.
     - *Paragraph 5 (Pivot Levels & Execution)*: Actionable technical boundaries (`站稳`, `跌破`, `防守`).

---

## Title & Heading Hard Rules

1. **Main Title (大标题 / H1)**:
   - **Branded Column Prefix**: Must begin with `【财经周报】`.
   - **Single Lead Theme**: Select **exactly one dominant macro tension** as the main line. Never string multiple disparate events together with commas.
   - **Eye-Catching & Conflict-Driven**: Highlight core tension and contrast; avoid bureaucratic reporting.
   - **Strictly No Colons**: **Main title must NOT contain colons (`:` or `：`)**! Use natural narrative phrasing.
   - End with target date stamp `YYYYMMDD`.
2. **Subheadings (小标题 / H2)**:
   - Sections `## 0`, `## 1`, `## 2`, `## 3` must use natural narrative phrases without colons (`:` or `：`).
3. **Natural Forward Outlook**:
   - Section `## 3` discusses game plans and risk boundaries. Do NOT use formulaic enumeration (其一/其二/其三/乐观情景/悲观情景).
4. **Numeral Formatting**:
   - Always use standard Arabic numerals in headings and metrics (`5%`, `7580点`, `50基点`, `6周`). Do NOT use spelled-out Chinese numerals.
5. **Strictly No Retail Broker Software Citations**:
   - Never cite retail brokerage apps (长桥, 富途, 老虎证券, 雪盈证券). Attribute market data to official public exchanges, Bloomberg, or Reuters.

---

## Structural Architecture (Fixed Four-Part Template)

- **Draft Title**: `【财经周报】[Single Dominant Theme + Conflict-Driven + No Colons] 2026MMDD`
- **`## 0 [盘面复盘与关键点位检验，无冒号]`**:
  - Closing statistics as of Friday (core indices `**SPY**`, `**QQQ**`, `**SOXX**`, `**IWM**`, 10Y Treasury, DXY, commodities) with explicit dates and exchange/terminal attributions.
  - Audit weekly tape reversals, evaluate support/resistance validity, and dissect market breadth.
- **`## 1 [核心宏观矛盾与资金面博弈，无冒号]`**:
  - Dissect the week's primary macro conflict (e.g. commodity inflation, fiscal debt expansion, yield surge).
  - Penetrate liquidity and sovereign balance-sheet dynamics; benchmark against historical analogues; attach cross-asset chart (```chart).
- **`## 2 [本周前瞻重磅事件与财报雷达，无冒号]`**:
  - Preview upcoming Monday-to-Friday macro calendar (FOMC, PCE, Non-Farm Payrolls, Treasury QRA refunding) and mega-cap earnings (`**AAPL**`, `**MSFT**`, `**NVDA**`).
  - Explain institutional consensus and expectations gaps.
- **`## 3 [后市博弈焦点与核心防线，无冒号]`**:
  - Outline key S&P 500 multi-day decision pivots and defensive positioning rules.
  - Social media copy (X) is handled downstream by an independent editorial stage; the main article remains self-contained.

---

## Five-Stage Industrial Workflow

```text
[Stage 1: Timeline & Data Anchoring]
  - Restrict review window to [T-7, T-1] and outlook window to [T, T+4]
  - Force current year/month qualifiers; log verified data into source_notes.md
      ↓
[Stage 2: Capital Ledger & Conflict Mapping]
  - Calculate liquidity reservoirs (TGA/RRP), sovereign debt interest, real yields
  - Map structural frictions between market participants
      ↓
[Stage 3: Historical Mirroring & 2-Turn Logic]
  - Benchmark against isomorphic historical cycles (e.g. 1995, 1980)
  - Construct 2-turn arc: Surface stability -> Micro tape crash -> Debt supply deadlock
      ↓
[Stage 4: Long-Form Drafting (3200~5000 Chars)]
  - Follow templates/macro-weekly-template.md with 3-5 paragraphs per section
  - Weave Road Transition Curves between paragraphs
      ↓
[Stage 5: Automated Validation & Quality Gate]
  - Run python3 macro-finance-weekly/scripts/validate_macro_weekly.py <file>
  - Ensure zero colon in titles, no retail brokers, and sufficient richness
```
