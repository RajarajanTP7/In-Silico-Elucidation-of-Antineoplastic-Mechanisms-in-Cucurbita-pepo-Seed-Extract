# In Silico Investigation of Antineoplastic Mechanisms of *Cucurbita pepo* Seed Phytochemicals Targeting HER2

## 📌 Project Overview

This repository presents a **reproducible computational biology workflow** to investigate the interaction of phytochemicals identified from *Cucurbita pepo* (pumpkin) seed aqueous extract with the **HER2 kinase domain**, a clinically relevant oncogenic target in breast and lung cancers.

The study integrates **GC–MS compound identification**, **molecular docking**, **ADMET screening**, **100 ns molecular dynamics (MD) simulations**, and **MM-GBSA binding free energy analysis** to evaluate **binding plausibility, energetic stability, and pharmacokinetic feasibility** of selected phytochemicals.

> ⚠️ This work is **mechanistic and exploratory**. It does not claim kinase selectivity or therapeutic efficacy. Results are intended to generate hypotheses for experimental validation.

---

## Scientific Rationale

- HER2 is a validated oncogenic driver and therapeutic target.
- Plant-derived fatty acids and lipid esters are known to modulate signaling pathways but are often **non-selective**.
- Computational screening enables **rapid mechanistic insight** before experimental studies.

**Research question:**  
Can GC–MS–identified phytochemicals from *Cucurbita pepo* form **stable and energetically favorable complexes** with the HER2 kinase domain under explicit solvent conditions?

---

## 🎯 Objectives

1. Identify phytochemicals in *C. pepo* seed aqueous extract via GC–MS  
2. Evaluate binding affinity toward HER2 using molecular docking  
3. Screen compounds based on ADMET and drug-likeness criteria  
4. Assess binding stability via 100 ns molecular dynamics simulations  
5. Quantify binding energetics using MM-GBSA  
6. Provide a **fully reproducible computational pipeline**

---

## 🧪 Methodological Workflow

```
Plant Material → Soxhlet Extraction → GC–MS Profiling
                    ↓
             Ligand Identification
                    ↓
         Molecular Docking (PyRx / AutoDock Vina)
                    ↓
              ADMET Screening
                    ↓
         Molecular Dynamics Simulation (Desmond)
```

---

## 🧬 Target Protein

- **Protein:** Human Epidermal Growth Factor Receptor 2 (HER2)
- **PDB ID:** 3PP0
- **Domain Used:** Kinase domain (Chain A; residues 703–1029)
- **Justification:** Canonical oncogenic kinase target with a well-characterized ATP-binding pocket

---

## 🧫 Ligand Identification and Preparation

- Phytochemicals identified experimentally via **GC–MS**
- Only GC–MS–confirmed compounds were included (no virtual libraries)
- Ligands retrieved from **PubChem** (SDF format)
- Protonation and energy minimization performed using **PyRx / LigPrep** at pH 7.0

---

## ⚙️ Protocol - Molecular Docking

- **Software:** AutoDock Vina (via PyRx)
- **Docking Strategy:** Blind docking
- **Grid Dimensions:**
  - X = 59.5691  
  - Y = 48.1705  
  - Z = 59.0717
- **Scoring Metric:** Binding affinity (kcal/mol)
- **Interaction Analysis:** LigPlot+

**Selection Criteria**
- Favorable binding energy
- Consistent interactions within the kinase active-site region
- Structural plausibility

---

## 🧾 ADMET Analysis

**Tools Used**
- SwissADME  
- ADMETlab 2.0  

**Parameters Assessed**
- Lipinski’s Rule of Five
- Oral bioavailability
- CYP450 inhibition risk
- BBB permeability
- Toxicological endpoints

Compounds with clear pharmacokinetic red flags were excluded.

---

## 🖥 Molecular Dynamics Simulation

### System Setup

- **Software:** Desmond (Schrödinger)
- **Force Field:** OPLS-2005
- **Solvent Model:** TIP3P
- **Box Type:** Orthorhombic
- **Ionic Strength:** 0.15 M NaCl
- **Ensemble:** NPT
- **Conditions:** 300 K, 1 atm
- **Simulation Time:** 100 ns
- **Trajectory Interval:** 100 ps

All system preparation and execution scripts are included for reproducibility.

---

## Trajectory and Energy Analysis

Post-simulation analysis includes:

- Root Mean Square Deviation (RMSD)
- Root Mean Square Fluctuation (RMSF)
- Ligand–protein hydrogen bond persistence
- Radius of gyration (Rg)
- MM-GBSA binding free energy decomposition

Custom Python scripts are provided for data parsing and visualization.

---

## MM-GBSA Binding Free Energy

Binding free energy was calculated using:

[DeltaG{bind} = G{complex} - (G{protein} + G{ligand})]

### Key Results (Linoleic Acid)

| Time | ΔG<sub>bind</sub> (kcal/mol) |
|------|------------------------------|
| 0 ns | −94.24 |
| 100 ns | −74.24 |

**Interpretation**
- Binding remains energetically favorable throughout the simulation
- Decrease in ΔG reflects **ligand flexibility and solvent exposure**
- Behavior is consistent with **long-chain fatty acids**, which are inherently non-rigid and non-selective

---

## 🏆 Key Findings

- GC–MS identified 13 phytochemicals, primarily fatty acids and lipid esters
- Linoleic acid demonstrated:
  - Favorable docking affinity
  - Acceptable ADMET profile
  - Stable MD behavior over 100 ns
- Long-chain lipid esters show membrane interaction potential but lack target specificity

---

## Limitations

- No experimental (in vitro or in vivo) validation
- Fatty acids are **not selective kinase inhibitors**
- MM-GBSA provides relative, not absolute, binding free energies
- Results should be interpreted as **hypothesis-generating**

These limitations are explicitly acknowledged to avoid overinterpretation.

---

## 📂 Repository Structure

```

├── GC-MS/
│ └── compound_list.csv
├── Docking/
│ ├── Docked_Complex_Structures/
│ ├── Individual_Structures/
│ └── Docking_Results.xlsx
├── ADMET/
│ ├── SwissADME/
│ ├── ADMETlab/
│ └── admet_results.xlsx
├── Molecular_Dynamics/
│ ├── MD_setup.md
│ ├── md.msj
│ ├── trajectories/
│ ├── Analysis/
│ │ ├── md_analysis.py
│ │ ├── mmgbsa_analysis.py
│ │ └── plots/
│ └── protein-ligand-mmgbsa-out.csv
├── LigPlot/
└── README.md

```

## 📚 Keywords

*Cucurbita pepo*, HER2, Molecular Docking, GC–MS, ADMET, Molecular Dynamics,  MM-GBSA, Computational Oncology, Cancer, Phytochemicals
