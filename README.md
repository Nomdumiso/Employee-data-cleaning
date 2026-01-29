# Employee Data Cleaning Project

## 📋 Project Overview
This project involves comprehensive data cleaning and analysis of employee records using Python and Excel. The dataset contains 155 employee records with 17 columns including personal information, job details, salary data, and location information.

## 👥 Group Members
- **Khayalethu Shezi** – Excel Analysis
- **Celimpilo Gumede** – Excel Analysis
- **Aobakwe Modillane** – Python Data Cleaning
- **Nomdumiso Mtshilibe** – Python HR KPIs & Analysis

## 🗂️ Project Structure
```
Employee-data-cleaning/
├── data/
│   ├── raw/
│   │   ├── Week-3-Employee-Data.xlsx
│   │   └── employee_data_raw.csv
│   └── cleaned/
│       └── employee_data_cleaned.csv
├── notebooks/
│   └── data_cleaning.ipynb
├── .gitignore
└── README.md
```

## 🔧 Data Cleaning Process

### Issues Identified and Resolved:
1. **Gender Values**: Standardized inconsistent values (M → Male, F → Female)
2. **Department Names**: Unified variations (H.R. → Human Resource, Ops → Operations)
3. **Date Formats**: Converted mixed date formats to standard datetime format
4. **Currency Codes**: Standardized currency symbols ($ → USD, £ → GBP, R → ZAR)
5. **Country Names**: Unified country representations (SA → South Africa)
6. **Email Validation**: Verified email format and completeness
7. **Date Logic**: Identified and corrected exit dates before hire dates
8. **Salary Data**: Checked for and handled negative salary values
9. **Missing Values**: Identified and documented missing data patterns
10. **Duplicate Records**: Checked for and removed duplicate entries

## 🛠️ Tools & Technologies
- **Python 3.13**
  - pandas - Data manipulation and cleaning
  - numpy - Numerical operations
  - re - Regular expressions for pattern matching
  - pathlib - File path handling
- **Jupyter Notebook** - Interactive development environment
- **Microsoft Excel** - Data exploration and pivot analysis
- **Git & GitHub** - Version control

## 📊 Dataset Information
- **Total Records**: 155 employees
- **Columns**: 17 (employee_id, first_name, last_name, email, gender, department, job_title, hire_date, exit_date, is_active, salary, currency, country, state, city, manager_id, performance_rating)
- **Data Quality Issues Resolved**: 10+ categories of inconsistencies

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy openpyxl jupyter
```

### Running the Project
1. Clone the repository:
```bash
git clone https://github.com/Nomdumiso/Employee-data-cleaning.git
cd Employee-data-cleaning
```

2. Navigate to notebooks folder:
```bash
cd notebooks
```

3. Open Jupyter Notebook:
```bash
jupyter notebook data_cleaning.ipynb
```

4. Run all cells to execute the data cleaning process

## 📈 Key Outputs
- **Cleaned Dataset**: `data/cleaned/employee_data_cleaned.csv`
- **Data Quality Report**: Documented in the Jupyter notebook
- **HR KPIs**: Calculated metrics for workforce analysis

## 📝 Files Included
- `Week-3-Employee-Data.xlsx` - Original raw data file
- `employee_data_raw.csv` - Converted CSV format
- `employee_data_cleaned.csv` - Final cleaned dataset
- `data_cleaning.ipynb` - Complete data cleaning workflow
- Excel workbook with pivot tables and visualizations

## 🤝 Contributing
This is a group project. For any questions or contributions, please contact the team members listed above.

## 📄 License
This project is part of an academic assignment.

## 🙏 Acknowledgments
- Dataset provided as part of Week 3 coursework
- Thanks to all team members for their contributions

---

**Repository**: [Employee-data-cleaning](https://github.com/Nomdumiso/Employee-data-cleaning)
