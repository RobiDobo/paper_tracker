# Summary for Bao__Automatic_Region_Placement_and_Memory_Allocat.pdf

Based on the provided text, here is the structured summary focusing on the energy modeling, budgeting, and optimization framework of Bao:

### 1. Core Method
* **MILP-Based Compilation Pipeline:** Bao introduces a compilation framework that jointly optimizes region-boundary placement and memory allocation for intermittent computing. It formulates the problem as a Mixed-Integer Linear Program (MILP), solved using Gurobi.
* **Energy Cost Semantics & Budgeting:** The system enforces strict per-region energy budget constraints ($E_{\text{budget}}$) derived from specific capacitor sizes (5 µF, 10 µF, and 50 µF) to guarantee safe execution under intermittent power. 
* **Instruction-Level Modeling:** It profiles basic blocks on an MSP430 architecture using an Otii Ace Pro, modeling execution costs, prologue/epilogue overheads, and variable save/restore costs (parameterized by byte reads/writes $\delta_r, \delta_w$) as linear expressions of MILP decision variables weighted by execution frequencies.

### 2. Main Conclusions (Energy/Dosimetry-equivalent Metrics)
* **Performance Improvements:** Evaluated across 13 benchmarks and three capacitor sizes, Bao achieves a **10% reduction in execution time** and **52% fewer boundary hits** compared to prior heuristic-based baselines (such as RockClimb and Schematic).
* **Model Accuracy:** Dosimetry/energy validation on synthetic microbenchmarks demonstrated a high-fidelity energy model with a **mean absolute error of just 0.62%** (primarily driven by data-switching effects between consecutive instructions).

### 3. Limitations / Future Work
*(Note: The provided text focuses strictly on the technical implementation, evaluation, and artifact reproducibility of the Bao framework, without explicitly outlining broader limitations or future work avenues.)*