# Import required libraries
from pathlib import Path
import pandas as pd

# Path of the input file
INPUT_FILE = Path("data/processed/events_drive.csv")


def compute_kpis(df):
    """
    This function calculates KPIs from the dataframe.
    It returns the KPI values in a Python dictionary.
    """

    # Create a dictionary to store KPI results
    kpis = {}

    # Maximum speed in the trip
    kpis["max_speed_kmh"] = df["speed_kmh"].max()

    # Average speed in the trip
    kpis["avg_speed_kmh"] = df["speed_kmh"].mean()

    # Count how many hard brake events happened
    kpis["hard_brake_count"] = df["hard_brake"].sum()

    # Count how many harsh acceleration events happened
    kpis["harsh_accel_count"] = df["harsh_accel"].sum()

    # Count how many sharp steering events happened
    kpis["sharp_steer_count"] = df["sharp_steer"].sum()

    # Count how many times brake was used
    kpis["brake_usage_count"] = df["brake"].sum()

    return kpis


# This part runs only when we directly execute this file
if __name__ == "__main__":

    # Step 1: Read the event data file
    df = pd.read_csv(INPUT_FILE)

    # Step 2: Compute KPI values
    kpis = compute_kpis(df)

    # Step 3: Print KPI results
    print("KPI calculation completed successfully!\n")

    print("Trip KPIs:")
    print(f"Maximum Speed (km/h): {kpis['max_speed_kmh']}")
    print(f"Average Speed (km/h): {kpis['avg_speed_kmh']:.2f}")
    print(f"Hard Brake Count: {kpis['hard_brake_count']}")
    print(f"Harsh Acceleration Count: {kpis['harsh_accel_count']}")
    print(f"Sharp Steering Count: {kpis['sharp_steer_count']}")
    print(f"Brake Usage Count: {kpis['brake_usage_count']}")