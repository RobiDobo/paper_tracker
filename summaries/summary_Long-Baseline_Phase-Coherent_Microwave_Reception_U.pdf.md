# Summary for Long-Baseline_Phase-Coherent_Microwave_Reception_U.pdf

**Bottom line up front:** this is a phase-metrology/coherent-reception paper, not a dosimetry study. There are no dosimetric results to report, so sections 2 and 3 below distinguish (a) what the work actually shows from (b) what is *absent* and would be needed for any dosimetric use.

---

## 1. Core Method — what they did

- **Sensor:** Cs Rydberg EIT electrometry, ladder 6S₁/₂ → 6P₃/₂ → 56D₅/₂, with the microwave field coupling 56D₅/₂ → 57P₃/₂.
- **Architecture:** superheterodyne receiver in a TEM cell; a **3.989 GHz local oscillator is transported optically** and mixed against a test signal offset by **+5 kHz**, so the RF phase appears as a 5 kHz IF phase.
- **Remote readout:** atomic IF phase recovered over an **8 m free-space optical link** (probe 420 µW, coupling 40 mW, ~0.2 mm waists); the remote channel is **differenced against a local classical-mixer reference**, and a matched-SNR classical mixer pair supplies the instrumentation noise floor.
- **Data:** phase from complex FFT coefficients on two DAQ channels; 500 ms hardware-triggered records, ~1200 samples over 10 min.

## 2. Main Conclusions — and the dosimetry status

- **Phase performance (the actual results):** differential phase stable at ~24.5° with **σ = 0.476°** over 10 min (±1° spread, no systematic drift); overlapping Allan deviation **0.321° @ 0.5 s → 0.099° @ 60 s → 0.048° @ ~200 s**; phase-noise PSD **S_φ ∝ f^−0.46** (0.02–0.5 Hz); **~0.01°** phase recovery pre/post link interruption (≈ 99 µm, λ/756 electrical-path fluctuation, ~0.13% of the λ/B angular resolution); **10° phase steps tracked**.
- **Dosimetry results: none.** No E-field amplitude, power density, SAR, modulation/duty factor, or field-uniformity/vapor-cell localization is reported, and no comparison to exposure limits is made. The only dosimetry-relevant transferable element is the **platform capability**: remote, phase-calibrated RF E-field sensing — i.e., a candidate *measurement method*, not a dose or compliance result.

## 3. Limitations / gaps

*No author-stated limitations were captured in this extraction* (nothing from the paper's own discussion section is included), so the following are **gaps identified from what is absent** — treat them as inferred, not author-quoted:

- **No field-amplitude calibration** reported for the LO/test signals in the TEM cell → phase stability cannot be converted into an E-field uncertainty budget.
- **No dosimetric quantities** (power density, SAR, duty/modulation factors) and **no safety-threshold comparison**.
- **Spatial characterization missing** — field uniformity and the localized sensing volume within the vapor cell are not given.
- **Instrumentation-bound interpretation risk** — the classical mixer noise floor is only a reference; whether the atomic channel is system- or atom-limited at long τ isn't established here.
- **For dosimetric use, needed next steps:** absolute E-field calibration/traceability, mapping of field uniformity, reporting of amplitude plus modulation/duty factors, and explicit comparison against relevant exposure limits — plus extension of the phase-stable link to amplitude-dose metrology rather than phase alone.

If you can supply the paper's own "limitations/future work" text (or its conclusion section), I can separate author-stated gaps from the inferred ones above.