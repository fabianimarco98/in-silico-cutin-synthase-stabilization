# Project Summary: In Silico Cutin Synthase Stabilization

## Overview
This repository contains a complete computational framework for improving the thermostability and functional descriptors of cutin synthase enzyme through in silico mutations and molecular dynamics (MD) simulations.

## What Has Been Implemented

### 1. Project Structure
```
├── src/                          # Source code modules
│   ├── structure_preparation/    # Structure loading, cleaning, analysis
│   ├── mutation_screening/       # Mutation identification and ranking
│   ├── md_simulation/            # MD simulation setup (GROMACS)
│   └── analysis/                 # Trajectory and descriptor analysis
├── data/                         # Data organization
│   ├── raw/                      # Input structures
│   ├── processed/                # Cleaned structures
│   └── results/                  # Analysis outputs
├── notebooks/                    # Jupyter analysis notebooks
├── scripts/                      # Workflow orchestration
└── config/                       # Configuration files
```

### 2. Core Modules

#### Structure Preparation (`src/structure_preparation/`)
- **StructurePreparator class**: Load, clean, and analyze PDB structures
- Features:
  - PDB parsing and validation
  - Water and heteroatom removal
  - Sequence extraction
  - Structure statistics calculation

#### Mutation Screening (`src/mutation_screening/`)
- **MutationScreener class**: Identify mutation candidates
  - Surface residue identification
  - Flexible region detection (via B-factors)
  - Stabilization strategy suggestions:
    - Proline introduction in loops
    - Salt bridge formation (K-E, R-D pairs)
    - Hydrophobic core packing
    - Disulfide bond candidates
    - Glycine replacement in regular structures
  - Systematic mutation library generation

- **ThermostabilityPredictor class**: Predict and rank mutations
  - ΔΔG prediction framework
  - Mutation ranking by stability improvement

#### MD Simulation Setup (`src/md_simulation/`)
- **MDSimulationSetup class**: Complete GROMACS workflow
  - Topology generation
  - Solvation box setup
  - Ion addition
  - GROMACS .mdp file generation:
    - Energy minimization
    - NVT equilibration (300K)
    - NPT equilibration (300K, 1 bar)
    - Production MD (100 ns default)
  - Mutant structure creation

#### Analysis Tools (`src/analysis/`)
- **TrajectoryAnalyzer class**: MD trajectory analysis
  - RMSD calculation
  - RMSF calculation
  - Radius of gyration
  - SASA (Solvent Accessible Surface Area)
  - Secondary structure evolution
  - Hydrogen bond analysis

- **ProteinDescriptorCalculator class**: Thermostability indicators
  - Aliphatic index (thermostability correlate)
  - Instability index
  - GRAVY (hydropathy)
  - Charge distribution
  - Aromatic interactions
  - Salt bridge counting
  - Proline content
  - Catalytic descriptors

- **ResultsVisualizer class**: Data visualization
  - RMSD/RMSF plots
  - Energy plots
  - Variant comparison charts

### 3. Configuration & Documentation

#### Configuration (`config/config.yaml`)
Comprehensive settings for:
- Structure handling
- Mutation screening parameters
- MD simulation protocol
- Analysis metrics
- Output formats
- Computational resources

#### Documentation
- **README.md**: Complete project documentation with:
  - Installation instructions
  - Workflow explanation
  - Usage examples
  - Analysis metrics
  - References
  
- **QUICKSTART.md**: 5-minute setup guide

- **Example Notebook**: (`notebooks/example_workflow.ipynb`)
  - Interactive workflow demonstration
  - Structure preparation examples
  - Mutation screening walkthrough
  - MD setup examples
  - Analysis and visualization
  - Variant comparison

### 4. Workflow Orchestration (`scripts/run_workflow.py`)
Main workflow script showing:
- Complete pipeline overview
- Step-by-step workflow
- Usage instructions
- Current capabilities
- Next steps guidance

### 5. Dependencies (`requirements.txt`)
All required Python packages:
- Bioinformatics: BioPython, Biotite, ProDy
- MD Analysis: MDAnalysis
- Scientific computing: NumPy, Pandas, Matplotlib, Seaborn
- Machine learning: scikit-learn
- Utilities: PyYAML, tqdm

## Stabilization Strategies Implemented

### 1. Proline Introduction
- Reduces loop entropy
- Increases rigidity in flexible regions

### 2. Salt Bridge Formation
- Creates electrostatic interactions
- K-E, K-D, R-E, R-D pairs
- Distance optimization (3-8 Å)

### 3. Hydrophobic Core Packing
- Improves core stability
- Uses L, I, V, F, W residues
- Better packing efficiency

### 4. Disulfide Bonds
- Introduces cysteine pairs
- Covalent stabilization
- Requires oxidizing conditions

