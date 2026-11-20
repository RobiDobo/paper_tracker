# Summary for Energy_Aware_Optimization_of_Non-Deterministic_Tas.pdf

Based on the extracted technical details from the paper, here is the structured summary:

1. **Core Method**: 
   The authors developed **Thimble**, an energy storage optimization system for intermittent computing nodes. Thimble dynamically maps tasks to a fixed set of capacitors (1.0–6.8 mF E6 series) based on runtime workload forecasts. It models task-based workloads using a **Markov chain**, employs a **binary linear program** to balance energy demands against capacitor leakage currents, and uses a **two-part energy certificate** to ensure task feasibility across stochastic execution paths. It also incorporates "depth replanning," which triggers task-to-capacitor remapping based on energy forecast uncertainty (threshold $\sigma_{max}$).

2. **Main Conclusions**: 
   *Note: As noted in the text, the paper does not contain information regarding non-ionizing radiation dosimetry, as it focuses on energy-aware optimization for battery-free embedded systems.* 
   Regarding system performance, Thimble improves inference throughput by **22–42%** compared to static mapping (LEACS) and maintains continuous system operation even when deployment conditions deviate from training data. Furthermore, runtime replanning improves throughput by up to **7%** in energy-starved conditions compared to static, non-adaptive strategies (though static planning remains effective in energy-dense scenarios).

3. **Limitations / Future Work**: 
   While the provided text highlights the system's resilience and adaptability under varying energy harvesting conditions (evaluated via PySpice and ngspice using simplified MOSFET models and power-scaling heuristics), specific limitations, boundary conditions, or avenues for future work were not explicitly detailed in the extracted excerpt beyond relying on training data distributions and managing forecast uncertainty ($\sigma_{max}$).