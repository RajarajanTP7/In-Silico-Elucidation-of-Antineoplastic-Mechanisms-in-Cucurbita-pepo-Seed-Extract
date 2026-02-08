# Step 1: Protein preparation
$SCHRODINGER/utilities/prepwizard \
  3PP0.pdb \
  3PP0_prepared.mae \
  -fillsidechains \
  -fillloops \
  -propka_pH 7.0 \
  -disulfides \
  -rehtreat

# Step 2: Ligand preparation
$SCHRODINGER/ligprep \
  -ismi linoleic_acid.smi \
  -omae linoleic_acid.mae \
  -pH 7.0 \
  -epik

# Step 3: Complex formation
$SCHRODINGER/utilities/structcat \
  3PP0_prepared.mae linoleic_acid.mae \
  complex.mae

# Step 4: System Builder
$SCHRODINGER/desmond/system_builder \
  -m complex.mae \
  -o system_out.cms \
  -solvent TIP3P \
  -shape orthorhombic \
  -neutralize \
  -salt 0.15
