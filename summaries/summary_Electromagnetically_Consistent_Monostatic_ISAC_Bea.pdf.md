# Summary for Electromagnetically_Consistent_Monostatic_ISAC_Bea.pdf

**Caveat up front:** per your extraction, this is an EM-consistency/beamforming paper, not an exposure study — it reports no SAR, E-field, dose-rate, or ICNIRP/IEEE compliance metrics. "Dosimetry" here means antenna-level power balance and near-field current/leakage only.

## 1. Core Method
- Built a **multiport scattering model** of a compact collinear shared-aperture dipole array (10 GHz, λ = 3 cm; wire radius λ/200, 0.46λ resonant length, Z_in = 72.9 + j1.0 Ω vs Z₀ = 73 Ω; 8 Tx + 8 Rx ports) from **NEC-2 method-of-moments** runs, cross-checked against openEMS FDTD.
- The model yields the true power balance, **P_rad = ‖x‖² − ‖S_TTᵀx‖² − ‖S_RT x‖²**, and **realized embedded patterns** that include coupling, mismatch, and absorption in the Rx loads.
- Validation: reproduces a direct full-wave run to ~10⁻⁵–10⁻⁴ relative error; radiated power to 3.5×10⁻⁴.
- Used it to compare coupling-unaware designs against the proposed leakage-aware beamforming design.

## 2. Main Conclusions (power-deposition-relevant, not exposure metrics)
- Coupling grows sharply with spacing: −15.2 dB (0.5λ) → −8.1 dB (0.3λ) → −6.6 dB (0.2λ); a broadside beam leaks −17.9 dB into the Rx subarray at 0.3λ (≈12 dBm into LNAs for a 30 dBm Tx). Embedded patterns deviate several dB from the isolated 2.13 dBi pattern.
- Coupling-unaware designs mispredict pattern (1.7° squint, −1.9 dB on-target gain) and PA match (equivalent VSWR > 3.3).

| Metric | Baseline / pattern-aware | Proposed |
|---|---|---|
| Tx→Rx leakage | −16.5 dB | **−37.5 dB** |
| Rx share of strip-current power | −15.4 dB | **−35.1 dB** |
| P_rad/P_T (d = 0.3λ) | 82.2 % | 88.9 % |
| Active reflection / VSWR | 3.57 dB | 2.00 dB |
| Residual SI per Rx port | −75.5 dBm (+9.9 dB over thermal) | −96.5 dBm (below thermal) |

Takeaway: near-field leakage/deposition in compact arrays must come from the full multiport model, not the ideal array manifold.

## 3. Limitations / Future Work
The provided extraction contains **no author-stated gaps or future work**, so I won't invent any. Only scope boundaries are observable (not author claims): single frequency (10 GHz), one array geometry/spacing set, and no human-body/phantom or exposure-limit quantities. If you can share the paper's conclusion section, I can fill this in with the authors' actual stated limitations.