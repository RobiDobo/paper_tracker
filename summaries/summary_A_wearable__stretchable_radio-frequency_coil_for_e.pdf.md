# Summary for A_wearable__stretchable_radio-frequency_coil_for_e.pdf

## Bottom line up front

The paper reports **no explicit dosimetry** — no SAR, no B1+rms, no temperature-rise/thermal modeling, no ICNIRP/IEC-limit compliance. All "dosimetry-relevant" content is indirect, via coil-efficiency and coupling proxies. Any SAR statement would have to be inferred, not extracted.

---

## 1. Core Method

**Device under test:** a wearable, stretchable RF coil — Litz wire (1,500 strands × 30 µm, vs. ~35 µm copper skin depth at these frequencies) stitched in a serpentine path on elastic textile; 30 turns, 23 cm length, 13–14.5 cm diameter (stretchable). Benchmarks: rigid copper solenoids (15/18 cm, 30/44 turns).

**Conditions:** 2.13–5.32 MHz (50–125 mT), including scanner frequencies 3.04 MHz (71 mT) and 3.53 MHz (83 mT); ACR phantom and in-vivo knee loading (NextMRI, Physio I systems).

**Measurements:**
- Q from S₁₁ bandwidth at −7 dB (VNA) → unloaded/loaded Q; loading factor LF = 1 − Q_loaded/Q_unloaded as the sample-coupling (RF-exposure coupling) metric.
- Pickup-coil efficiency ε = √(2R_L/(4πf))·S·N·S₂₁/√P_in (µT/√W).
- In-scanner transmit efficiency by Rabi-flop.
- SNR (phantom + in-vivo).

## 2. Main Conclusions (proxies only)

- **Litz vs. copper crosses over near ~3.1 MHz:** at 3.04 MHz Litz is marginally better (Q 518 vs 504; ε 49 vs 48 µT/√W); at 3.53 MHz slightly worse → any SAR-per-unit-SNR comparison must be frequency-dependent.
- **Stretchable coil couples most strongly to the sample:** LF = 0.72 (NextMRI) / 0.76 (Physio I) vs 0.53 / 0.44 for RFC-Litz → sample-noise-dominated operation, i.e., better conformity/filling factor. Authors caution LF is **not** a merit figure (higher LF ⇒ stronger capacitive body–coil coupling, potential EMI pathway).
- **Transmit efficiency comparable or higher:** in vivo 31 vs 30 µT/√W (NextMRI), 48 vs 43 (Physio I); phantom up to 40 vs 37 and 56 vs 50.
- **SNR gain:** ≈8% at 3.53 MHz, ≈20% at 3.04 MHz in phantom; ~1.3× phantom, ~1.8–2.0× in-vivo vs the rigid reference.
- **Dosimetric implication (unmeasured):** comparable-or-better efficiency for equal B1+ implies comparable-or-lower required drive power, hence potentially lower deposited power — but this was **not quantified**.

## 3. Limitations / Future Work

**Stated by authors:**
- B1+ homogeneity was not isolated; direct B1+ mapping or EM simulation is explicitly future work.
- Coil deformation under stretch flagged as a potential B1+ inhomogeneity source; only evidence is a small, unquantified contrast variation in axial STIR images.
- LF is not a performance figure of merit.

**Absent / would be required for any exposure claim:** SAR (average/local), B1+rms, temperature rise or thermal modeling, ICNIRP/IEC compliance, stretch-state-dependent efficiency, and frequency-dependent (Litz skin/proximity effect) drive-power accounting.

**Source caveat:** this summary is from the supplied excerpts only (methods/results excerpt; the bibliography excerpt [4]–[55] contains no dosimetry content). Full-text sections on coil safety testing, SAR estimation, or thermal measurement — if they exist — were not available; provide them for extraction.