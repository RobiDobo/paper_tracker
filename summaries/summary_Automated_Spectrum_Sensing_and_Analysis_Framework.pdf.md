# Summary for Automated_Spectrum_Sensing_and_Analysis_Framework.pdf

## 1. Core Method

**Automated, multi-site spectrum-*utilization* monitoring (not an exposure study).**

- **Sensing hardware:** Signal Hound BB60C scanners with calibrated antennas; cable-loss/nonlinearity correction; optional LNA and lightning protection.
- **Acquisition:** Timestamped frequency–power observations logged to Parquet files, gated by a receive-power threshold; per-site volumes ~30–200 GB/day.
- **Transport/storage:** Lossless 7-ZIP/LZMA at level 9 (~5:1, ~20% residual size) → central FTP server → NAS; system parameters partitioned into minute/hourly JSON (frequency range, resolution bandwidth, sweep time, coordinates, antenna/LNA type).
- **Analysis:** Python + MATLAB compute channel occupancy and airtime-utilization (AU) metrics → MySQL → web dashboard; includes ops monitoring/failure detection.
- **Metric definition:** AU over 5-MHz channels using a −72 dBm/20 MHz occupancy threshold.
- **Example deployments:** Anchorage AK, Washington DC, Louisville, Purdue, Ohio State; mid-band (~450 MHz) AU results reported for June 2025 at Anchorage and Louisville.

## 2. Main Conclusions — Dosimetry

**There are none.** The excerpt explicitly contains no dosimetric quantities — no E-field strength, power density, SAR, whole-body or localized averaging, exposure ratios, or comparison to ICNIRP/FCC limits. The only quantitative findings are operational:

- ~100% airtime utilization in the f1–f2 sub-segment of mid-band, with the remainder of mid-band largely unused.
- Calibrated power-level measurements are described as the *type* of data that **could** feed an RF-exposure assessment, but no such assessment was performed.

Note that "AU ≈ 100%" is a *threshold-crossing occupancy* statistic, not a dose or field-strength result — it cannot be converted to exposure without antenna factor, duty-cycle/peak statistics, geometry, and time-averaging per compliance standards.

## 3. Limitations / Future Work

**Author-stated limitations are not quoted in this excerpt** (results are said to be deferred to Section III), so the following gaps are *inferred from the described methodology*, not stated by the authors:

- No dosimetric endpoints, no compliance limits, no exposure-ratio computation — nothing here supports non-ionizing-radiation dose evaluation.
- Threshold-based AU (binarized at −72 dBm/20 MHz) discards amplitude information; it is not a duty cycle, time-averaged power, or exposure metric, and lacks the 6-min/30-min averaging required by ICNIRP/FCC.
- Scalar frequency–power logs only (no retained I/Q), so peak/average ratios, modulation, and temporal microstructure are unavailable even though the 5:1 compression is lossless.
- Calibration traceability (antenna factor, LNA gain, cable loss, temperature drift) is asserted but the uncertainty budget is not given here.
- Single fixed-site geometry: no spatial mapping, no body-facing orientation, no worst-case or personal-dose interpretation.
- Frequency weighting/summation across bands and site-to-site comparability (e.g., the Anchorage vs. Louisville "KY/CO" label ambiguity) are not addressed in this excerpt.

**Bottom line:** Cite this work only as evidence about spectrum occupancy/airtime and monitoring infrastructure — not as dosimetry or exposure-compliance evidence.