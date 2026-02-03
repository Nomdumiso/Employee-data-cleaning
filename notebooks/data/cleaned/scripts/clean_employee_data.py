import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
CLEANED_DIR = BASE_DIR / "data" / "cleaned"

RAW_DIR.mkdir(parents=True, exist_ok=True)
CLEANED_DIR.mkdir(parents=True, exist_ok=True)

excel_path = BASE_DIR / "Week-3-Employee-Data.xlsx"
raw_csv_path = RAW_DIR / "employee_data_raw.csv"
cleaned_csv_path = CLEANED_DIR / "employee_data_cleaned.csv"

print(f"Reading Excel from: {excel_path}")

df = pd.read_excel(excel_path)

df.to_csv(raw_csv_path, index=False)
print("✓ Raw CSV created")

df['department'] = df['department'].replace({
    'HR': 'Human Resource',
    'H.R': 'Human Resource',
    'Human Resources': 'Human Resource',
    'IT': 'Information Technology',
    'Ops': 'Operations',
    'Eng': 'Engineering',
    'FIN': 'Finance',
    'sales': 'Sales'
})

df['currency'] = df['currency'].replace({
    'R': 'ZAR',
    'ZAR': 'ZAR',
    '$': 'USD',
    'USD': 'USD',
    '£': 'GBP',
    'Â£': 'GBP'
})

df.to_csv(cleaned_csv_path, index=False)
print("✓ Cleaned data saved")

print(f"Rows: {len(df)}")
