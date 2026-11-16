# Summary for Common-Loss_Parameter-Efficiency_Analysis_of_MLP_a.pdf

Based on the provided technical details from the paper, here is the final structured summary:

### 1. **Core Method**: What did they do?
The study investigated and compared Multi-Layer Perceptrons (MLPs) and Kolmogorov–Arnold Networks (KANs) acting as neural receivers for classical Nyquist-rate BPSK over Additive White Gaussian Noise (AWGN) channels. The authors conducted a common-loss parameter-efficiency analysis evaluating the models based on Mean Squared Error (MSE), Bit Error Rate (BER), and the total count of trainable parameters. They utilized a synthetically generated dataset of 4 million total samples across multiple SNR levels ($7, 8, 9,$ and $10$ dB), split into training ($3.2 \times 10^6$), validation ($4 \times 10^5$), and test ($4 \times 10^5$) sets.

### 2. **Main Conclusions**: What were the key dosimetry results?
*Note: As noted in the provided text, the study focuses strictly on machine learning architectures (MLPs and KANs) for communication receivers rather than non-ionizing radiation dosimetry, electromagnetic field exposure, or Specific Absorption Rate (SAR). Therefore, there are no dosimetry results to report.* 

Regarding communication performance, the KAN receiver achieved a test BER of $2.45 \times 10^{-4}$ using 3,281 trainable parameters, while the baseline MLP achieved a comparable test BER of $2.50 \times 10^{-4}$ requiring 8,513 parameters. This demonstrates that the KAN architecture can reach a similar operational performance region while utilizing approximately 61.5% fewer parameters than the MLP.

### 3. **Limitations / Future Work**: What are the gaps mentioned by the authors?
*(Note: The provided text snippet does not explicitly list the limitations or future work gaps mentioned by the authors beyond the scope of testing KANs versus MLPs for AWGN communication receivers.)*