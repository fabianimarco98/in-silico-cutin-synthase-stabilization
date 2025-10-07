# Quick Start Guide

## Cutin Synthase Stabilization Project

### 🎯 Quick Setup (5 minutes)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify installation:**
   ```bash
   python scripts/run_workflow.py
   ```

3. **Add your structure:**
   - Place your AlphaFold3 PDB file in: `data/raw/cutin_synthase.pdb`

### 🚀 Quick Test Run

```python
# Test structure preparation
python -c "from src.structure_preparation.prepare_structure import StructurePreparator; StructurePreparator('.').main()"

# Test mutation screening
python -c "from src.mutation_screening.mutation_screener import MutationScreener; MutationScreener().main()"

# Test MD setup
python -c "from src.md_simulation.setup_md import MDSimulationSetup; MDSimulationSetup('.').main()"

# Test analysis tools
python -c "from src.analysis.analyze_results import TrajectoryAnalyzer; TrajectoryAnalyzer().main()"
```

### 📊 Example Usage

```python
from src.structure_preparation.prepare_structure import StructurePreparator
from src.mutation_screening.mutation_screener import MutationScreener, ThermostabilityPredictor

# 1. Prepare structure
prep = StructurePreparator('data/raw/cutin_synthase.pdb')
structure = prep.load_structure()
stats = prep.analyze_structure()

# 2. Screen mutations
screener = MutationScreener(structure)
flexible = screener.identify_flexible_regions()
mutations = screener.generate_mutation_library([10, 23, 45])

# 3. Predict stability
predictor = ThermostabilityPredictor()
ranked = predictor.rank_mutations(mutations[:10])

# 4. Check top candidates
for mut in ranked[:5]:
    print(f"{mut['mutation']}: ΔΔG = {mut['ddg']:.2f} kcal/mol")
```

### 📚 Learn More

- **Full documentation**: See `README.md`
- **Example notebook**: Open `notebooks/example_workflow.ipynb`
- **Configuration**: Edit `config/config.yaml`

### 🔧 Required External Tools

For full functionality, install:
- **GROMACS**: Molecular dynamics - http://www.gromacs.org/
- **PyMOL** (optional): Structure visualization - https://pymol.org/
- **DSSP** (optional): Secondary structure - https://swift.cmbi.umcn.nl/gv/dssp/

### ⚡ Common Tasks

**Generate mutation library:**
```bash
python -c "
from src.mutation_screening.mutation_screener import MutationScreener
screener = MutationScreener()
strategies = screener.suggest_stabilizing_mutations()
print(strategies)
"
```

**Setup MD simulation:**
```bash
python -c "
from src.md_simulation.setup_md import MDSimulationSetup
md = MDSimulationSetup('data/processed/cutin_synthase_clean.pdb')
mdp_files = md.generate_mdp_files('.')
"
```

**Analyze trajectory:**
```bash
python -c "
from src.analysis.analyze_results import TrajectoryAnalyzer
analyzer = TrajectoryAnalyzer()
rmsd = analyzer.calculate_rmsd()
"
```

### 🆘 Troubleshooting

**Import errors:**
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

**Missing dependencies:**
```bash
pip install --upgrade -r requirements.txt
```

**GROMACS not found:**
- Ensure GROMACS is in your PATH
- Test with: `gmx --version`

### 📝 Next Steps

1. Place your structure in `data/raw/`
2. Run structure preparation
3. Screen for mutations
4. Setup and run MD simulations
5. Analyze results
6. Compare variants
7. Select top candidates

For detailed instructions, see the main [README.md](README.md)
