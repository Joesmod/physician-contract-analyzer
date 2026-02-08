# Physician Contract Analyzer

AI-powered analysis of physician employment contracts. Upload a PDF, get a plain-English breakdown of key terms, risks, and red flags.

## Features

- **PDF Upload** — Accepts physician contract PDFs up to 20MB
- **Key Term Extraction** — Compensation, tail coverage, non-compete, termination, benefits, etc.
- **Risk Assessment** — Each term rated low/medium/high/critical
- **Red Flag Detection** — Automatically flags problematic clauses
- **Plain English** — Complex legal language translated to understandable summaries

## Quick Start

```bash
cd src
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
python main.py
```

API runs at `http://localhost:8000`. Swagger docs at `/docs`.

## API Endpoints

- `GET /health` — Health check
- `POST /analyze` — Upload PDF, get structured analysis

## Response Format

```json
{
  "summary": "Overall contract assessment...",
  "key_terms": [
    {
      "category": "Tail Coverage",
      "extracted_text": "Physician shall be responsible for...",
      "plain_english": "You pay for tail coverage if you leave",
      "risk_level": "critical"
    }
  ],
  "red_flags": [
    {
      "title": "No Employer Tail Coverage",
      "description": "Contract requires physician to pay tail coverage",
      "severity": "critical",
      "recommendation": "Negotiate employer-paid tail or tail-free policy"
    }
  ],
  "overall_risk_score": 7
}
```

## Pricing Tiers

- **Standard ($500)** — Key terms + red flags
- **Comprehensive ($1,200)** — Full analysis + negotiation points
- **Premium ($2,000)** — Analysis + attorney review + negotiation support

## License

MIT
