# In Silico Cutin Synthase Stabilization

Thermostability and enzyme descriptor improvement of cutin synthase using computational tools and molecular dynamics simulations.

## 🧬 Project Overview

This project aims to improve the thermostability and other functional descriptors of cutin synthase enzyme through in silico mutations and molecular dynamics (MD) simulations. The work builds upon an AlphaFold3-predicted structure and implements a systematic computational pipeline for protein engineering.

### Key Objectives
- Increase thermostability of cutin synthase enzyme
- Maintain or improve catalytic activity
- Identify stabilizing mutations through computational screening
- Validate mutations through MD simulations
- Provide recommendations for experimental validation

## 📁 Project Structure

```
├── src/                          # Source code modules
│   ├── structure_preparation/    # Structure loading and cleaning
│   ├── mutation_screening/       # Mutation identification and screening
│   ├── md_simulation/            # MD simulation setup
│   └── analysis/                 # Trajectory and descriptor analysis
├── data/                         # Data directory
│   ├── raw/                      # Raw input structures (AlphaFold3 models)
│   ├── processed/                # Cleaned and prepared structures
│   └── results/                  # Analysis results and outputs
├── notebooks/                    # Jupyter notebooks for analysis
├── scripts/                      # Workflow execution scripts
├── config/                       # Configuration files
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

1. **Python 3.8+** with pip
2. **GROMACS** (for MD simulations) - [Installation guide](http://www.gromacs.org/)
3. **Optional tools:**
   - PyMOL or MODELLER (structure manipulation)
   - FoldX or Rosetta (ΔΔG predictions)
   - DSSP (secondary structure analysis)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/fabianimarco98/in-silico-cutin-synthase-stabilization.git
cd in-silico-cutin-synthase-stabilization
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Verify installation:
```bash
python scripts/run_workflow.py
```

## 📊 Workflow

### 1. Structure Preparation
```python
from src.structure_preparation.prepare_structure import StructurePreparator

# Load and clean AlphaFold3 structure
prep = StructurePreparator('data/raw/cutin_synthase.pdb')
prep.load_structure()
prep.clean_structure('data/processed/cutin_synthase_clean.pdb')
stats = prep.analyze_structure()
```

### 2. Mutation Screening

The project implements several stabilization strategies:

- **Proline Introduction**: Reduce loop entropy
- **Salt Bridge Formation**: Create K-E, K-D, R-E, R-D pairs
- **Hydrophobic Core Packing**: Optimize core residues (L, I, V, F, W)
- **Disulfide Bonds**: Introduce cysteine pairs (3-8 Å apart)
- **Glycine Replacement**: Replace flexible glycines in regular structures

```python
from src.mutation_screening.mutation_screener import MutationScreener, ThermostabilityPredictor

# Screen for beneficial mutations
screener = MutationScreener(structure)
flexible_regions = screener.identify_flexible_regions()
strategies = screener.suggest_stabilizing_mutations()

# Predict stability changes
predictor = ThermostabilityPredictor()
mutations = screener.generate_mutation_library(positions=[10, 23, 45])
ranked = predictor.rank_mutations(mutations)
```

### 3. MD Simulation Setup

```python
from src.md_simulation.setup_md import MDSimulationSetup

# Setup MD simulation
md_setup = MDSimulationSetup('data/processed/cutin_synthase_clean.pdb')
md_setup.generate_topology()
md_setup.setup_solvation()
md_setup.add_ions(concentration=0.15)
mdp_files = md_setup.generate_mdp_files()
```

**Simulation Protocol:**
1. Energy minimization (50,000 steps)
2. NVT equilibration (1 ns at 300 K)
3. NPT equilibration (1 ns at 300 K, 1 bar)
4. Production MD (100 ns)

### 4. Trajectory Analysis

```python
from src.analysis.analyze_results import TrajectoryAnalyzer, ProteinDescriptorCalculator

# Analyze MD trajectory
analyzer = TrajectoryAnalyzer('trajectory.xtc', 'topology.pdb')
rmsd = analyzer.calculate_rmsd()
rmsf = analyzer.calculate_rmsf()
rg = analyzer.calculate_radius_of_gyration()

# Calculate thermostability descriptors
calc = ProteinDescriptorCalculator(structure)
descriptors = calc.calculate_thermostability_indicators()
```

### 5. Complete Workflow

```bash
# Run the complete workflow
python scripts/run_workflow.py --step all

# Or run individual steps
python scripts/run_workflow.py --step prepare
python scripts/run_workflow.py --step screen
python scripts/run_workflow.py --step simulate
python scripts/run_workflow.py --step analyze
```

## 📈 Analysis Metrics

### Trajectory Metrics
- **RMSD**: Root Mean Square Deviation (structural stability)
- **RMSF**: Root Mean Square Fluctuation (residue flexibility)
- **Rg**: Radius of gyration (compactness)
- **SASA**: Solvent Accessible Surface Area
- **Secondary Structure**: Helix, sheet, coil content evolution
- **Hydrogen Bonds**: Intramolecular H-bond network

### Thermostability Descriptors
- **Aliphatic Index**: Correlates with thermostability
- **Instability Index**: Values > 40 indicate unstable proteins
- **GRAVY**: Grand Average of Hydropathy
- **Charge Distribution**: Positive/negative residue analysis
- **Aromatic Interactions**: π-π stacking, cation-π
- **Salt Bridges**: Electrostatic stabilization
- **Proline Content**: Rigidity indicator

### Catalytic Descriptors
- Active site accessibility
- Binding pocket volume
- Substrate binding flexibility
- Electrostatic potential

## 🔧 Configuration

Edit `config/config.yaml` to customize:
- Force fields and water models
- Simulation parameters (temperature, time, etc.)
- Analysis metrics and thresholds
- Mutation screening strategies

## 📝 Results

Results are saved to `data/results/`:
- **Figures**: Plots and visualizations
- **Reports**: Markdown/HTML/PDF summaries
- **Data**: CSV files with metrics and descriptors

## 🔬 Recommended Workflow

1. **Import Structure**: Place AlphaFold3 structure in `data/raw/`
2. **Structure Analysis**: Validate quality and identify flexible regions
3. **Mutation Screening**: Generate and rank mutation candidates
4. **Preliminary Testing**: Test top 5-10 mutations with short MD (10-20 ns)
5. **Extended Validation**: Run 100 ns MD for promising candidates
6. **Comparative Analysis**: Compare WT vs mutants across all descriptors
7. **Experimental Planning**: Select 2-3 best variants for lab validation

## 🤝 Contributing

This project is part of a Master's thesis on cutin synthase engineering. Suggestions and improvements are welcome!

## 📚 References

### Key Methods
- **AlphaFold3**: Structure prediction
- **GROMACS**: Molecular dynamics simulations
- **MDAnalysis**: Trajectory analysis
- **BioPython**: Structural bioinformatics

### Stabilization Strategies
1. Korkegian et al. (2005) - "Computational thermostabilization of an enzyme"
2. Reetz et al. (2006) - "Iterative saturation mutagenesis (ISM)"
3. Borgo & Havranek (2012) - "Automated selection of stabilizing mutations"

## 📧 Contact

For questions or collaboration:
- GitHub: [@fabianimarco98](https://github.com/fabianimarco98)

## 📄 License

This project is available for academic and research purposes.

---

**Note**: This is a computational framework. Actual MD simulations require appropriate computational resources (HPC cluster recommended for production runs). External tools (GROMACS, PyMOL, etc.) must be installed separately.
