"""
Structure Preparation Module for Cutin Synthase
Handles protein structure loading, cleaning, and preparation for analysis
"""

from Bio.PDB import PDBParser, PDBIO, Select
import warnings
from pathlib import Path


class CleanStructure(Select):
    """Select only protein atoms, removing water and heteroatoms"""
    def accept_residue(self, residue):
        if residue.get_id()[0] == ' ':  # Standard residues only
            return True
        return False


class StructurePreparator:
    """
    Prepare protein structures for mutation screening and MD simulations
    """
    
    def __init__(self, pdb_file):
        """
        Initialize with a PDB file
        
        Parameters:
        -----------
        pdb_file : str or Path
            Path to the PDB file
        """
        self.pdb_file = Path(pdb_file)
        self.parser = PDBParser(QUIET=True)
        self.structure = None
        
    def load_structure(self):
        """Load structure from PDB file"""
        try:
            self.structure = self.parser.get_structure('cutin_synthase', self.pdb_file)
            print(f"Successfully loaded structure from {self.pdb_file}")
            return self.structure
        except Exception as e:
            print(f"Error loading structure: {e}")
            return None
    
    def clean_structure(self, output_file=None):
        """
        Remove water molecules and heteroatoms
        
        Parameters:
        -----------
        output_file : str or Path, optional
            Output file path for cleaned structure
        """
        if self.structure is None:
            print("No structure loaded. Call load_structure() first.")
            return None
        
        io = PDBIO()
        io.set_structure(self.structure)
        
        if output_file is None:
            output_file = self.pdb_file.stem + "_clean.pdb"
        
        io.save(str(output_file), CleanStructure())
        print(f"Cleaned structure saved to {output_file}")
        return output_file
    
    def get_sequence(self):
        """Extract protein sequence from structure"""
        if self.structure is None:
            print("No structure loaded. Call load_structure() first.")
            return None
        
        from Bio.SeqUtils import seq1
        sequence = ""
        
        for model in self.structure:
            for chain in model:
                for residue in chain:
                    if residue.get_id()[0] == ' ':  # Standard residue
                        try:
                            sequence += seq1(residue.get_resname())
                        except:
                            sequence += 'X'  # Unknown residue
        
        return sequence
    
    def analyze_structure(self):
        """
        Perform basic structure analysis
        
        Returns:
        --------
        dict : Structure statistics
        """
        if self.structure is None:
            print("No structure loaded. Call load_structure() first.")
            return None
        
        stats = {
            'num_models': len(list(self.structure.get_models())),
            'num_chains': 0,
            'num_residues': 0,
            'num_atoms': 0
        }
        
        for model in self.structure:
            for chain in model:
                stats['num_chains'] += 1
                for residue in chain:
                    if residue.get_id()[0] == ' ':
                        stats['num_residues'] += 1
                        stats['num_atoms'] += len(list(residue.get_atoms()))
        
        return stats


def main():
    """Example usage"""
    print("Structure Preparation Module for Cutin Synthase")
    print("=" * 50)
    print("\nThis module provides tools to:")
    print("- Load and parse PDB structures")
    print("- Clean structures (remove water, heteroatoms)")
    print("- Extract sequences")
    print("- Analyze structure statistics")
    print("\nUsage example:")
    print("  prep = StructurePreparator('path/to/structure.pdb')")
    print("  prep.load_structure()")
    print("  prep.clean_structure('cleaned.pdb')")
    print("  stats = prep.analyze_structure()")


if __name__ == "__main__":
    main()
