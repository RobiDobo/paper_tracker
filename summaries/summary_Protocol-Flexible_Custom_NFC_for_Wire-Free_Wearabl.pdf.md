# Summary for Protocol-Flexible_Custom_NFC_for_Wire-Free_Wearabl.pdf

## Structured Summary

**1. Core Method — What did they do?**

The paper presents a protocol-flexible, software-defined NFC system (13.56 MHz carrier) for wire-free wearable sensor networks, and characterizes its **communication link performance** — polling rate, throughput, and packet error rate (PER) — rather than any dosimetric quantity. The physical layer examined consists of a 400 mm × 260 mm fabric meander coil resonant at 13.44 MHz (L = 1.7 µH, six 495 pF series capacitors, |Z₁₁| = 6.45 Ω, Q = 22.3, −3 dB bandwidth 604 kHz, with ±1 MHz reply sidebands lying outside resonance), interrogated with the reader in contact at 0 and 10.5 mm reader–coil gaps and ~10–20 mm tag–coil air gaps, with the coil conformed to a 228 mm-diameter cylinder. Modulation is 10% ASK, with ~17 mW tag power. Note: no SAR, E/H-field strength, absorbed dose, or ICNIRP/IEEE compliance assessment was performed; the listed parameters are used only to explain link behavior.

**2. Main Conclusions — Key dosimetry results**

- **There are no dosimetry results in this paper.** No SAR, internal/external field values, absorbed dose, or exposure-limit compliance figures are reported, so no safety conclusion can be drawn from it.
- The only exposure-*relevant* (not exposure-*assessed*) information is geometric/electrical: resonance at 13.44 MHz, coil dimensions and conformity to a 228 mm cylinder, and the contact/near-contact reader–coil gaps (0 and 10.5 mm) plus 10–20 mm tag–coil gaps.
- Communication conclusions: static bending preserved the usable link window (minimum PER ≈ 5%, with only a ~6 mm shift at one measurement position), i.e., the link is robust to conformal/static deformation.

**3. Limitations / Future Work — Gaps**

- **No human-exposure or safety evaluation** of any kind (no SAR, no field mapping, no ICNIRP/IEEE 2020/ICNIRP 2020-style compliance check).
- **On-body operation not tested** — measurements were on a cylinder phantom/rig, not a human subject or realistic tissue model.
- **Dynamic deformation not evaluated** — only static bending; motion, stretching, and sweat/motion-induced impedance changes are unaddressed.
- Implied future work: add human/tissue-realistic exposure assessment, dynamic on-body mechanical trials, and safety-limit compliance verification before any claim about RF safety of the wearable link can be made.