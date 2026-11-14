# Summary for Wearable_metasurfaces_for_boosting_the_effective_a.pdf

**Framing note:** The extracted content shows this is a metasurface/antenna-engineering paper, not a dosimetry study. An honest extraction must record "no dosimetry data" rather than infer any.

## 1. Core Method
- **Goal:** passive, screen-printed textile metasurface (worn on torso) that converts an incident 26 GHz plane wave into a guided surface wave toward the garment edge, boosting the device antenna's effective area (~10× reported).
- **Model:** semi-analytical thin-wire model (line currents on strips, r_eff = w/4) using the Green's function of a finite, grounded, lossy substrate; solved via an impedance matrix; accounts for finite metasurface size, substrate loss, and finite-conductivity ink.
- **Optimization:** multiple-population genetic algorithm tuning reactive loads X_L,n ∈ [−5×10⁵, −1.8×10⁵] Ω/m; TE normal incidence.
- **Materials:** cotton–polyester (ε_s = 1.81, tan δ_s = 0.015, h ≈ 2.2 mm); Metalon silver ink (ρ = 0.0716 Ω·µm → R_loss = 8.5×10³ Ω/m, best of three inks), printed on TPU film and laminated to textile.
- **Metrics:** FOM = fraction of P_inc redirected into the receiving region; power balance P_inc = P_sw + P_r + P_sca + P_abs; full-wave fields; measurements vs. rigid-PCB control.

## 2. Main Conclusions (dosimetry)
**None.** No SAR, power density, absorbed dose, tissue parameters, exposure-limit compliance, or body-exposure simulations appear anywhere in the extracted sections. The only adjacent statement is qualitative (incident mmWave power would otherwise be "mostly absorbed by biological tissue or scattered away"). For a dosimetry review, this paper should be logged as **out of scope / null extraction**.

*Technical conclusions (not dosimetry):* FOM ≈ 0.6 (lossless), degrading with length (Ly = 7λ–42λ) once losses are included; P_abs is the limiting term; measured ~8× (≈9 dB) textile vs. ~12× (≈10.8 dB) PCB; near-edge fields ~5× incident. (The ~8–12× received-power vs. ~10× effective-area figures are different metrics, not a contradiction.)

## 3. Limitations / Future Work
- **Author-stated limitations/future work:** not present in the extracted parts (Parts 3–5 cover fabrication, results, references only).
- **Limitations evident from results:** absorption dominates at large Ly; design is tied to 26 GHz, TE normal incidence, and this geometry; textile underperforms PCB control.
- **Dosimetry-relevant gaps (absent, not author-acknowledged):** no SAR/power-density data, no ICNIRP/FCC compliance assessment, no tissue/body modeling, no on-body exposure measurements, no curvature/posture/durability variability.

If other sections (e.g., discussion or an exposure subsection) contain SAR or exposure content, share them and I will extract accordingly.