import anthropic
import json
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

# Your financial data
data = """
Revenue: 4.2M SEK actual vs 4.5M SEK budget
Costs: 3.1M SEK actual vs 2.9M SEK budget
Gross Profit: 1.1M SEK actual vs 1.6M SEK budget
Period: March 2026
"""

print("=" * 50)
print("STEP 1: Analysing numbers...")
print("=" * 50)

# STEP 1 — Extract key metrics as JSON
step1 = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": f"""
<data>{data}</data>

<instructions>
Analyse this financial data and return ONLY a JSON object with these fields:
- revenue_variance_amount (number, negative means miss)
- revenue_variance_pct (number, as percentage)
- cost_variance_amount (number, negative means overspend)
- cost_variance_pct (number, as percentage)
- profit_variance_amount (number)
- overall_verdict (string: "beat", "miss", or "mixed")
- severity (string: "minor", "moderate", "severe")

Return only the JSON. No explanation.
</instructions>
"""
        }
    ]
)

# Parse the JSON output from step 1
raw = step1.content[0].text.strip()
# Remove markdown code fences if present
if raw.startswith("```"):
    raw = raw.split("```")[1]
    if raw.startswith("json"):
        raw = raw[4:]
analysis = json.loads(raw.strip())
print(json.dumps(analysis, indent=2))

print("\n" + "=" * 50)
print("STEP 2: Writing commentary...")
print("=" * 50)

# STEP 2 — Write commentary based on JSON analysis
step2 = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=300,
    temperature=0,
    system="You are a CFO writing for a board pack. Be direct and concise.Always use SEK currency",
    messages=[
        {
            "role": "user",
            "content": f"""
<analysis>{json.dumps(analysis)}</analysis>

<instructions>
Write a 3-sentence executive variance commentary based on this analysis.
Sentence 1: Revenue performance.
Sentence 2: Cost performance.
Sentence 3: Overall impact and one recommended action.
</instructions>
"""
        }
    ]
)

commentary = step2.content[0].text
print(commentary)

print("\n" + "=" * 50)
print("STEP 3: Generating action plan...")
print("=" * 50)

# STEP 3 — Generate action plan based on commentary and analysis
step3 = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=400,
    temperature=0,
    system="You are a management consultant. Be specific and actionable.",
    messages=[
        {
            "role": "user",
            "content": f"""
<analysis>{json.dumps(analysis)}</analysis>
<commentary>{commentary}</commentary>

<instructions>
Based on the analysis and commentary above, generate a specific action plan.
Format as exactly 3 bullet points.
Each bullet point: Owner (CFO/Sales/Operations) + Action + Deadline.
Example: "• Sales Director: Present pipeline recovery plan covering Q2 shortfall — by Friday"
</instructions>
"""
        }
    ]
)

print(step3.content[0].text)

print("\n" + "=" * 50)
print("COMPLETE — 3 Claude calls chained successfully")
print("=" * 50)