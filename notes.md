# SWIFT Parser Model Experiment — 2026.05.17

## Example SWIFT MT103 Message
{1:F01CHASUS33AXXX0000000000}
{2:I103DEUTDEFFXXXXN}
{4:
:20:PAYREF123456
:23B:CRED
:32A:241225USD10000,00
:50K:/12345678
JOHN DOE COMPANY
:59:/87654321
JANE SMITH LTD
:70:INVOICE 2024-001 PAYMENT
:72:URGENT SAME DAY
-}

## Key Findings
- Haiku 4.5 > Sonnet 4.6 in BIC accuracy
- System prompt = 3x faster + 5x cheaper
- Temperature=0 required for consistency
- More expensive model ≠ more accurate

## Bugs Found
- Sonnet 4.6: BIC truncation error
  CHASUS33AXXX → CHASUS33A (9 chars, wrong)
  DEUTDEFFXXXX → DEUTDEFFXXX (10 chars, wrong)
  → Wrong BIC = payment failure in production
- Without system prompt:
  Field 72 mislabelled as "Sender's Charges"
  Value Date parsed as 24th instead of 25th

## Measured Results (Haiku 4.5, system prompt ON, temp=0)
- Latency: 2.14~2.45s (avg ~2.3s)
- Input tokens: 171/message
- Output tokens: ~188/message (avg)

## Cost Calculation (1,000 messages/day)
Input:  1,000 × 171 / 1,000,000 × $1.00 = $0.171
Output: 1,000 × 188 / 1,000,000 × $5.00 = $0.940
Total:  ~$1.11/day

### Model Comparison
| Model     | Daily cost | Accuracy        |
|-----------|------------|-----------------|
| Haiku 4.5 | ~$1.11     | ✅ BIC correct  |
| Sonnet 4.6| ~$3.33     | ❌ BIC error    |
| Opus 4.7  | ~$5.55     | not measured    |

## Design Decisions
- Model: claude-haiku-4-5-20251001
- Temperature: 0
- System prompt: required
- Estimated cost: ~$1.11/day (based on measured tokens)

## Next Steps
→ Add Pydantic structured output
  - Enforce BIC as exactly 11 characters
  - Resolve case inconsistency (JOHN DOE vs John Doe)
  - Guarantee type-safe parsing results
→ Generate 50 mock messages and run full eval

## Architecture Decision
- Regex for structured fields (:20:, :32A:, :50K:, :59:)
- LLM only for free-text (:70:, :72:)
- Reason: cost optimization + LLM adds value only where regex fails
- Estimated cost reduction: ~80% vs full LLM parsing