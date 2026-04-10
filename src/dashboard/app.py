# Import required libraries
import pandas as pd
import streamlit as st

# Path of the input file
DATA_FILE = "data/processed/events_drive.csv"

# Set page title and layout
st.set_page_config(page_title="ADAS KPI Dashboard", layout="wide")

# Dashboard title
st.title("ADAS Event Mining and KPI Dashboard")

# Read the processed event data
df = pd.read_csv(DATA_FILE)

# -----------------------------------
# Calculate KPIs
# -----------------------------------

max_speed = df["speed_kmh"].max()
avg_speed = df["speed_kmh"].mean()
hard_brake_count = df["hard_brake"].sum()
harsh_accel_count = df["harsh_accel"].sum()
sharp_steer_count = df["sharp_steer"].sum()

# -----------------------------------
# Show KPI cards
# -----------------------------------

st.subheader("Main KPIs")

col1, col2, col3 = st.columns(3)

# First row of KPI values
col1.metric("Max Speed (km/h)", f"{max_speed}")
col2.metric("Average Speed (km/h)", f"{avg_speed:.2f}")
col3.metric("Hard Brake Count", int(hard_brake_count))

col4, col5 = st.columns(2)

# Second row of KPI values
col4.metric("Harsh Acceleration Count", int(harsh_accel_count))
col5.metric("Sharp Steering Count", int(sharp_steer_count))

# -----------------------------------
# Show line chart for main signals
# -----------------------------------

st.subheader("Vehicle Signals Over Time")

# Use timestamp as x-axis
signal_data = df.set_index("timestamp")[["speed_kmh", "accel_mps2", "steering_deg"]]

st.line_chart(signal_data)

# -----------------------------------
# Show event counts as a bar chart
# -----------------------------------

st.subheader("Detected Event Counts")

event_counts = pd.DataFrame({
    "event_name": ["Hard Brake", "Harsh Acceleration", "Sharp Steering"],
    "count": [hard_brake_count, harsh_accel_count, sharp_steer_count]
})

# Set event_name as index so Streamlit shows labels nicely
event_counts = event_counts.set_index("event_name")

st.bar_chart(event_counts)

# -----------------------------------
# Show full table
# -----------------------------------

st.subheader("Processed Event Data")

st.dataframe(df)