# Macro & Finance Weekly Skill

Agent and Codex skill for market review, liquidity tracking, and scenario tree game planning for Monday's **Global Macro & US Equities Weekly Wrap (全球宏观与美股周报)**.

Rooted in institutional research discipline and **Industrial Content Engineering Methodology**:
1. **Follow the Capital Ledger & Real Costs**: Penetrate headline macro aggregates to calculate underlying liquidity balance sheets (Federal Reserve Reverse Repo Facility / RRP levels, Treasury General Account / TGA flows, federal debt interest expense pressures on long-term capital costs, and the divergence between real disposable personal income and consumption durability).
2. **Structure of Conflicts over Moralizing**: Reject simplistic moralistic framing; dissect the objective Nash equilibria and structural friction between Treasury debt financing requirements and bondholder term-premium demands, as well as inflation-fighting monetary postures vs. equity valuation multiples.
3. **Cognitive Ladder & 2-Turn Narrative Logic**: 70% familiar market consensus hooks to establish broad relevance + 30% institutional-grade analytical depth; strictly apply the two-turn cognitive progression (Consensus Narrative A $\to$ Accounting & Balance Sheet Disruption B $\to$ Systemic Institutional & Treasury Issuance Deadlock C).
4. **Historical Mirroring**: Benchmark current market price action against isomorphic historical regimes (e.g., Greenspan's 1995 preemptive rate cuts and subsequent yield rebounds, or the high-deficit, high-rate valuation squeeze of the 1980s).
5. **The Binder Protocol (Welcome Verification)**: Ensure every weekly wrap is entirely self-contained, presenting testable price thresholds, specific time horizons, and falsifiable market indicators without assuming prior-issue context.

## Repository Layout

```text
macro-finance-weekly-skill/
├── macro-finance-weekly/
│   ├── SKILL.md                          # Primary agent skill instructions
│   ├── references/
│   │   ├── industrial-media-methodology.md # Industrial media methodology & content engineering standard
│   │   ├── macro-research-standard.md    # Liquidity, attribution & scenario standards
│   │   └── event-calendar-guide.md       # Macro calendar & earnings radar guidance
│   ├── templates/
│   │   └── macro-weekly-template.md      # Rich five-layer paragraph structural template
│   └── scripts/
│       └── validate_macro_weekly.py      # Richness, volume, attribution & format validator
├── tests/
│   └── test_macro_weekly.py              # Test suite for weekly validator
├── LICENSE                               # MIT License
└── README.md
```

## Validation

```bash
python3 macro-finance-weekly/scripts/validate_macro_weekly.py path/to/draft.md [--source-notes path/to/source_notes.md]
```

## Running Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT © 2026 Tony Law
