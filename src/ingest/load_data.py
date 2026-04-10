from pathlib import Path
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    df = load_csv("data/raw/sample_drive.csv")

    print("Data Loaded Successfully!\n")
    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())