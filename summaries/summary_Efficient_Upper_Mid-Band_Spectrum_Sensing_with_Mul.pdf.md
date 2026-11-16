# Summary for Efficient_Upper_Mid-Band_Spectrum_Sensing_with_Mul.pdf

**Note first:** The extraction confirms this paper is a signal-processing work on spectrum sensing, not a dosimetry study. So the summary below reflects what actually exists — and explicitly flags where dosimetry content is absent.

**1. Core Method**
- Frequency-domain occupancy estimation (spectrum sensing) for the 6–24 GHz upper mid-band (FR3).
- Detection via GLRT, with occupancy interval estimation formulated as a combinatorial optimization: binary search plus dynamic programming (weighted interval scheduling).
- Validation on simulated data and over-the-air measurements using a Pi-Radio SDR; 960 kHz bins over N = 1024 bins, unit-variance-normalized non-coherent power measurements, per-interval SNR estimates γₖ.
- Reported metrics: IoU (intersection-over-union) error rate and runtime — 0.74% of exhaustive ML search cost.

**2. Main Conclusions (dosimetry results)**
- **None.** No SAR, power density, absorbed dose, exposure limits, or safety margins are defined, measured, or discussed anywhere in the paper. The RF-power-related quantities are technical signal-processing parameters, not exposure metrics. Any dosimetry summary would be fabricated — so there is nothing to report here.

**3. Limitations / Future Work**
- None were captured in the extraction — the excerpt contains no author-stated limitations or future-work section. (The extraction only covers a methods/results summary and the reference list.)
- Observable scope boundaries from what was extracted: validation appears limited to simulation plus one SDR platform (Pi-Radio), and performance is benchmarked on IoU error and runtime only — but I can't attribute these as author-acknowledged gaps without the full text.

**Bottom line:** This appears to be a case of document/topic mismatch — the PDF is a cognitive-radio spectrum-sensing paper, and "IoU" here is intersection-over-union, not a dose metric. If you intended a different paper (e.g., an actual EMF-exposure/dosimetry work, or the "Part 2" body text referenced in your excerpt), share it and I'll produce the three-part summary as requested.