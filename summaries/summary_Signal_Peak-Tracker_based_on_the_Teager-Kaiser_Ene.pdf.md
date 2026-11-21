# Summary for Signal_Peak-Tracker_based_on_the_Teager-Kaiser_Ene.pdf

Based on the technical details provided from the paper, here is the structured summary:

1. **Core Method**: 
   The authors modified the traditional Teager-Kaiser Energy (TKE) operator to create a normalized peak-detector called the Teager-Kaiser-Peak (TKP) operator. This was achieved by using the numerical integration of a simple harmonic oscillator through discrete-time formulations and spreadsheet-based simulations (employing the Euler algorithm with specific damping and sampling parameters) to successfully track signal amplitudes and peak values.

2. **Main Conclusions**: 
   The results demonstrate that the TKP operator is successful in predicting peak displacements and tracking time-varying amplitudes. *(Note: While the prompt mentions "dosimetry," the provided technical details focus entirely on signal processing, amplitude tracking, and peak detection rather than radiation dosimetry).*

3. **Limitations / Future Work**: 
   The primary limitation noted is the occurrence of anomalies at sharp transition points in the signal, which require explicit filtering to ensure proper functioning of the TKP operator.