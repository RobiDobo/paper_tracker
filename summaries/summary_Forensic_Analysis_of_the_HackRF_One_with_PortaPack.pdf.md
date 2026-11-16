# Summary for Forensic_Analysis_of_the_HackRF_One_with_PortaPack.pdf

Based on the provided extracted technical details from the paper "Forensic_Analysis_of_the_HackRF_One_with_PortaPack.pdf", here is the structured summary:

### 1. Core Method: What did they do?
* **Digital Forensics & Data Recovery:** Conducted FAT32 file system forensics on the device's microSD card, analyzing cluster allocation ordering, unallocated cluster ranges, and timeline reconstruction across multiple operating systems to recover deleted or discarded files (such as 16-bit IQ sample [C16] capture files and data lost during "IQ Trim" operations).
* **RF Signal Analysis & Processing:** Processed I/Q recordings using envelope analysis (with 20 µs and 50 µs moving averages), Welch power spectral density (PSD) estimation (using a 4,096-point Hann window), and spectrogram generation.
* **Demodulation & Decoding:** Demodulated On-Off Keying (OOK) signals by thresholding envelope segments into on/off durations to extract bit sequences and frame structures (preamble, data, repeat, and release frames, such as Manchester-coded signals from rolling-code remotes near 433.92 MHz). Validation was performed by cross-comparing outputs against independent decoders like `rtl_433`.

### 2. Main Conclusions: What were the key dosimetry results?
* **Non-Ionizing Radiation Dosimetry:** **None.** The provided text explicitly notes that the paper contains no technical methods, data, or results related to non-ionizing radiation dosimetry, as the research focuses strictly on digital forensics, software-defined radio (SDR) artifacts, file recovery, and signal demodulation.

### 3. Limitations / Future Work: What are the gaps mentioned by the authors?
* *Note: The provided extracted text snippets do not contain specific statements detailing limitations or future work regarding the research.*