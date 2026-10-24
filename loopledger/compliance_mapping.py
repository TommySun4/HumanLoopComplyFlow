"""D: mappings are possible supporting evidence, never compliance conclusions."""
COMPLIANCE_MAPPING = [
    {
        "framework": "EU AI Act",
        "reference": "Article 12 — Record-keeping",
        "expectation": "High-risk AI systems should support automatic event logging and traceability.",
        "loopledger_feature": "Decision, gate and review events; integrity check",
        "evidence_field": "event_counts, total_events, integrity.chain_intact",
        "limitation": "Prototype retention, completeness and production logging have not been evaluated.",
        "source_url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12",
    },
    {
        "framework": "EU AI Act",
        "reference": "Article 13 — Transparency to deployers",
        "expectation": "Provide information that helps deployers appropriately interpret and use system outputs.",
        "loopledger_feature": "Shown predictions, confidence and illustrative contributing factors",
        "evidence_field": "events with prediction payloads; demo review interface",
        "limitation": "Mock factor values are NOT SHAP, nor full user instructions or tested explanations.",
        "source_url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-13",
    },
    {
        "framework": "EU AI Act",
        "reference": "Article 14 — Human oversight",
        "expectation": "Enable effective human monitoring, interpretation and override, accounting for automation bias.",
        "loopledger_feature": "Review queue, overrides, synthetic gold-control catch rate and review-time metrics",
        "evidence_field": "reviewer_metrics, system_stats",
        "limitation": "Heuristic metrics alone cannot establish effective human oversight.",
        "source_url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14",
    },
    {
        "framework": "ISO/IEC 42001:2023",
        "reference": "AI management system (high-level alignment)",
        "expectation": "An organizational framework for establishing and improving AI management.",
        "loopledger_feature": "Structured monitoring records and exportable evidence summaries",
        "evidence_field": "report_metadata, system_stats, reviewer_metrics, integrity",
        "limitation": "No clause-by-clause conformity assessment or accredited certification is performed.",
        "source_url": "https://webstore.iec.ch/en/publication/90574",
    },
]
