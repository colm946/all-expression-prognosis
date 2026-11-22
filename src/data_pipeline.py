import pandas as pd
from pathlib import Path
import numpy as numpy

sample_sheet_path = "/workspaces/all-expression-prognosis/data/gdc_sample_sheet.tsv"
raw_data_path = Path("/workspaces/all-expression-prognosis/data/raw")

def get_gene_id(param_gene_id):
    gene_id = param_gene_id.split(".")[0]
    return gene_id

"""Building compatability over the full amount of data now, using the tsv sheet to find the folders inside the raw data then assigning patient number using case id add to the big matrix"""

gene_data_frames = []
sample_sheet_df = pd.read_csv(sample_sheet_path, sep="\t", comment="#")

for file_id, case_id in zip(sample_sheet_df["File ID"], sample_sheet_df["Case ID"]):
    
    data_tsv = next((raw_data_path / file_id).glob("*.tsv"))

    gene_data_df = pd.read_csv(data_tsv, sep="\t", comment="#", usecols=["gene_id", "tpm_unstranded"]).iloc[4:]
    gene_data_df["gene_id"] = gene_data_df["gene_id"].apply(get_gene_id)
    gene_data_df = gene_data_df.drop_duplicates(subset="gene_id")
    gene_data_df["tpm_unstranded"] = gene_data_df["tpm_unstranded"].to_numpy(dtype=numpy.float32)
    patient = gene_data_df.set_index("gene_id")["tpm_unstranded"].rename(case_id)
    
    gene_data_frames.append(patient)

output_path = Path("/workspaces/all-expression-prognosis/data/processed/tpm_expression_matrix.parquet")
large_gene_dataset = pd.concat(gene_data_frames, axis=1).T
large_gene_dataset.to_parquet(output_path)