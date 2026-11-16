# Summary for Zero-Knowledge_Remote_Adversarial_Attack_against_W.pdf

Based on the provided technical details from the paper "Zero-Knowledge_Remote_Adversarial_Attack_against_W.pdf", here is the final structured summary:

### 1. Core Method: What did they do?
* **Adversarial Framework (GRAW):** Developed a zero-knowledge remote adversarial attack framework targeting Wi-Fi-based Human Activity Recognition (HAR) systems. It utilizes Generative Adversarial Imitation Learning (GAIL) and Trust Region Policy Optimization (TRPO) to generate adversarial perturbation signals.
* **Signal Manipulation & Channel Reciprocity:** Leveraged Wi-Fi Time-Division Duplexing (TDD) channel reciprocity to align router-estimated Channel State Information (CSI) with HAR device observations. 
* **Update Mechanisms & Constraints:** Operated at online perturbation update rates up to 50 Hz (within commodity NIC limits of up to 1 kHz) and updated perturbations within the channel coherence time (~20 ms for 5 GHz Wi-Fi at 1.5 m/s movement).
* **Multi-Antenna Handling:** Implemented a multi-antenna manipulation scheme that projects online perturbations onto a feasible subspace to satisfy shared Long Training Field (LTF) amplitude constraints independently per transmitter antenna across SIMO and MIMO settings.

### 2. Main Conclusions: What were the key dosimetry results?
* **Absence of Dosimetry Metrics:** The provided text explicitly notes **no mention** of non-ionizing radiation dosimetry, specific absorption rate (SAR) metrics, specific RF exposure limits, or biological tissue interactions. 
* **Signal/Performance Metrics:** Instead of dosimetry, evaluation focused on the **Perturbation-to-Signal Ratio (PSR)** and **Attack Success Ratio (ASR)**. Results demonstrate that GRAW achieves a high ASR at low PSR levels across 2.4 GHz and 5 GHz bands, successfully degrading target classifier accuracy. Furthermore, multi-antenna LTF manipulation achieved an ASR comparable to an ideal LTF-oracle with a minimal PSR difference (< 1.9 dB for 50% ASR).
* **Computational & Energy Efficiency:** The framework requires 2.2 × 10⁵ FLOPs per LTF update, translating to an estimated power consumption of 0.067 mW on GPUs and 0.1 W on CPUs (< 1% of total capacity), with a total system power consumption of 11 mW and a memory footprint of 0.7–1.3 MB.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
*(Note: The provided text excerpts focus strictly on operational, computational, and algorithmic mechanics rather than explicitly listing formal "Limitations / Future Work" sections. However, the constraints and operational boundaries mentioned in the text implicitly highlight the following system limitations:)*
* **Coherence Time Constraints:** Perturbations must be updated strictly within the channel coherence time (~20 ms for 5 GHz Wi-Fi under 1.5 m/s human movement) to remain effective under dynamic channel conditions.
* **LTF Amplitude Constraints:** Perturbation injection is bounded by strict target amplitude thresholds relative to the Long Training Field (LTF) to maintain stealthiness, requiring subspace projection techniques for multi-antenna receivers ($N_{\text{RX}} > 1$).
* **Absence of Biological/Regulatory Evaluation:** The text lacks any evaluation or integration regarding safety limits, tissue exposure, SAR, or non-ionizing radiation compliance, which represents a complete gap regarding real-world physical deployment safety standards in the provided data.