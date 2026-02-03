"""
Script Name: hr_kpis.py

Purpose:
This script calculates key HR KPIs from a cleaned employee dataset.
It generates CSV output files for reporting and analysis.

KPIs Calculated:
1. Total employees
2. Active vs inactive employees
3. Attrition rate
4. Hires by year
5. Average salary by department and currency

Output Location:
notebooks/data/results/
"""

import pandas as pd
from pathlib import Path

# -----------------------------
# File Paths
# -----------------------------
BASE_DIR = Path(r"C:\Users\nmtsh\OneDrive\Employee-data-cleaning\notebooks\data")

INPUT_FILE = BASE_DIR / "processed" / "employee_cleaned.csv"
RESULTS_DIR = BASE_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv(INPUT_FILE)

# Convert dates
df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')
df['exit_date'] = pd.to_datetime(df['exit_date'], errors='coerce')

# -----------------------------
# KPI 1: Overall HR KPIs
# -----------------------------
total_employees = len(df)
active_employees = df[df['is_active'] == True].shape[0]
inactive_employees = df[df['is_active'] == False].shape[0]

attrition_rate = round((inactive_employees / total_employees) * 100, 2)

hr_kpis = pd.DataFrame({
    "Metric": [
        "Total Employees",
        "Active Employees",
        "Inactive Employees",
        "Attrition Rate (%)"
    ],
    "Value": [
        total_employees,
        active_employees,
        inactive_employees,
        attrition_rate
    ]
})

hr_kpis.to_csv(RESULTS_DIR / "hr_kpis_results.csv", index=False)

# -----------------------------
# KPI 2: Hires by Year
# -----------------------------
df['hire_year'] = df['hire_date'].dt.year

hires_by_year = (
    df.groupby('hire_year')
      .size()
      .reset_index(name='number_of_hires')
      .sort_values('hire_year')
)

hires_by_year.to_csv(RESULTS_DIR / "hires_by_year.csv", index=False)

# -----------------------------
# KPI 3: Average Salary by Department & Currency
# -----------------------------
avg_salary = (
    df.groupby(['department', 'currency'])['salary']
      .mean()
      .round(2)
      .reset_index(name='average_salary')
)

avg_salary.to_csv(
    RESULTS_DIR / "avg_salary_by_dept_currency.csv",
    index=False
)

print("✅ HR KPI files successfully created in the results folder.")
