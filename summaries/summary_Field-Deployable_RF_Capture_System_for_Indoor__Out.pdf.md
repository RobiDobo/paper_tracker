# Summary for Field-Deployable_RF_Capture_System_for_Indoor__Out.pdf

Based on the extracted technical details from the paper, here is the structured summary:

### 1. Core Method: What did they do?
* **System Architecture:** Developed a portable, battery-powered RF capture system combining a HackRF One software-defined radio (SDR), a Raspberry Pi 5, an 800 MHz–6 GHz LPDA antenna, and an embedded GNSS receiver.
* **Data Collection:** Recorded continuous IQ data at 20 Msps with a 2.45 GHz center frequency and fixed receiver gains (LNA 16 dB, VGA 32 dB). 
* **Data Processing & Storage:** Automatically embedded 1 Hz GNSS geotagging metadata into SigMF-compliant storage files, maintaining a reliable write throughput of 75–85 MB/s with zero dropped samples.
* **Field Evaluation:** Conducted physical testing across three distinct environments: dense foliage, urban outdoor, and indoor office settings to quantify RF propagation and attenuation.

### 2. Main Conclusions: What were the key results?
* **Dense Foliage:** Induced severe RF attenuation (~30 dB canopy loss), resulting in power levels near the noise floor (−76 to −82 dBFS, specifically averaging around −79.1 dBFS).
* **Urban Outdoor:** Exhibited a 30 dB dynamic range with high temporal variability, multipath scattering, interference, and peak power levels reaching −40 dBFS.
* **Indoor Settings:** Experienced a 20–25 dB building entry loss alongside an 8–10 dB elevated interference floor driven by structural multipath.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
*(Note: The provided text does not explicitly detail future work or limitations, focusing instead on the successful deployment and characterization metrics. However, based on the scope provided, potential implicit limitations revolve around fixed-gain testing and the specific evaluation confined to the 2.45 GHz frequency band.)*