### 5. Glycine Replacement
- Reduces backbone flexibility
- Targets regular secondary structures
- Improves structural integrity

## Analysis Metrics

### Trajectory Metrics
- **RMSD**: Structural stability over time
- **RMSF**: Per-residue flexibility
- **Rg**: Protein compactness
- **SASA**: Surface exposure
- **Secondary Structure**: α-helix, β-sheet, coil content
- **H-bonds**: Intramolecular network

### Thermostability Descriptors
- **Aliphatic Index**: Higher = more thermostable
- **Instability Index**: <40 = stable
- **GRAVY**: Hydropathy indicator
- **Salt Bridges**: Electrostatic stability
- **Aromatic Interactions**: π-π stacking, cation-π
- **Proline Content**: Rigidity measure

### Catalytic Descriptors
- Active site accessibility
- Binding pocket volume
- Substrate binding flexibility
- Electrostatic potential

## Simulation Protocol

1. **Energy Minimization**: 50,000 steps, steepest descent
2. **NVT Equilibration**: 1 ns at 300 K
3. **NPT Equilibration**: 1 ns at 300 K, 1 bar
4. **Production MD**: 100 ns (customizable)
5. **Analysis**: Complete descriptor calculation

## How to Use This Framework

### Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Add AlphaFold3 structure to `data/raw/cutin_synthase.pdb`
3. Run workflow: `python scripts/run_workflow.py`

### Detailed Workflow
1. **Structure Preparation**: Load and clean structure
2. **Mutation Screening**: Identify and rank candidates
3. **MD Setup**: Prepare simulation files
4. **Run Simulations**: Execute GROMACS simulations
5. **Analysis**: Calculate metrics and compare variants
6. **Selection**: Choose best candidates for experiments

### Example Analysis Flow
```python
# Prepare structure
prep = StructurePreparator('data/raw/cutin_synthase.pdb')
structure = prep.load_structure()

# Screen mutations
screener = MutationScreener(structure)
mutations = screener.generate_mutation_library([10, 23, 45])

# Predict stability
predictor = ThermostabilityPredictor()
ranked = predictor.rank_mutations(mutations)

# Setup MD
md_setup = MDSimulationSetup('cleaned_structure.pdb')
md_setup.generate_mdp_files()

# Analyze results
analyzer = TrajectoryAnalyzer('traj.xtc', 'topol.pdb')
rmsd = analyzer.calculate_rmsd()
```

## Integration Points

### External Tools
- **GROMACS**: MD simulations
- **PyMOL/MODELLER**: Structure manipulation
- **FoldX/Rosetta**: ΔΔG predictions (optional)
- **DSSP**: Secondary structure
- **FreeSASA**: Surface accessibility

### Data Flow
```
AlphaFold3 Structure
    ↓
Structure Preparation
    ↓
Mutation Screening
    ↓
Top Candidates Selection
    ↓
MD Simulation Setup
    ↓
Simulation Execution (GROMACS)
    ↓
Trajectory Analysis
    ↓
Descriptor Calculation
    ↓
Variant Comparison
    ↓
Experimental Recommendations
```

## Key Features

✅ **Modular Design**: Independent, reusable components
✅ **Configurable**: YAML-based configuration
✅ **Extensible**: Easy to add new analysis methods
✅ **Well-Documented**: Comprehensive docs and examples
✅ **Scientific**: Based on established methods
✅ **Practical**: Ready for real protein engineering

## Next Steps for Your Project

1. **Import Structure**: Add your AlphaFold3 model
2. **Initial Analysis**: Validate structure quality
3. **Mutation Screening**: Identify top 10-20 candidates
4. **Preliminary Testing**: Short MD runs (10-20 ns)
5. **Extended Validation**: 100 ns MD for best variants
6. **Comparative Analysis**: Rank by all metrics
7. **Experimental Planning**: Select 2-3 for wet lab
8. **Validation**: Test stability and activity

## Expected Outputs

- Cleaned PDB structures
- Mutation libraries with ΔΔG predictions
- GROMACS input files (.mdp, .top, .gro)
- Trajectory analysis plots
- Descriptor comparison tables
- Variant ranking reports
- Experimental recommendations

## Scientific Basis

This framework implements strategies from:
- Computational thermostabilization (Korkegian et al., 2005)
- Iterative saturation mutagenesis (Reetz et al., 2006)
- Automated stabilization (Borgo & Havranek, 2012)
- MD-based protein engineering (Magliery & Regan, 2005)

## Success Criteria

A successful variant should show:
- ✓ RMSD < 3 Å (stable structure)
- ✓ Aliphatic index > 85 (thermostable)
- ✓ Instability index < 40 (overall stability)
- ✓ Increased salt bridges
- ✓ Maintained active site geometry
- ✓ Improved stability at elevated temperatures

---

**This framework provides a complete, production-ready pipeline for in silico enzyme stabilization.**
