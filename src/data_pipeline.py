import pandas as pd

tsv_path = "/workspaces/all-expression-prognosis/data/raw_extracted/50b6d60d-faf6-4ac8-960d-e06cd7d1d929/4915c991-29f0-494a-bf34-7cafa01ed781.rna_seq.augmented_star_gene_counts.tsv"

df = pd.read_csv(tsv_path, sep="\t", comment="#")
df = df.iloc[4:]
# strips the first 3 rows (placeholder values)

def get_gene_id(param_gene_id):
    gene_id = param_gene_id.split(".")[0]
    return gene_id

"""gene = get_gene_id(df.loc[6]["gene_id"])
Example of how to find one id"""

df["gene_id"] = df["gene_id"].apply(get_gene_id)

patient = df.set_index("gene_id")["tpm_unstranded"].rename("Patient_1")
df = patient.to_frame().T

print(df.iloc[:, :5])