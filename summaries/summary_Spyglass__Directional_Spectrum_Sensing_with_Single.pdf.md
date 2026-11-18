# Summary for Spyglass__Directional_Spectrum_Sensing_with_Single.pdf

## Structured Summary

**Important caveat:** The extracted content contains **no dosimetry material whatsoever**. The paper is an RF-sensing/localization work, not a radiation-safety or exposure-assessment study. The summary below reflects what is actually present, and flags where the requested categories cannot be filled.

---

### 1. Core Method — What did they do?

They built **Spyglass**, a low-cost, protocol-agnostic directional spectrum sensing system:

- **Hardware:** USRP B210 SDR + PE42582 SP8T RF switch driving a switched antenna array (8 elements), operating at 2.4–2.6 GHz and 5 GHz. Switching synthesizes a *virtual* array from a single RF chain.
- **Searchlite (detection):** protocol-agnostic signal detection using half-overlap STFT energy detection with sub-matrix extraction to isolate concurrent transmissions.
- **SSFP (AoA):** Switch-Synchronous Fourier Processing — a switch-synchronous partial ISTFT that recovers per-antenna virtual-array streams from the single merged I/Q capture, so the switch timing is compensated rather than treated as an impairment.
- **Estimation:** Maximum-Likelihood Estimation (MLE) over the reference and switched I/Q streams yields single-shot Angle of Arrival, without averaging, waveform knowledge, or multiple receivers.
- **Evaluation:** Azimuth/elevation AoA accuracy, multi-device separation, scalability with antenna count, switching-rate sweeps, and a multipath prevalence study using the DLOC CSI dataset.

### 2. Main Conclusions — key *dosimetry* results

**None exist.** The excerpts explicitly state that no SAR, power-density, exposure, absorbed-dose, or compliance metrics are reported, and that no dosimetric methods or data appear in any section, including the references.

For completeness, the actual reported results are RF-sensing metrics:
- **Median azimuth AoA error 1.4°** (90th percentile 3.3°) with 8 antennas; ~2° median in the multi-device azimuth case.
- **Elevation** is hard: 17° median error with 4 antennas, resolved with 8 antennas (multipath-limited).
- Graceful degradation with fewer antennas; wider error spread at faster switching times.
- Demonstrated separation of simultaneous transmitters in unconstrained RF environments.

### 3. Limitations / Future Work — gaps mentioned by the authors

No author-stated limitations or future-work section was captured in the provided excerpts, so nothing can be quoted here without fabrication. What the excerpts *do* support as observed limitations:

- Elevation estimation degrades under multipath and needs more elements (4 → 8 antennas).
- Faster switch timing broadens the AoA error distribution.
- Fewer antennas reduce accuracy (though gracefully).

**Reasonable inferences (not verbatim author statements):** multipath robustness in real deployments, dependence on switch calibration/timing fidelity, and bandwidth/array-size scaling. If you need the paper's own "limitations/future work" text, please supply that section — it was not included in the extraction.

**Bottom line:** this source cannot support any dosimetry, SAR, or exposure-limit claim, and should not be cited as evidence in a dosimetric context.