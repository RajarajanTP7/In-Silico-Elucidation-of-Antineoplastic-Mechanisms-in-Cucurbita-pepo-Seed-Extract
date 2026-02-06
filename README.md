# In Silico Elucidation of Antineoplastic Mechanisms in *Cucurbita pepo* Seed Extract

## 📌 Project Overview

This project investigates the **anticancer potential of *Cucurbita pepo* (pumpkin) seed aqueous extract** using an integrated **computational biology workflow**. The study focuses on identifying bioactive phytochemicals and evaluating their interaction with the **HER2 kinase domain**, a clinically relevant target in breast and lung cancers.

The work combines **GC–MS compound profiling**, **molecular docking**, **ADMET prediction**, and **molecular dynamics (MD) simulations** to assess binding stability and drug-likeness of identified compounds.

This repository documents the **in-silico pipeline**, datasets, structures, and parameters used in the study.

---

## 🎯 Objectives

* Identify bioactive compounds in *C. pepo* seed aqueous extract via GC–MS
* Evaluate binding affinity of identified compounds against HER2 (PDB ID: 3PP0)
* Assess drug-likeness and pharmacokinetic properties using ADMET tools
* Validate top ligand–protein complexes through 100 ns MD simulations
* Provide a reproducible computational workflow for future experimental validation

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

* **Protein:** Human Epidermal Growth Factor Receptor 2 (HER2)
* **PDB ID:** 3PP0
* **Domain Used:** Kinase domain (Chain A; residues 703–1029)
* **Rationale:** HER2 is a validated oncogenic driver and therapeutic target in breast and lung cancers

---

## 🧫 Ligand Preparation

* Ligands identified from GC–MS were retrieved from **PubChem**
* Structures downloaded in **SDF format**
* Energy minimization and conversion to **PDBQT** performed using **PyRx**
* Only GC–MS-confirmed compounds were included (no virtual libraries)

---

## ⚙️ Docking Protocol

* **Software:** PyRx (AutoDock Vina engine)
* **Docking Type:** Blind docking
* **Grid Dimensions:**

  * X = 59.5691
  * Y = 48.1705
  * Z = 59.0717
* **Scoring Metric:** Binding affinity (kcal/mol)
* **Interaction Analysis:** LigPlot

Lower binding energy and consistent active-site interactions were used as selection criteria.

---

## 🧾 ADMET Analysis

* **Tools Used:**

  * SwissADME
  * ADMETlab 2.0
* **Parameters Assessed:**

  * Lipinski’s Rule of Five
  * Oral bioavailability
  * CYP450 inhibition
  * BBB permeability
  * Toxicological endpoints

This step eliminated compounds with obvious pharmacokinetic red flags.

---

## 🖥 Molecular Dynamics Simulation

* **Software:** Desmond (Schrödinger LLC)
* **Simulation Time:** 100 ns
* **Force Field:** OPLS-2005
* **Solvent Model:** TIP3P
* **Box Type:** Orthorhombic
* **Ionic Strength:** 0.15 M NaCl
* **Conditions:** 300 K, 1 atm
* **Trajectory Interval:** 100 ps

### Binding Free Energy Calculation

[
\Delta G_{bind} = G_{complex} - (G_{protein} + G_{ligand})
]

---

## 🏆 Key Findings

* GC–MS identified **13 bioactive compounds**, including fatty acids and lipid esters
* **Linoleic acid (9,12-Octadecadienoic acid, Z,Z)** showed:

  * Strong binding affinity toward HER2
  * Favorable ADMET profile
  * Stable interaction during 100 ns MD simulation
* Long-chain fatty acid esters demonstrated good membrane interaction potential but remain **non-selective**, which is a known limitation

---

## 📂 Repository Structure

```
├── GC-MS/
│   └── compound_list.csv
├── Docking/
│   ├── Docked Complex - Protein-Ligand Structures/
│   ├── Docked Protein and ligand Structures (Not in complex)/
│   └── Structures for docking.xlsx
│   ├── MDcomplex.pdb
│   ├── Pumpkin Compounds - 3pp0 Docked results.xlsx
├── ADMET/
│   └── ADMET2.0 Results
│   └── Toxicity Assessment - Protux Results
│   └── admet_results.xlsx
├── Molecular Dynamics Simulation/
│   ├── Images/
│   └── MD Output Files/
│   └── protein-ligand-mmgbsa-out.csv
│   └── protein-ligand-out_pl_1.pdf
├── Ligplot/
└── README.md
```

## 📚 Keywords

*Cucurbita pepo*, HER2, Molecular Docking, GC–MS, ADMET, Molecular Dynamics, Cancer, Phytochemicals
