============================================================
Experiment: 1. Opus 4.7 | system❌
Model: claude-opus-4-7 | Temp: None | System: ❌
============================================================
⏱️  Latency: 7.59s
📊 Tokens: input=208, output=500
💬 Answer:
# SWIFT MT103 Message - Parsed Fields

| Field | Value |
|-------|-------|
| **Sender BIC** | `CHASUS33AXXX` (JPMorgan Chase, USA) |
| **Receiver BIC** | `DEUTDEFFXXXX` (Deutsche Bank, Germany) |
| **Amount** | `10,000.00` |
| **Currency** | `USD` |
| **Remittance Info** | `INVOICE 2024-001 PAYMENT` |

## Additional Details Extracted

- **Block 1 (Basic Header):** `F01CHASUS33AXXX0000000000`
  - Application ID: `F` (FIN)
  - Service ID: `01`
  - Sender LT address: `CHASUS33AXXX`

- **Block 2 (Application Header):** `I103DEUTDEFFXXXXN`
  - Direction: `I` (Input/Outgoing)
  - Message Type: `103` (Single Customer Credit Transfer)
  - Receiver: `DEUTDEFFXXXX`
  - Priority: `N` (Normal)

- **Block 4 (Text Block):**
  - **:20:** Transaction Reference → `PAYREF123456`
  - **:23B:** Bank Operation Code → `CRED` (Credit Transfer)
  - **:32A:** Value Date / Currency / Amount → `2024-12-25 / USD / 10,000.00`
  - **

============================================================
Experiments: 2. Opus 4.7 | system✅
Model: claude-opus-4-7 | Temp: None | System: ✅
============================================================
⏱️  Latency: 2.41s
📊 Tokens: input=237, output=100
💬 Answer:
- **Sender BIC:** CHASUS33AXXX
- **Receiver BIC:** DEUTDEFFXXXX
- **Amount:** 10,000.00
- **Currency:** USD
- **Remittance Info:** INVOICE 2024-001 PAYMENT

============================================================
Experiments: 3. Sonnet 4.6 | system✅
Model: claude-sonnet-4-6 | Temp: None | System: ✅
============================================================
⏱️  Latency: 6.58s
📊 Tokens: input=172, output=395
💬 Answer:
## SWIFT MT103 Parsed Fields

| Field | Value |
|-------|-------|
| **Sender BIC** | `CHASUS33A` |
| **Receiver BIC** | `DEUTDEFFXXX` |
| **Amount** | `10,000.00` |
| **Currency** | `USD` |
| **Remittance Info** | `INVOICE 2024-001 PAYMENT` |

---

### Additional Extracted Fields

| Field | Tag | Value |
|-------|-----|-------|
| Transaction Reference | `:20:` | `PAYREF123456` |
| Bank Operation Code | `:23B:` | `CRED` |
| Value Date | `:32A:` | `2024-12-25` |
| Ordering Customer | `:50K:` | Acct: `12345678` / `JOHN DOE COMPANY` |
| Beneficiary | `:59:` | Acct: `87654321` / `JANE SMITH LTD` |
| Sender to Receiver Info | `:72:` | `URGENT SAME DAY` |

---

### Notes
- **Sender BIC** sourced from Block 1 (`F01` header): `CHASUS33A` → JP Morgan Chase
- **Receiver BIC** sourced from Block 2 (`I103` header): `DEUTDEFFXXX` → Deutsche Bank
- **Amount** formatted from `10000,00` (SWIFT comma-decimal notation) → `10,000.00`
- `:70:` is the designated **Remittance/Payment Details** field

============================================================
Experiments: 4. Haiku 4.5 | temp=0 | system✅ (3runs)
Model: claude-haiku-4-5-20251001 | Temp: 0 | System: ✅
============================================================

--- Run 1 ---
⏱️  Latency: 2.45s
📊 Tokens: input=171, output=192
💬 Answer:
# SWIFT MT103 Parse Results

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

## Additional Details
- **Reference**: PAYREF123456
- **Transaction Type**: Credit (CRED)
- **Value Date**: 25 December 2024
- **Sender Account**: /12345678 (JOHN DOE COMPANY)
- **Beneficiary Account**: /87654321 (JANE SMITH LTD)
- **Special Instructions**: URGENT SAME DAY

--- Run 2 ---
⏱️  Latency: 2.36s
📊 Tokens: input=171, output=186
💬 Answer:
# SWIFT MT103 Parse Results

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

