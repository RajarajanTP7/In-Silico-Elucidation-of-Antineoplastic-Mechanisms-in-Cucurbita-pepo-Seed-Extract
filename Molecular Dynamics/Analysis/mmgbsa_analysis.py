import pandas as pd

data = pd.read_csv("protein-ligand-mmgbsa-out.csv")

print("Average ΔGbind:", data['r_psp_MMGBSA_dG_Bind'].mean())
print("Std Dev ΔGbind:", data['r_psp_MMGBSA_dG_Bind'].std())

# Compare early vs late simulation
early = data[data['title'] == '0 ns']['r_psp_MMGBSA_dG_Bind'].values[0]
late = data[data['title'] == '100 ns']['r_psp_MMGBSA_dG_Bind'].values[0]

print(f"ΔGbind at 0 ns: {early:.2f} kcal/mol")
print(f"ΔGbind at 100 ns: {late:.2f} kcal/mol")
