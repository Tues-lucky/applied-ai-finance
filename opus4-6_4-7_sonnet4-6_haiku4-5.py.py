from anthropic import Anthropic
import time

client = Anthropic()

# Common question (SWIFT-related)
QUESTION = "Parse this SWIFT MT103 message and extract: sender BIC, receiver BIC, amount, currency, and remittance info.\n\n{1:F01CHASUS33AXXX0000000000}{2:I103DEUTDEFFXXXXN}{4:\n:20:PAYREF123456\n:23B:CRED\n:32A:241225USD10000,00\n:50K:/12345678\nJOHN DOE COMPANY\n:59:/87654321\nJANE SMITH LTD\n:70:INVOICE 2024-001 PAYMENT\n:72:URGENT SAME DAY\n-}"

SYSTEM_PROMPT = "You are a SWIFT MT103 parser. Extract fields precisely and concisely."

def run_experiment(name, model, temperature, use_system, runs=1):
    print(f"\n{'='*60}")
    print(f"Experiment: {name}")
    print(f"Model: {model} | Temp: {temperature} | System: {'✅' if use_system else '❌'}")
    print('='*60)

    # Check for models where temperature is deprecated
    no_temp_models = ["opus-4-7", "opus-4-6", "sonnet-4-6"]
    use_temperature = not any(m in model for m in no_temp_models)

    for i in range(runs):
        start = time.time()

        kwargs = {
            "model": model,
            "max_tokens": 500,
            "messages": [{"role": "user", "content": QUESTION}]
        }

        if use_system:
            kwargs["system"] = SYSTEM_PROMPT

        if use_temperature:
            kwargs["temperature"] = temperature

        response = client.messages.create(**kwargs)
        
        elapsed = time.time() - start
        
        if runs > 1:
            print(f"\n--- Run {i+1} ---")
        
        print(f"⏱️  Latency: {elapsed:.2f}s")
        print(f"📊 Tokens: input={response.usage.input_tokens}, output={response.usage.output_tokens}")
        print(f"💬 Answer:\n{response.content[0].text}")


# ─────────────────────────────────────────
# Experiment 1: Opus, temp=None (deprecated), system X
# ─────────────────────────────────────────
run_experiment(
    name="1. Opus 4.7 | system❌",
    model="claude-opus-4-7",
    temperature=None,
    use_system=False,
)

# ─────────────────────────────────────────
# Experiment 2: Opus, temp=None (deprecated), system O
# ─────────────────────────────────────────
run_experiment(
    name="2. Opus 4.7 | system✅",
    model="claude-opus-4-7",
    temperature=None,
    use_system=True,
)

# ─────────────────────────────────────────
# Experiment 3: Sonnet, temp=None (deprecated), system O
# ─────────────────────────────────────────
run_experiment(
    name="3. Sonnet 4.6 | system✅",
    model="claude-sonnet-4-6",
    temperature=None,
    use_system=True,
)

# ─────────────────────────────────────────
# Experiment 4: Haiku, temp=0, system O (3 runs)
# ─────────────────────────────────────────
run_experiment(
    name="4. Haiku 4.5 | temp=0 | system✅ (3runs)",
    model="claude-haiku-4-5-20251001",
    temperature=0,
    use_system=True,
    runs=3,
)

# ─────────────────────────────────────────
# Experiment 5: Haiku, temp=1, system O (3 runs)
# ─────────────────────────────────────────
run_experiment(
    name="5. Haiku 4.5 | temp=1 | system✅ (3runs)",
    model="claude-haiku-4-5-20251001",
    temperature=1,
    use_system=True,
    runs=3,
)

# ─────────────────────────────────────────
# Additional Experiment 6: Haiku, temp=0, system X (3 runs)
# Verify the difference with/without system prompt in Haiku
# ─────────────────────────────────────────
run_experiment(
    name="6. Haiku 4.5 | temp=0 | system❌ (3runs)",
    model="claude-haiku-4-5-20251001",
    temperature=0,
    use_system=False,
    runs=3,
)

# ─────────────────────────────────────────
# Additional Experiment 7: Sonnet, temp=None (deprecated), system O (3 runs)
# ─────────────────────────────────────────
run_experiment(
    name="7. Sonnet 4.6 | system✅ (3runs)",
    model="claude-sonnet-4-6",
    temperature=None,
    use_system=True,
    runs=3,
)

# ─────────────────────────────────────────
# Additional Experiment 8: Cost Calculation
# ─────────────────────────────────────────
print(f"\n{'='*60}")
print("💰 Cost Calculation (reference)")
print('='*60)
print("""
Model pricing (per 1M tokens):
- Opus 4.7:   input $5,    output $25
- Sonnet 4.6: input $3,    output $15
- Haiku 4.5:  input $1,    output $5

If parsing 1,000 SWIFT messages per day:
- Average input: ~500 tokens/message
- Average output: ~200 tokens/message

Haiku:  (500*1000/1M)*$1 + (200*1000/1M)*$5  = $0.50 + $1.00  = $1.50/day
Sonnet: (500*1000/1M)*$3 + (200*1000/1M)*$15 = $1.50 + $3.00  = $4.50/day
Opus:   (500*1000/1M)*$5 + (200*1000/1M)*$25 = $2.50 + $5.00  = $7.50/day

→ Haiku is 5x cheaper than Opus
→ If accuracy is the same, always choose Haiku
""")