# Summary for Analysis_of_Multi-Tone__Multi-Conductor__Spatially.pdf

**Important caveat first:** This paper contains **no dosimetry content whatsoever** — it is a circuit-theory/electromagnetics paper on spatially discrete traveling-wave modulated (SDTWM) loop networks. I have not fabricated dosimetry results; below is what the text actually supports.

## 1. Core Method
- A semi-analytical **"Interpath Relation"** method that reduces an infinite periodic space–time-modulated loop network to a **single unit cell**, using a multi-harmonic ABCD (transmission) matrix plus a delay matrix D_ℓℓ′ = δ_ℓℓ′ e^(−jℓΩt₀).
- **Born–von Karman quantization** of discrete Bloch–Floquet modes (κd₀ = m2π/N, Ωt₀ = p2π/N) for N = 4 cells; example 10 GHz network (C₀ = 0.43 pF, L = 0.23 nH, Z₀ = 131 Ω, M = 0.1, Ω/2π = 2 GHz).
- Multi-tone/multi-conductor extension via harmonic-index-difference mapping to build the Fourier coefficient tensor ĀF (up to q^v harmonics, q = 11), plus an **Analytic Array Scanning** method for spatial Green's functions.
- Validation against **Keysight ADS harmonic balance** (Toshiba 1SV280 varactor), reporting ~18.35× speedup (6.54 s vs 120 s) and complexity O((2uqv)³) vs O((Kqv)³).

## 2. Main Conclusions (dosimetry)
- **None.** No SAR, power density, internal/external field conversion, exposure limits, tissue properties, or dose metrics appear anywhere in the paper (including the reference list).
- The paper's actual conclusions are device-level: ~40 dB gain for a single-tone four-cell parametric amplifier (Ω/2π = 18.94 GHz, M = 0.395); >6 dB VSWR bandwidth improvement for an electrically small antenna (ka = 0.253 at 341 MHz; Rrad = 1.434 Ω); and a 3-port magnetless circulator achieving 186 MHz bandwidth and −0.63 dB insertion loss vs 92.8 MHz / −2.62 dB in [12], with no idler-frequency reflections.

## 3. Limitations / Future Work
- **No dosimetry gaps are mentioned**, because dosimetry is entirely out of scope. The authors' limitations are computational/device-oriented (circuit-level modeling, validation against a specific varactor and harmonic-balance setup).
- For exposure/safety purposes, the reported quantities (radiated power P_rad/P_inc, reflected power, Rrad) could only serve as **inputs** to a dosimetric assessment; converting them into SAR or exposure-metric results would require field-to-dose conversion, tissue properties, and compliance limits that this work does not provide.

**Bottom line:** If your goal is a dosimetry dataset, this source is not usable — you would need the paper's field-/SAR-oriented sections (which do not exist) or a different paper. I'd be happy to summarize the circuit-level contributions in more detail, or help identify papers that actually report SAR/power-deposition results.