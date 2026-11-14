# Summary for Artificial_magnetic_conductor_backed_dual-mode_sec.pdf

## Summary: AMC-Backed Dual-Mode QCDRA — SAR/Dosimetry

### 1. Core Method
- Designed a wearable sectoral cylindrical dielectric resonator antenna (QCDRA) for 5.2–5.9 GHz and applied a 7×9 AMC surface to its back side to simultaneously boost gain and suppress power absorbed by body tissue.
- Computed average SAR per Eq. (21), SAR_avg = (1/ρ)∫σ(r)|E(r)|²dr, via FDTD following IEC/IEEE 62704-1, simulating the antenna at 1 W input placed 2 mm above a human-arm voxel model.
- Verified compliance against IEEE C95.1/ECC-CEPT limits (1.6 W/kg for 1 g, 2 W/kg for 10 g, 4 W/kg peak for 1 g), then back-calculated the maximum allowable input power: P_max = P_in × (SAR_limit/SAR_achieved).
- Compared no-ground-plane (no AMC) vs. AMC-backed designs; the AMC's in-phase reflection permits only ~0.0867λ₀ (5 mm) antenna–body spacing vs. 0.25λ₀ for a PEC reflector (~65% thickness reduction).

### 2. Main Conclusions
- **Without AMC:** intense back radiation drove SAR to 53.3 W/kg (10 g, 1 W) — far above limits — restricting safe input power to just 37.5 mW.
- **With AMC:** SAR dropped to 1.24 W/kg (EH₁₁₀) / 1.26 W/kg (TE₂₁₀) for 10 g at 1 W, i.e., within IEEE C95.1-2019 limits even at full 1 W input.
- Gain rose from ~4.1–4.4 dBi to 8.01–8.2 dBi (measured peak 7.9 dBi); efficiency fell from >86% (free-standing) to <70% on the arm, but was restored to >80% with the AMC — indicating less power coupled into tissue.
- Trade-offs: bandwidth shrank from 22.2% to 12.6%; thickness increased to 0.16λ₀.

### 3. Limitations / Future Work
- The provided excerpt contains **no explicit author-stated limitations or future-work section**; it notes only that detailed SAR analysis is deferred to Section IV (not included here).
- Documented trade-offs that function as implicit limitations: ~10-point bandwidth loss, added thickness, and reduced on-body efficiency vs. free-space operation.
- Any further gaps (e.g., other body sites, phantom vs. real-tissue validation, multi-band operation) cannot be reported without fabricating content — please share Section IV if these details are needed.