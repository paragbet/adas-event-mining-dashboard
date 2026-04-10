# Import required libraries
from pathlib import Path
import pandas as pd

# Path of the input file (raw data)
INPUT_FILE = Path("data/raw/sample_drive.csv")

# Path of the output file (cleaned data)
OUTPUT_FILE = Path("data/processed/clean_drive.csv")


def clean_drive_data(df):
    """
    This function cleans the input dataframe.
    """

    # Make a copy so the original dataframe stays unchanged
    df = df.copy()

    # Remove duplicate rows if any exist
    df = df.drop_duplicates()

    # Replace missing values with 0
    df = df.fillna(0)

    # List of columns that should contain numbers
    numeric_columns = [
        "timestamp",
        "speed_kmh",
        "accel_mps2",
        "steering_deg",
        "brake",
        "throttle"
    ]

    # Convert these columns to numeric values
    # If conversion fails, replace with 0
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)

    # Convert brake column to integer (0 or 1)
    df["brake"] = df["brake"].astype(int)

    return df


# This part runs only when we directly execute this file
if __name__ == "__main__":

    # Step 1: Read the raw CSV file
    df = pd.read_csv(INPUT_FILE)

    # Step 2: Clean the data
    cleaned_df = clean_drive_data(df)

    # Step 3: Make sure output folder exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Step 4: Save cleaned data to a new CSV file
    cleaned_df.to_csv(OUTPUT_FILE, index=False)

    # Step 5: Print message to confirm success
    print("Cleaning completed successfully!")
    print(f"Saved file: {OUTPUT_FILE}")

    # Show first 5 rows
    print("\nPreview of cleaned data:")
    print(cleaned_df.head())