# Import required libraries
from pathlib import Path
import pandas as pd

# Path of the cleaned input file
INPUT_FILE = Path("data/processed/clean_drive.csv")

# Path of the output file with detected events
OUTPUT_FILE = Path("data/processed/events_drive.csv")


def detect_events(df):
    """
    This function adds new columns that mark
    different driving events.
    """

    # Make a copy so original data stays unchanged
    df = df.copy()

    # Hard brake:
    # If acceleration is less than -3.0, mark as True
    df["hard_brake"] = df["accel_mps2"] < -3.0

    # Harsh acceleration:
    # If acceleration is greater than 2.5, mark as True
    df["harsh_accel"] = df["accel_mps2"] > 2.5

    # Sharp steering:
    # abs() means check both positive and negative values
    # If steering angle is greater than 12 degrees, mark as True
    df["sharp_steer"] = df["steering_deg"].abs() > 12

    return df


# This part runs only when we directly execute this file
if __name__ == "__main__":

    # Step 1: Read the cleaned CSV file
    df = pd.read_csv(INPUT_FILE)

    # Step 2: Detect events
    events_df = detect_events(df)

    # Step 3: Save the new CSV file
    events_df.to_csv(OUTPUT_FILE, index=False)

    # Step 4: Print message to confirm success
    print("Event detection completed successfully!")
    print(f"Saved file: {OUTPUT_FILE}")

    # Show first 5 rows
    print("\nPreview of event data:")
    print(events_df.head())