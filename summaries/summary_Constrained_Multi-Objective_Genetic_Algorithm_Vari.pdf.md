# Summary for Constrained_Multi-Objective_Genetic_Algorithm_Vari.pdf

Note upfront: this paper contains no dosimetry content. The extracted text explicitly confirms the absence of SAR, power density, or exposure compliance metrics. It is an antenna design/optimization study. I've flagged where your question assumes dosimetry results that don't exist, and provided the actual findings instead.

## 1. Core Method

The authors optimized a CSRR-loaded (complementary split-ring resonator) microstrip patch antenna using a weighted-sum scalarized genetic algorithm. Key elements:

- Converted a tri-objective problem (minimizing return loss S₁₁ at 2.4, 3.6, and 5.2 GHz) into a single scalarized fitness function via weighted sum.
- Incorporated elitist preservation (retaining best solutions across generations).
- Applied domain-specific constraint-handling mechanisms.
- Used a MATLAB–CST co-simulation environment for evaluation.

## 2. Main Conclusions

There are no dosimetry results in this paper. The reported outcomes are antenna performance metrics:

- Return loss (S₁₁): −21.56 dB @ 2.4 GHz, −16.60 dB @ 3.6 GHz, −27.69 dB @ 5.2 GHz
- VSWR: consistently below 1.5 at all three target frequencies
- Gain: 1.96 dBi (2.4 GHz), 2.6 dBi (3.6 GHz), 3.99 dBi (5.2 GHz)
- Size reduction: 16.29%
- Convergence/quality vs. other MOGA variants: generational distance ≈ 0.19, inverted generational distance ≈ 0.18, indicating superior convergence and solution diversity relative to the compared multi-objective genetic algorithm variants.

## 3. Limitations / Future Work

The provided details do not include an explicit limitations or future-work statement from the authors — that section was not captured in the extracted text. I cannot summarize gaps the paper may state without inventing them.

If you need this section, I'd need the corresponding excerpt (typically the "Conclusion" or "Future Work" part of the paper). It's also worth clarifying your overall goal: if you're screening literature for RF exposure/dosimetry relevance, this paper would not qualify, since it addresses antenna radiation performance rather than human exposure assessment.