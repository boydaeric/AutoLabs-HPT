# KFF chart data used for Figure 3

Downloaded October 15, 2026 with curl from Datawrapper, which serves KFF's chart data. Unchanged copies; `review/tools/build_figure_data.py` reads them.

| File | KFF source | URL |
|---|---|---|
| `ZdNkK_23.csv` | August 14, 2026 SDP brief, Figure 1 map (likelihood of impact, managed care status) | https://datawrapper.dwcdn.net/ZdNkK/23/dataset.csv |
| `UbS1f_14.csv` | August 14, 2026 SDP brief, Figure 4 (federal hospital SDP spending and spending above the new limits, 35 states) | https://datawrapper.dwcdn.net/UbS1f/14/dataset.csv |
| `q3dXL_7.csv` | August 20, 2026 provider tax brief, appendix table (any non-exempt tax above 3.5%, affected taxes) | https://datawrapper.dwcdn.net/q3dXL/7/dataset.csv |
| `ZJUAA_5.csv` | Status of State Medicaid Expansion Decisions (expansion tracker map data) | https://datawrapper.dwcdn.net/ZJUAA/5/dataset.csv, embedded at https://www.kff.org/medicaid/status-of-state-medicaid-expansion-decisions/ |

**Not available:** m5vRC/2 (August 20, 2026 map of expansion states with a non-exempt tax above 3.5%), recorded in `review/ledger/verification_v4_log.md`, returned HTTP 404 on October 15, 2026 (versions 1–5 and the unversioned URL; the server reports a delete marker). The map draws on the same state data as the appendix table q3dXL/7, from which the 31 and 28 counts were rebuilt.
