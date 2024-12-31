import pandas as pd


def parse_file(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format")
