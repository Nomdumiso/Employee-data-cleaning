"""
Employee Data Cleaning Script
==============================

This script performs comprehensive data cleaning on employee data including:
- Data loading and initial exploration
- String standardization (trimming, case conversion)
- Data type conversions
- Date parsing and validation
- Category standardization (departments, currencies, countries, states, cities)
- Email validation
- Data quality checks (negative salaries, invalid dates)
- Duplicate removal
- Export to cleaned CSV

Author: Data Cleaning Project
Date: 2026
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime
from pathlib import Path
import os

# =============================================================================
# STEP 1: DATA LOADING
# =============================================================================

def load_data(file_path):
    """
    Load employee data from Excel or CSV file.
    
    Parameters:
    -----------
    file_path : str or Path
        Path to the input data file
        
    Returns:
    --------
    df : DataFrame
        Loaded employee data
    """
    print("=" * 70)
    print("STEP 1: LOADING DATA")
    print("=" * 70)
    
    file_path = Path(file_path)
    
    if file_path.suffix in ['.xlsx', '.xls']:
        df = pd.read_excel(file_path)
    elif file_path.suffix == '.csv':
        df = pd.read_csv(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")
    
    print(f"✓ Successfully loaded {len(df)} rows and {len(df.columns)} columns")
    print(f"✓ File: {file_path.name}")
    
    return df


# =============================================================================
# STEP 2: INITIAL DATA EXPLORATION
# =============================================================================

def explore_data(df):
    """
    Display initial data exploration and quality checks.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe to explore
    """
    print("\n" + "=" * 70)
    print("STEP 2: INITIAL DATA EXPLORATION")
    print("=" * 70)
    
    print(f"\nDataset Shape: {df.shape}")
    print(f"\nColumn Names:\n{df.columns.tolist()}")
    
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nFirst Few Rows:")
    print(df.head())
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print(f"\nDuplicate Rows: {df.duplicated().sum()}")


# =============================================================================
# STEP 3: STRING CLEANING
# =============================================================================

def clean_strings(df):
    """
    Clean string columns by trimming whitespace and standardizing case.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with cleaned string columns
    """
    print("\n" + "=" * 70)
    print("STEP 3: STRING CLEANING")
    print("=" * 70)
    
    # Get all string/object columns
    string_cols = df.select_dtypes(include=['object']).columns
    
    # Strip whitespace from all string columns
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip()
    
    # Standardize name formatting (Title Case)
    df['first_name'] = df['first_name'].str.title()
    df['last_name'] = df['last_name'].str.title()
    
    # Standardize email (lowercase)
    df['email'] = df['email'].str.lower()
    
    # Standardize city names (Title Case)
    df['city'] = df['city'].str.title()
    
    print("✓ Trimmed whitespace from all string columns")
    print("✓ Converted first_name and last_name to Title Case")
    print("✓ Converted email to lowercase")
    print("✓ Converted city to Title Case")
    
    return df


# =============================================================================
# STEP 4: DATA TYPE CONVERSIONS
# =============================================================================

def convert_data_types(df):
    """
    Convert columns to appropriate data types.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with converted data types
    """
    print("\n" + "=" * 70)
    print("STEP 4: DATA TYPE CONVERSIONS")
    print("=" * 70)
    
    # Convert salary (remove commas and convert to float)
    df['salary'] = df['salary'].astype(str).str.replace(',', '').str.strip()
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    print(f"✓ Converted salary to numeric (issues: {df['salary'].isnull().sum()})")
    
    # Convert manager_id to numeric
    df['manager_id'] = pd.to_numeric(df['manager_id'], errors='coerce')
    print(f"✓ Converted manager_id to numeric (null values: {df['manager_id'].isnull().sum()})")
    
    # Convert dates
    df['hire_date'] = pd.to_datetime(df['hire_date'], format='mixed', dayfirst=True, errors='coerce')
    df['exit_date'] = pd.to_datetime(df['exit_date'], format='mixed', dayfirst=True, errors='coerce')
    
    print(f"✓ Converted hire_date to datetime (invalid: {df['hire_date'].isnull().sum()})")
    print(f"✓ Converted exit_date to datetime (null: {df['exit_date'].isnull().sum()})")
    
    return df


# =============================================================================
# STEP 5: GENDER STANDARDIZATION
# =============================================================================

def standardize_gender(df):
    """
    Standardize gender values to consistent categories.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with standardized gender values
    """
    print("\n" + "=" * 70)
    print("STEP 5: GENDER STANDARDIZATION")
    print("=" * 70)
    
    gender_mapping = {
        'M': 'Male',
        'Male': 'Male',
        'F': 'Female',
        'Female': 'Female',
        'Other': 'Other'
    }
    
    df['gender'] = df['gender'].replace(gender_mapping)
    
    print("\nGender distribution after standardization:")
    print(df['gender'].value_counts())
    
    return df


# =============================================================================
# STEP 6: DEPARTMENT STANDARDIZATION
# =============================================================================

def standardize_department(df):
    """
    Standardize department names to consistent values.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with standardized department values
    """
    print("\n" + "=" * 70)
    print("STEP 6: DEPARTMENT STANDARDIZATION")
    print("=" * 70)
    
    dept_mapping = {
        'HR': 'Human Resource',
        'H.R': 'Human Resource',
        'H.R.': 'Human Resource',
        'Human Resources': 'Human Resource',
        'Human Resource': 'Human Resource',
        'IT': 'Information Technology',
        'Information Technology': 'Information Technology',
        'Ops': 'Operations',
        'Operations': 'Operations',
        'Eng': 'Engineering',
        'Engineering': 'Engineering',
        'FIN': 'Finance',
        'Finance': 'Finance',
        'sales': 'Sales',
        'Sales': 'Sales'
    }
    
    df['department'] = (
        df['department']
        .astype(str)
        .str.strip()
        .replace(dept_mapping)
    )
    
    print("\nDepartment distribution after standardization:")
    print(df['department'].value_counts())
    
    return df


# =============================================================================
# STEP 7: CURRENCY STANDARDIZATION
# =============================================================================

def standardize_currency(df):
    """
    Standardize currency codes to ISO format.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with standardized currency values
    """
    print("\n" + "=" * 70)
    print("STEP 7: CURRENCY STANDARDIZATION")
    print("=" * 70)
    
    currency_map = {
        "ZAR": "ZAR",
        "R": "ZAR",
        "$": "USD",
        "GBP": "GBP",
        "£": "GBP",
        "Â£": "GBP",  # Handle encoding issue
        "USD": "USD"
    }
    
    df['currency'] = df['currency'].replace(currency_map)
    
    print("\nCurrency distribution after standardization:")
    print(df['currency'].value_counts())
    
    return df


# =============================================================================
# STEP 8: COUNTRY STANDARDIZATION
# =============================================================================

def standardize_country(df):
    """
    Standardize country names to full official names.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with standardized country values
    """
    print("\n" + "=" * 70)
    print("STEP 8: COUNTRY STANDARDIZATION")
    print("=" * 70)
    
    country_mapping = {
        'south-africa': 'South Africa',
        'South Africa': 'South Africa',
        'SA': 'South Africa',
        'ZA': 'South Africa',
        'UK': 'United Kingdom',
        'U.K.': 'United Kingdom',
        'United Kingdom': 'United Kingdom',
        'USA': 'United States',
        'United States': 'United States'
    }
    
    df['country'] = df['country'].replace(country_mapping)
    
    print("\nCountry distribution after standardization:")
    print(df['country'].value_counts())
    
    return df


# =============================================================================
# STEP 9: STATE STANDARDIZATION
# =============================================================================

def standardize_state(df):
    """
    Standardize state/province names.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with standardized state values
    """
    print("\n" + "=" * 70)
    print("STEP 9: STATE STANDARDIZATION")
    print("=" * 70)
    
    state_mapping = {
        'KZN': 'KwaZulu-Natal',
        'KwaZulu-Natal': 'KwaZulu-Natal',
        'Western Cape': 'Western Cape',
        'Gauteng': 'Gauteng',
        'Limpopo': 'Limpopo'
    }
    
    df['state'] = df['state'].replace(state_mapping)
    
    print("\nState distribution after standardization:")
    print(df['state'].value_counts())
    
    return df


# =============================================================================
# STEP 10: EMAIL VALIDATION
# =============================================================================

def validate_emails(df):
    """
    Validate email addresses using regex pattern.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with email_valid column added
    """
    print("\n" + "=" * 70)
    print("STEP 10: EMAIL VALIDATION")
    print("=" * 70)
    
    # Basic email pattern: contains @ and at least one dot after @
    email_pattern = r'.+@.+\..+'
    
    df['email_valid'] = df['email'].str.match(email_pattern, na=False)
    
    invalid_emails = df[~df['email_valid']]
    
    print(f"\n✗ Number of invalid emails: {len(invalid_emails)}")
    
    if len(invalid_emails) > 0:
        print("\nSample invalid email records:")
        print(invalid_emails[['employee_id', 'first_name', 'last_name', 'email']].head(10))
    
    return df


# =============================================================================
# STEP 11: FIX NEGATIVE SALARIES
# =============================================================================

def fix_negative_salaries(df):
    """
    Convert negative salaries to absolute values.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with corrected salary values
    """
    print("\n" + "=" * 70)
    print("STEP 11: FIX NEGATIVE SALARIES")
    print("=" * 70)
    
    negative_salaries = df[df['salary'] < 0]
    
    print(f"\n✗ Number of negative salaries: {len(negative_salaries)}")
    
    if len(negative_salaries) > 0:
        print("\nNegative salary records:")
        print(negative_salaries[['employee_id', 'first_name', 'last_name', 'salary']])
        
        # Convert to absolute value
        df['salary'] = df['salary'].abs()
        
        print("\n✓ Negative salaries fixed (converted to absolute values)")
    
    return df


# =============================================================================
# STEP 12: VALIDATE DATE LOGIC
# =============================================================================

def validate_dates(df):
    """
    Check for and fix invalid date logic (exit_date before hire_date).
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with corrected date values
    """
    print("\n" + "=" * 70)
    print("STEP 12: VALIDATE DATE LOGIC")
    print("=" * 70)
    
    invalid_dates = df[df['exit_date'] < df['hire_date']]
    
    print(f"\n✗ Records with exit_date before hire_date: {len(invalid_dates)}")
    
    if len(invalid_dates) > 0:
        print("\nInvalid date records:")
        print(invalid_dates[['employee_id', 'first_name', 'last_name', 'hire_date', 'exit_date']])
        
        # Set invalid exit dates to NaN
        df.loc[df['exit_date'] < df['hire_date'], 'exit_date'] = pd.NaT
        
        print("\n✓ Invalid exit dates set to NaN")
    
    return df


# =============================================================================
# STEP 13: CHECK MISSING VALUES
# =============================================================================

def analyze_missing_values(df):
    """
    Analyze and report on missing values in the dataset.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
    """
    print("\n" + "=" * 70)
    print("STEP 13: MISSING VALUES ANALYSIS")
    print("=" * 70)
    
    print("\nMissing Values Summary:")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    
    print("\nMissing Value Decisions:")
    print("- exit_date: Left as NaN for active employees (expected)")
    print("- manager_id: Left as NaN (some employees don't have managers)")
    print("- performance_score: Left as NaN (not all employees have been evaluated)")
    print("- state/city: Left as NaN (incomplete location data)")


# =============================================================================
# STEP 14: REMOVE DUPLICATES
# =============================================================================

def remove_duplicates(df):
    """
    Identify and remove duplicate employee records.
    
    Parameters:
    -----------
    df : DataFrame
        Input dataframe
        
    Returns:
    --------
    df : DataFrame
        DataFrame with duplicates removed
    """
    print("\n" + "=" * 70)
    print("STEP 14: REMOVE DUPLICATE RECORDS")
    print("=" * 70)
    
    print(f"\n✗ Duplicate employee_ids: {df['employee_id'].duplicated().sum()}")
    
    if df['employee_id'].duplicated().sum() > 0:
        duplicates = df[df.duplicated(subset=['employee_id'], keep=False)]
        print(f"\nFound {len(duplicates)} duplicate records")
        print("\nDuplicate employee IDs:")
        print(duplicates[['employee_id', 'first_name', 'last_name']].sort_values('employee_id'))
        
        # Remove duplicates, keeping first occurrence
        initial_count = len(df)
        df = df.drop_duplicates(subset=['employee_id'], keep='first')
        final_count = len(df)
        
        print(f"\n✓ Removed {initial_count - final_count} duplicate records")
        print(f"✓ Final dataset size: {df.shape}")
    
    return df


# =============================================================================
# STEP 15: FINAL DATA QUALITY REPORT
# =============================================================================

def generate_quality_report(df):
    """
    Generate final data quality report.
    
    Parameters:
    -----------
    df : DataFrame
        Cleaned dataframe
    """
    print("\n" + "=" * 70)
    print("FINAL DATA QUALITY REPORT")
    print("=" * 70)
    
    print(f"\nTotal Records: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]}")
    
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print(f"\nInvalid Emails: {(~df['email_valid']).sum()}")
    print("Negative Salaries: Fixed (converted to absolute)")
    print("Duplicate Records: Removed")
    print("Date Logic Issues: Fixed")
    
    print("\nStandardized Categories:")
    print(f"- Departments: {df['department'].nunique()} unique values")
    print(f"- Currencies: {df['currency'].nunique()} unique values")
    print(f"- Countries: {df['country'].nunique()} unique values")
    print(f"- Gender: {df['gender'].nunique()} unique values")


# =============================================================================
# STEP 16: EXPORT CLEANED DATA
# =============================================================================

def export_cleaned_data(df, output_path):
    """
    Export cleaned data to CSV file.
    
    Parameters:
    -----------
    df : DataFrame
        Cleaned dataframe
    output_path : str or Path
        Path to save the cleaned CSV file
    """
    print("\n" + "=" * 70)
    print("STEP 16: EXPORT CLEANED DATA")
    print("=" * 70)
    
    output_path = Path(output_path)
    
    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Drop temporary validation column before export
    df_export = df.drop(columns=['email_valid'], errors='ignore')
    
    # Export to CSV
    df_export.to_csv(output_path, index=False)
    
    print(f"\n✓ Cleaned data saved to: {output_path}")
    print(f"✓ Exported {len(df_export)} rows and {len(df_export.columns)} columns")


# =============================================================================
# MAIN EXECUTION FUNCTION
# =============================================================================

def main():
    """
    Main function to execute the complete data cleaning pipeline.
    """
    print("\n" + "=" * 70)
    print("EMPLOYEE DATA CLEANING PIPELINE")
    print("=" * 70)
    print("\nThis script will clean the employee data through multiple steps:")
    print("1. Load data")
    print("2. Explore initial data quality")
    print("3. Clean strings (trim, case standardization)")
    print("4. Convert data types")
    print("5-9. Standardize categories (gender, department, currency, country, state)")
    print("10. Validate email addresses")
    print("11. Fix negative salaries")
    print("12. Validate date logic")
    print("13. Analyze missing values")
    print("14. Remove duplicates")
    print("15. Generate quality report")
    print("16. Export cleaned data")
    print("\n")
    
    # Define file paths
    # Adjust these paths based on your project structure
    input_file = "../data/raw/Week-3-Employee-Data.xlsx"
    output_file = "../data/cleaned/employee_data_cleaned.csv"
    
    # Execute cleaning pipeline
    try:
        # Step 1: Load data
        df = load_data(input_file)
        
        # Step 2: Initial exploration
        explore_data(df)
        
        # Step 3: Clean strings
        df = clean_strings(df)
        
        # Step 4: Convert data types
        df = convert_data_types(df)
        
        # Step 5: Standardize gender
        df = standardize_gender(df)
        
        # Step 6: Standardize department
        df = standardize_department(df)
        
        # Step 7: Standardize currency
        df = standardize_currency(df)
        
        # Step 8: Standardize country
        df = standardize_country(df)
        
        # Step 9: Standardize state
        df = standardize_state(df)
        
        # Step 10: Validate emails
        df = validate_emails(df)
        
        # Step 11: Fix negative salaries
        df = fix_negative_salaries(df)
        
        # Step 12: Validate dates
        df = validate_dates(df)
        
        # Step 13: Analyze missing values
        analyze_missing_values(df)
        
        # Step 14: Remove duplicates
        df = remove_duplicates(df)
        
        # Step 15: Generate quality report
        generate_quality_report(df)
        
        # Step 16: Export cleaned data
        export_cleaned_data(df, output_file)
        
        print("\n" + "=" * 70)
        print("DATA CLEANING COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        print("\nPlease check:")
        print("1. Input file path is correct")
        print("2. Input file exists and is readable")
        print("3. Output directory has write permissions")
        raise


# =============================================================================
# SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()
