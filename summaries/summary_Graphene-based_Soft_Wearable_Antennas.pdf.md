# Summary for Graphene-based_Soft_Wearable_Antennas.pdf

## Summary of "Graphene-based Soft Wearable Antennas" (as extracted)

**1. Core Method**
- Fabricated a CPW-fed planar inverted-cone antenna from CVD-grown multi-layer graphene laminated on cellulosic textile (graphene sheet resistance ≈ 25 Ω/sq; textile substrate εr = 1.58, tanδ = 0.02 measured by resonant-perturbation cavity method with an Agilent 85072A split-cylinder resonator at 10 GHz; adhesive layer loss negligible).
- Targeted UWB operation (3–9 GHz) and characterized performance in free space vs. on-body, under bending and torso proximity.
- Body-exposure modelling used a four-layer torso phantom (1 mm skin / 3 mm fat / 40 mm muscle / 1 mm air gap under the antenna) with a tissue-mimicking liquid (79.7% DI water, 0.25% NaCl, 16% Triton X-100, 4% DGBE, 0.05% boric acid) representing muscle (highest εr and σ). Tissue dielectric data were quoted at 2.45 GHz (e.g., muscle εr = 52.729, σ = 1.7388 S/m).
- Dosimetry was *inferred* from S11, gain, and radiation patterns at 3/5/7 GHz, using CST simulations cross-validated against VNA measurements.

**2. Main Conclusions**
- The torso phantom absorbed the backward-radiated fields, strongly degrading the front-to-back ratio relative to free space.
- The *physical* phantom absorbed more energy than the numerical model, attributed to surface-wave enhancement from the antenna's curvature-directed design.
- The full ground plane minimized radiation toward the body, and ≥6 GHz bandwidth (3–9 GHz) was retained on-body → qualitatively "low power deposition in tissue."
- ⚠️ **Caveat:** No SAR values, power-density metrics, or ICNIRP/FCC compliance assessment are reported anywhere in the provided excerpts; dosimetry conclusions are qualitative, based on antenna parameters only.

**3. Limitations / Gaps** *(inferred — the authors do not state future work in these excerpts)*
- Absence of explicit dosimetric quantities (SAR, power density, exposure-limit comparison).
- Tissue properties given only at 2.45 GHz despite a 3–9 GHz operating band.
- Simulation–phantom mismatch (physical phantom absorbed more) suggests the numerical model may underestimate absorption.
- Single torso configuration; no other body sites/postures reported.
- Parts 4–5 contain only funding and references — no additional dosimetry content to extract.

**Bottom line:** Solid antenna engineering + phantom-based body-interaction study, but it stops short of true dosimetry; SAR/exposure-limit analysis would be the logical next step.