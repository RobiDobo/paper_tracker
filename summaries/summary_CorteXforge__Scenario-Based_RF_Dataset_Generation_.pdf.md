# Summary for CorteXforge__Scenario-Based_RF_Dataset_Generation_.pdf

Based on the provided technical details from the paper "CorteXforge: Scenario-Based RF Dataset Generation," here is the structured summary:

### 1. Core Method: What did they do?
* **Framework Development:** The authors introduced **CorteXforge**, a framework designed to translate high-level wireless scenarios into synchronized over-the-air (OTA) software-defined radio (SDR) experiments. This was executed on the SLICES-RI/CorteXlab testbed using USRPs housed in a shielded, partially anechoized room with shared frequency and timing references.
* **Dataset Generation:** The framework automatically generated standardized, annotated datasets following the SigMF format. This resulted in **ModForge**, an OTA modulation dataset containing nearly 3 million (2,970,079) IQ vectors—each with 1024 complex samples—across 24 modulation classes, operating at a 2.45 GHz carrier frequency and a 16.667 MHz sampling rate.
* **Evaluation:** They evaluated automatic modulation classification (AMC) using a convolutional neural network (CNN) trained on synthetic data and tested on the real-world OTA acquisitions from the ModForge dataset to quantify and address the synthetic-to-real performance gap.

### 2. Main Conclusions: What were the key dosimetry results?
* *Note on Scope:* The provided text and the paper's focus are exclusively on RF dataset generation, wireless testbeds, and automatic modulation classification (AMC). **There are no mentions of non-ionizing radiation dosimetry, specific absorption rate (SAR), electromagnetic field absorption, or biological tissue modeling.** 
* **Key Findings (regarding RF Machine Learning):** 
  * Evaluating a CNN model revealed a substantial zero-shot performance drop (accuracy plunging from 61.4% to 23.2%) when moving from synthetic data to real OTA acquisitions, primarily driven by real-world domain shifts such as hardware impairments.
  * Despite this performance gap, pretraining models on synthetic data successfully accelerates domain adaptation when they are subsequently fine-tuned using limited real-world OTA samples.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
* **Domain Shift / Hardware Impairments:** The evaluation highlights a significant synthetic-to-real performance gap caused by real-world environmental factors and hardware imperfections, emphasizing the challenge of deploying models trained purely on synthetic data to realistic RF environments without fine-tuning. 
*(Note: The provided excerpt does not explicitly list broader future work or limitations beyond the identified synthetic-to-real domain shift and the need for limited OTA fine-tuning).*