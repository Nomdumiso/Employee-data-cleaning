# Employee Data Cleaning (Week 3)

Team
- Nomdumiso — Part 4 (HR KPIs, tenure, turnover)
- Aaobakwe Modillane — Part 3 (Import & Clean in Python)
- Khayalethu Shezi — Part A (Excel pivots/charts)
- Celimpilo Gumede — Part A (Excel pivots/charts)

Overview
This repository contains files and scripts to clean and analyze an employee dataset (Week-3-Employee-Data.csv), validate summaries in Excel, and compute HR KPIs using Python (pandas) in a Jupyter notebook. The project is split across Excel (Part A) and Python (Part B).

Repository structure (recommended)
- data/
  - Week-3-Employee-Data.csv  # original dataset (place here)
  - Week-3-Employee-Data_CLEANED.csv  # cleaned output (generated)
- notebooks/
  - week3_cleaning.ipynb  # Jupyter Notebook with cleaning and KPI calculations
- excel/
  - Week3_pivots.xlsx  # Excel workbook with pivot tables and chart (Part A)
- reports/
  - one_page_summary.pdf  # one-page summary for submission
- README.md
- requirements.txt

How to run (local environment)
1. Clone the repo:
   git clone https://github.com/Nomdumiso/Employee-data-cleaning.git
2. Create and activate a virtual environment (example with venv):
   python -m venv .venv
   source .venv/bin/activate  (mac/linux)
   .venv\Scripts\activate     (Windows)
3. Install dependencies:
   pip install -r requirements.txt
4. Launch Jupyter Lab or Notebook:
   jupyter lab  # or jupyter notebook
5. Open notebooks/week3_cleaning.ipynb and run the cells.

Suggested requirements.txt
pandas>=1.5
numpy
openpyxl
jupyterlab
python-dateutil

Part A — Excel (20 marks)
- Use Microsoft Excel to create pivot tables and charts for the following:
  - Headcount by Department (count of employee_id)
  - Active vs Inactive Employees by Department (use is_active)
  - Hires by Year (derive year from hire_date)
  - Average Salary by Department and Currency (do not convert currencies in Excel)
  - Create one chart (bar/column) showing headcount by department
- Save the workbook as excel/Week3_pivots.xlsx. Label sheets clearly (Headcount, Active_vs_Inactive, Hires_by_Year, AvgSalary).

Part B — Python (20 marks)
- In notebooks/week3_cleaning.ipynb implement Part 3 (Import & Clean) and Part 4 (HR KPIs):
  - Load data from data/Week-3-Employee-Data.csv
  - Convert hire_date and exit_date to datetime, salary and manager_id to numeric
  - Trim whitespace, normalize casing, standardize department and currency values
  - Handle missing values with documented decisions
  - Remove duplicates using employee_id
  - Flag invalid emails, negative salaries, and exit_date earlier than hire_date
  - Save cleaned output to data/Week-3-Employee-Data_CLEANED.csv
  - Compute KPIs: current headcount, hires by year, avg salary by department and currency, median tenure for active employees, turnover rate

Deliverables (what to submit)
- excel/Week3_pivots.xlsx  (Excel workbook with pivot sheets and a chart)
- notebooks/week3_cleaning.ipynb  (Jupyter Notebook with commented steps)
- data/Week-3-Employee-Data_CLEANED.csv  (cleaned dataset)
- reports/one_page_summary.pdf  (one-page summary with team names and brief findings)

Notes & workflow suggestions
- Work locally with Jupyter Lab or VS Code + Jupyter extension, or use GitHub Codespaces for a cloud environment.
- If using Google Colab, upload the CSV to the Colab session or mount Google Drive and remember to download the cleaned CSV and notebook for submission.
- Document all cleaning decisions in the notebook so graders can follow your reasoning.

Next steps I can take for you
- Create and commit a notebook skeleton (notebooks/week3_cleaning.ipynb) with code cells for Parts 3 & 4.
- Upload a starter requirements.txt.
- Add collaborators to this repository (invite usernames you provide).