# 🚗 ADAS Event Mining and KPI Dashboard

## 📌 Project Overview

This project is a beginner-friendly automotive data analytics system designed to simulate and analyze vehicle telemetry data.

It processes driving data to detect key driving events such as:
- Hard braking
- Harsh acceleration
- Sharp steering

The system computes important driving KPIs and visualizes them using an interactive dashboard.

---

## 🎯 Objective

The goal of this project is to demonstrate:

- Understanding of vehicle data analysis
- Basic ADAS-related event detection
- KPI computation for driving behavior
- Data visualization using dashboards
- Structured Python-based data pipeline

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn (planned)**
- **Streamlit (Dashboard)**
- **Git & GitHub**

---

## 📂 Project Structure
adas-event-mining-dashboard/
├── data/
│ ├── raw/ # Raw input data
│ └── processed/ # Cleaned and processed data
├── src/
│ ├── ingest/ # Data loading scripts
│ ├── preprocessing/ # Data cleaning
│ ├── events/ # Event detection logic
│ ├── features/ # KPI computation
│ └── dashboard/ # Streamlit dashboard
├── README.md
├── requirements.txt


---

## ⚙️ How the System Works

### Step 1 — Data Ingestion
Reads raw vehicle telemetry data from CSV.

### Step 2 — Data Cleaning
- Removes duplicates  
- Handles missing values  
- Converts data types  

### Step 3 — Event Detection
Detects driving events using simple rules:

- Hard Brake → acceleration < -3.0  
- Harsh Acceleration → acceleration > 2.5  
- Sharp Steering → steering angle > 12  

### Step 4 — KPI Calculation
Calculates:

- Maximum speed  
- Average speed  
- Event counts  
- Brake usage  

### Step 5 — Dashboard Visualization
Displays:
- KPI cards  
- Line charts (speed, acceleration, steering)  
- Event count charts  
- Full dataset  

---

## 📊 Sample Output

The dashboard shows:

- Driving KPIs
- Event detection results
- Vehicle signal trends over time

---

## ▶️ How to Run the Project

### 1. Activate virtual environment
```bash
source .venv/bin/activate