# Finance Prompt Chain — 3-Step Automated Pipeline

A multi-step prompt chain that takes raw financial numbers and automatically 
produces structured analysis, executive commentary, and an action plan 
with specific owners and deadlines.

## 🎯 Business Problem
Finance professionals spend hours translating raw numbers into 
structured reports. This pipeline does it in 3 automated steps — 
each building on the previous output.

## ⚡ How It Works

**Step 1 — Extract**
Raw financial numbers → Claude → structured JSON with variance amounts, 
percentages, verdict, and severity rating.

**Step 2 — Interpret**
JSON analysis → Claude → 3-sentence executive commentary 
written for CFO board pack.

**Step 3 — Act**
JSON + commentary → Claude → specific action plan with owners 
(CFO/Sales/Operations) and deadlines.

## 📊 Example Output
Step 1: {"verdict": "miss", "revenue_variance": -300000, "severity": "severe"}
Step 2: Revenue missed budget by 300K SEK (-6.7%)...
Step 3: • Sales Director: Present recovery plan by Friday
• CFO: Implement cost freeze within 5 days
• COO: Audit cost flex mechanisms within 10 days
## 🛠️ Tools
- Claude Sonnet API (Anthropic)
- Python 3.12
- python-dotenv

## 🚀 How to Run
```bash
git clone https://github.com/Ayman-Kassar/prompt-chain-finance
cd prompt-chain-finance
pip install anthropic python-dotenv
cp .env.example .env  # add your ANTHROPIC_API_KEY
python chain.py
```

## 💡 Key Concept
Each step receives the output of the previous step as its input.
Claude never sees the raw numbers in Step 3 — it works purely 
from the structured output of Steps 1 and 2.
This is the foundation of every serious AI finance automation system.

## 💼 Portfolio Context
Demonstrates prompt chaining — the core architecture behind 
multi-step AI finance workflows. Built as part of an AI Finance 
transformation portfolio by a 15+ year FP&A professional.