## Additional Details
- **Reference**: PAYREF123456
- **Transaction Type**: Credit (CRED)
- **Value Date**: 25 December 2024
- **Sender Account**: /12345678 (John Doe Company)
- **Beneficiary Account**: /87654321 (Jane Smith Ltd)
- **Special Instructions**: URGENT SAME DAY

--- Run 3 ---
⏱️  Latency: 2.14s
📊 Tokens: input=171, output=186
💬 Answer:
# SWIFT MT103 Parse Results

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

## Additional Details
- **Reference**: PAYREF123456
- **Transaction Type**: Credit (CRED)
- **Value Date**: 25 December 2024
- **Sender Account**: /12345678 (John Doe Company)
- **Beneficiary Account**: /87654321 (Jane Smith Ltd)
- **Special Instructions**: URGENT SAME DAY

============================================================
Experiments: 5. Haiku 4.5 | temp=1 | system✅ (3runs)
Model: claude-haiku-4-5-20251001 | Temp: 1 | System: ✅
============================================================

--- Run 1 ---
⏱️  Latency: 1.96s
📊 Tokens: input=171, output=185
💬 Answer:
# SWIFT MT103 Parse Results

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

## Additional Details
- **Reference**: PAYREF123456
- **Transaction Type**: Credit Transfer (CRED)
- **Date**: 25 December 2024
- **Sender Account**: 12345678 (John Doe Company)
- **Receiver Account**: 87654321 (Jane Smith Ltd)
- **Special Instructions**: URGENT SAME DAY

--- Run 2 ---
⏱️  Latency: 2.05s
📊 Tokens: input=171, output=194
💬 Answer:
# SWIFT MT103 Parse Results

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

### Additional Details
- **Reference Number**: PAYREF123456
- **Value Date**: 25 Dec 2024
- **Transaction Type**: Credit Transfer (CRED)
- **Sender Account**: 12345678 (JOHN DOE COMPANY)
- **Beneficiary Account**: 87654321 (JANE SMITH LTD)
- **Special Instructions**: URGENT SAME DAY

--- Run 3 ---
⏱️  Latency: 2.04s
📊 Tokens: input=171, output=178
💬 Answer:
# SWIFT MT103 Extraction

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

**Additional Details:**
- **Reference:** PAYREF123456
- **Transaction Type:** CRED (Credit)
- **Value Date:** 25 Dec 2024
- **Ordering Customer:** JOHN DOE COMPANY
- **Beneficiary:** JANE SMITH LTD
- **Special Instructions:** URGENT SAME DAY

============================================================
Experiments: 6. Haiku 4.5 | temp=0 | system❌ (3runs)
Model: claude-haiku-4-5-20251001 | Temp: 0 | System: ❌
============================================================

--- Run 1 ---
⏱️  Latency: 2.36s
📊 Tokens: input=153, output=231
💬 Answer:
# SWIFT MT103 Message Parse

## Extracted Information:

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

## Additional Details:

- **Reference Number** (Field 20): PAYREF123456
- **Transaction Type** (Field 23B): CRED (Credit)
- **Value Date**: 24 December 2024
- **Ordering Customer** (Field 50K): JOHN DOE COMPANY (Account: 12345678)
- **Beneficiary** (Field 59): JANE SMITH LTD (Account: 87654321)
- **Sender's Charges** (Field 72): URGENT SAME DAY

--- Run 2 ---
⏱️  Latency: 2.56s
📊 Tokens: input=153, output=231
💬 Answer:
# SWIFT MT103 Message Parse

## Extracted Information:

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

## Additional Details:

- **Reference Number** (Field 20): PAYREF123456
- **Transaction Type** (Field 23B): CRED (Credit)
- **Value Date**: 24 December 2024
- **Ordering Customer** (Field 50K): JOHN DOE COMPANY (Account: 12345678)
- **Beneficiary** (Field 59): JANE SMITH LTD (Account: 87654321)
- **Sender's Charges** (Field 72): URGENT SAME DAY

--- Run 3 ---
⏱️  Latency: 2.87s
📊 Tokens: input=153, output=231
💬 Answer:
# SWIFT MT103 Message Parse

## Extracted Information:

| Field | Value |
|-------|-------|
| **Sender BIC** | CHASUS33AXXX |
| **Receiver BIC** | DEUTDEFFXXXX |
| **Amount** | 10,000.00 |
| **Currency** | USD |
| **Remittance Info** | INVOICE 2024-001 PAYMENT |

## Additional Details:

- **Reference Number** (Field 20): PAYREF123456
- **Transaction Type** (Field 23B): CRED (Credit)
- **Value Date**: 24 December 2024
- **Ordering Customer** (Field 50K): JOHN DOE COMPANY (Account: 12345678)
- **Beneficiary** (Field 59): JANE SMITH LTD (Account: 87654321)
- **Sender's Charges** (Field 72): URGENT SAME DAY

