import pandas as pd

"""Strategy - restrict to primary diagnosis types."""

sample_sheet_path = "/workspaces/all-expression-prognosis/data/gdc_sample_sheet.tsv"
raw_data = "/workspaces/all-expression-prognosis/data/gdc_sample_sheet.tsv"

df = pd.read_csv(sample_sheet_path, sep="\t", comment="#")

def check_files():
    for file_id in df["File ID"]:
        try:
            file = raw_data.find(file_id)
        except:
            return f"File not found - id: {file_id}"

def count_patients():
    unique_patients = []

    for case_id in df["Case ID"]:
        try:
            unique_patients.find(case_id)
        except:
            unique_patients.append(case_id)

    return len(unique_patients)


def count_primary_recurrence():
    primary = 0
    recurrence = 0
    other = 0

    for type in df["Tumor Descriptor"]:
        if type == "Primary":
            primary += 1
        elif type == "Recurrence":
            recurrence += 1
        else:
            other += 1

    return f"P: {primary}, R: {recurrence}, O: {other}"