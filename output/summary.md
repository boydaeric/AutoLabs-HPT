# Autonomic testing: hospital facility rates vs. independent-site Medicare

**These are hospital facility (outpatient department) rates from hospital price-transparency files. They bound independent-site rates from above. They are not AutoLabs' expected rates.**
Battery = 95924 + 95923. Physician fee = Medicare professional component, **$142.57**, used as an *approximation* because physician-group rates are not in hospital files. Benchmark = independent-site Medicare global for the battery, **$316.15** (CY2026 MPFS, Metro Boston 1421201).

## 1. Medicare site-of-service ratio, full battery
(hospital facility rate + $142.57) ÷ $316.15. Under OPPS, 95923 is status Q1: it is packaged, with no separate payment, when billed on the same claim as 95924 (status S). So the realistic Medicare facility payment for the battery is the 95924 APC alone.

| Hospital | Medicare facility source | Facility | + physician | **Ratio** | If 95923 paid separately |
|---|---|---|---|---|---|
| MGH | Hospital's Medicare FFS row, 95924 (median allowed, 84 claims) | $369.81 | $512.38 | **1.62x** | 2.05x (95923 not listed; national rate substituted) |
| BW Faulkner | Hospital's Medicare FFS row, 95924 (median allowed, 121 claims) | $369.81 | $512.38 | **1.62x** | 2.59x ($306.16 median allowed for 95923) |
| BIDMC | No Medicare rows in file; OPPS Addendum B national | $220.60 | $363.17 | **1.15x** | 1.58x |

Cross-check: the hospitals' 95924 Medicare price ($369.8) is **1.68x the CY2026 Addendum B national rate** ($220.60, APC 5722). That is more than the Massachusetts wage index explains (it would need an index of about 2.1). It is closer to APC 5723 ($381.24). The median allowed amounts confirm about $370 was actually paid. Addendum B rates are national and unadjusted for the Massachusetts wage index. So BIDMC's 1.15x is a floor.

## 2. Best available commercial comparators: BIDMC, hospital facility rates
Fee-schedule dollars. BIDMC publishes no allowed amounts for these codes.

| Payer / plan | 95924 | 95923 | Facility battery | + physician | ÷ $316.15 |
|---|---|---|---|---|---|
| Blue Cross Blue Shield — HMO | $325.87 | $255.23 | $581.10 | $723.67 | **2.29x** |
| Blue Cross Blue Shield — PPO | $340.79 | $266.92 | $607.71 | $750.28 | **2.37x** |
| Harvard Pilgrim — self-insured commercial | $396.97 | $310.92 | $707.89 | $850.46 | **2.69x** |

Blue Cross and Harvard Pilgrim list **no commercial rows** for these codes at any MGB hospital.

## 3. Median commercial facility rate for the battery
The headline uses median allowed amounts (what was actually paid) where the file gives them; otherwise the negotiated rate.

| Hospital | Commercial payer/plan pairs | Median facility battery | (negotiated median) | Median total ÷ $316.15 | Range |
|---|---|---|---|---|---|
| MGH | 9 | **$1,538.14** | $1,385.15 | **5.32x** | 2.89x – 8.86x |
| BW Faulkner | 5 | **$1,068.72** | $1,098.65 | **3.83x** | 2.56x – 5.08x |
| BIDMC | 3 | **$607.71** | $607.71 | **2.37x** | 2.29x – 2.69x |
| Brigham and Women's, Wentworth-Douglass | — | not listed | — | — | no rows for any payer |

## 4. Widest payer spreads (commercial facility battery, across plans and hospitals)
- **UnitedHealthcare:** $667 (Faulkner "New Business Discount") to $1,652 (MGH), **2.5x**. On negotiated rates it is $669 to $1,741, 2.6x.
- **Cigna:** $858 (Faulkner) to $1,626 (MGH HMO/PPO), **1.9x**.
- **Aetna (MGH, one plan):** allowed $2,658 vs negotiated $1,487. Paid amounts exceed the contract rate by 1.8x.
- Narrow: MGB Health Plan ($771–$808), Blue Cross at BIDMC ($581–$608), Wellpoint ($1,464–$1,538).

## Caveats
- **Hospital facility rates only.** Independent-site rates (the global fee, no facility fee) should sit well below these. Use them as an upper bound.
- **Sparse payer coverage.** A typical MGH charge line lists 3 payers, against 35 in the whole file. BIDMC lists 2–3 payers per code. Blue Cross and Harvard Pilgrim commercial rates appear only at BIDMC. Tufts appears only on Medicare Advantage plans. No MassHealth ACO or WellSense rows exist. Brigham and Women's and Wentworth-Douglass list none of the codes.
- **Medicare rows are missing where claims exist.** MGH lists no Medicare row for 95923, despite 95 Medicare patients in CY2024; the likely cause is packaging. BIDMC lists no Medicare rows despite 99 patients. See the Reconciliation tab.
- **Allowed-amount quality.** MGB medians look pooled at payer level: United's two MGH plans have identical medians. Some medians exceed the negotiated rate (Aetna, Wellpoint), possibly because of multiple units or a different plan mix.
- **Medicare mismatch.** APC prices in the files do not reconcile to CY2026 Addendum B with a single wage index (Medicare_check tab).
- **Physician fee approximation.** $142.57 is the Medicare professional component. Commercial physician rates would be higher, which makes the commercial totals understated.

*Sources: hospital MRFs (schema v3.0.0; MGB last updated 2026-03-27, BIDMC 2026-04-01); CMS OPPS Addendum B, July 2026; CY2026 MPFS and CY2024 patient counts as supplied. Detail: `autonomic_rate_summary.xlsx`.*
