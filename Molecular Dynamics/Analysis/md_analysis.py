import pandas as pd
import matplotlib.pyplot as plt

# Load RMSD
rmsd = pd.read_csv("rmsd.csv")
plt.plot(rmsd['Time (ns)'], rmsd['RMSD (Å)'])
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (Å)")
plt.title("HER2–Linoleic Acid RMSD")
plt.show()

# Load RMSF
rmsf = pd.read_csv("rmsf.csv")
plt.plot(rmsf['Residue'], rmsf['RMSF (Å)'])
plt.xlabel("Residue Index")
plt.ylabel("RMSF (Å)")
plt.title("Residue Flexibility (RMSF)")
plt.show()
