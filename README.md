# Design-Study-Project---SHG-in-SiN-microring-resonators
Repository for allocating data from the results of the design study project on "Reconfigurable SHG in Silicon Nitride Microrings via Self-Injection Locking and All-Optical Poling: A Design Study.


This repository contains the complete numerical design study of second-harmonic generation (SHG) in silicon nitride (SiN) microring resonators leveraging **All-Optical Poling (AOP)** and **Self-Injection Locking (SIL)** techniques.

The goal is to analyze and model the nonlinear dynamics of AOP-assisted SHG on CMOS-compatible SiN platforms, identify geometrical configurations that maximize conversion efficiency, and critically compare the results against other photonic platforms such as thin-film lithium niobate (TFLN).

## 🔬 Project Structure

### 📁 `BECO_PIC_Report.pdf/` 
Detailed report and analysis of the results.

### 📁 `BECO_PIC_Slides-Presentation.pdf/` 
Slides showing the results of the project.

### 📁 `EMode Codes/`
Scripts for sweeping and extracting modal data from straight waveguides using Lumerical EMode simulations.

- `sweep_data_FH.py` – Extracts effective indices for FH modes
- `sweep_data_SH.py` – Extracts effective indices for SH modes
- `sweep-SiN-SiO2-Rectangular.py` – Automates width sweep for rectangular waveguides
- `sweep-SiN-SiO2-angled.py` – Sweep for trapezoidal waveguide geometries

### 📁 `Results/`
Contains modal results, simulations, and plots categorized by waveguide width.

Example subfolders:
- `900nm - width/` – Includes:
  - Raw CSV files for `FH_modes` and `SH_modes`
  - Field profile images (`SiN_FH_1.png`, `SiN_SH_1.png`)
  - Dispersion curves (`dispersionSiN_1520_1600.png`, etc.)
  - QPM period, phase mismatch, detuning, SHG output power, etc.

Other folders from `600nm` to `1800nm` contain similar structured outputs for each width.

### 📁 Main Analysis Files
- `main_results_sheet.xlsx` – Aggregated modal and nonlinear results for all widths

### Complementary document 

- Detailed extension of the theoretical framework implemented in the project, including details about the SIL and AOP-grating processes and the models used.

## 📈 Key Methodology

1. **Modal Simulations**: EMode sweep in wavelength (1520–1600 nm) for various waveguide widths.
2. **Phase-Matching Analysis**: Computation of $\Delta k$, QPM period, and $\mathrm{sinc}(\Delta k L/2)$.
3. **Hot-Spot Detection**: Minimum detunings for FH/SH double-resonance.
4. **AOP Dynamics**: Rate equation modeling of the induced $\chi^{(2)}_{\mathrm{eff}}$ via photogalvanic effect.
5. **SHG Performance**: Coupled-mode equations simulated in Python for steady-state power transfer.
6. **Fit of $\chi^{(2)}_{\mathrm{eff}}$**: Polynomial (3rd order) fit as a function of waveguide width.

## 🧠 Key Findings

- Maximum $\chi^{(2)}_{\mathrm{eff}} \approx 0.516$ pm/V was found at **900 nm** width, closely matching recent experimental values from Clementi et al. (2025).
- Despite SiN's small nonlinear coefficient compared to TFLN, the compactness and maturity of its photonic integration make it competitive.

## 📚 References

Key sources used in the analysis include:

- Clementi et al., *Light Sci. Appl.*, 2025
- Nitiss et al., *Nat. Photonics*, 2022
- Moss et al., *Nat. Photonics*, 2013
- Boyd, *Nonlinear Optics*, Springer


