# Computational Redesign of Cutinase for Enhanced Thermostability

This repository documents the *in silico* workflow to improve the thermostability of a cutinase enzyme, starting from a structure predicted by AlphaFold3. The goal is to identify key point mutations for future experimental validation, building upon work from a Master's thesis project.

## 🎯 Project Goal

To computationally identify and validate single-point mutations that increase the thermal stability of cutinase without compromising its function.

## 🔬 Workflow

The project follows a standard computational protein design pipeline:

1.  **Model Preparation:** The initial AlphaFold3 structure is validated, cleaned, and energy-minimized.
2.  **Stability Prediction:** All possible mutations are screened using **FoldX** and **Rosetta** to predict their effect on folding free energy (ΔΔG).
3.  **MD Simulation:** The most promising mutants and the wild-type (WT) are simulated at high temperatures using **GROMACS** to test their structural stability.
4.  **Analysis:** Trajectories are analyzed (RMSD, RMSF) to compare the mutants against the WT and rank the best candidates.

## 🛠️ Key Tools

* **Modeling:** AlphaFold3, PyMOL
* **Prediction:** FoldX, Rosetta
* **Simulation:** GROMACS
* **Analysis:** VMD, Matplotlib

## 📂 Repository Structure