============================================================
Experiments: 7. Sonnet 4.6 | system✅ (3runs)
Model: claude-sonnet-4-6 | Temp: None | System: ✅
============================================================

--- Run 1 ---
⏱️  Latency: 6.77s
📊 Tokens: input=172, output=377
💬 Answer:
## SWIFT MT103 Parsed Fields

| Field | Value |
|-------|-------|
| **Sender BIC** | `CHASUS33AXXX` |
| **Receiver BIC** | `DEUTDEFFXXXX` |
| **Amount** | `10,000.00` |
| **Currency** | `USD` |
| **Remittance Info** | `INVOICE 2024-001 PAYMENT` |

---

### Additional Context
| Field | Tag | Value |
|-------|-----|-------|
| Transaction Reference | `:20:` | `PAYREF123456` |
| Bank Operation Code | `:23B:` | `CRED` |
| Value Date | `:32A:` | `2024-12-25` |
| Ordering Customer | `:50K:` | `A/C 12345678 — JOHN DOE COMPANY` |
| Beneficiary | `:59:` | `A/C 87654321 — JANE SMITH LTD` |
| Sender to Receiver Info | `:72:` | `URGENT SAME DAY` |

---

### Parsing Notes
- **Sender/Receiver BICs** extracted from block `{1:}` (LT address) and block `{2:}` respectively
- **Amount** decoded from field `:32A:` — format is `YYMMDD` + currency + amount (comma = decimal separator in SWIFT)
- **Remittance info** sourced from field `:70:` (purpose of payment)

--- Run 2 ---
⏱️  Latency: 6.96s
📊 Tokens: input=172, output=387
💬 Answer:
## SWIFT MT103 Parsed Fields

| Field | Value |
|-------|-------|
| **Sender BIC** | `CHASUS33AXXX` |
| **Receiver BIC** | `DEUTDEFFXXXX` |
| **Amount** | `10,000.00` |
| **Currency** | `USD` |
| **Remittance Info** | `INVOICE 2024-001 PAYMENT` |

---

### Additional Extracted Fields

| Field | Tag | Value |
|-------|-----|-------|
| Transaction Reference | `:20:` | `PAYREF123456` |
| Bank Operation Code | `:23B:` | `CRED` |
| Value Date | `:32A:` | `2024-12-25` |
| Ordering Customer | `:50K:` | Acct `/12345678` — `JOHN DOE COMPANY` |
| Beneficiary | `:59:` | Acct `/87654321` — `JANE SMITH LTD` |
| Sender to Receiver Info | `:72:` | `URGENT SAME DAY` |

---

### Parsing Notes
- **Amount** decoded from `10000,00` → SWIFT uses **comma as decimal separator**
- **Sender BIC** extracted from **Block 1** (`F01` + BIC + session/sequence)
- **Receiver BIC** extracted from **Block 2** (Input descriptor `I103` + BIC)
- **Value date** `241225` interpreted as **YYMMDD** → December 25, 2024

--- Run 3 ---
⏱️  Latency: 7.06s
📊 Tokens: input=172, output=393
💬 Answer:
## SWIFT MT103 Parsed Fields

| Field | Value |
|-------|-------|
| **Sender BIC** | `CHASUS33A` |
| **Receiver BIC** | `DEUTDEFFXXX` |
| **Amount** | `10,000.00` |
| **Currency** | `USD` |
| **Remittance Info** | `INVOICE 2024-001 PAYMENT` |

---

### Additional Extracted Fields

| Field | Tag | Value |
|-------|-----|-------|
| Transaction Reference | `:20:` | `PAYREF123456` |
| Bank Operation Code | `:23B:` | `CRED` |
| Value Date | `:32A:` | `2024-12-25` |
| Ordering Customer | `:50K:` | Acct `12345678` / `JOHN DOE COMPANY` |
| Beneficiary | `:59:` | Acct `87654321` / `JANE SMITH LTD` |
| Sender-to-Receiver Info | `:72:` | `URGENT SAME DAY` |

---

### Parsing Notes
> ⚠️ **Sender BIC** extracted from Block 1 (`F01` + `CHASUS33A`), padded zeros stripped.
> ⚠️ **Receiver BIC** extracted from Block 2 (`DEUTDEFFXXX`), trailing `X` padding normalized.
> ⚠️ **Amount** converted from MT103 comma-decimal format (`10000,00` → `10,000.00`).

============================================================
💰 Cost Calculation (reference)
============================================================

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