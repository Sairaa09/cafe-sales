# Cleaned Cafe Sales Dataset

## Overview
This dataset contains cleaned sales records from a cafe. The raw data included missing values, invalid entries, and inconsistent formatting. The cleaning process ensures the dataset is reliable and ready for analysis.

## Cleaning Steps
1. Standardized column names: lowercase, no spaces or special characters.  
2. Replaced 'UNKNOWN', 'ERROR', and blank values with `NaN`.  
3. Converted numeric columns (`quantity`, `price_per_unit`, `total_spent`) to numeric types.  
4. Identified and corrected invalid `total_spent` values using `quantity * price_per_unit`.  
5. Dropped rows with remaining `NaN` in `total_spent`.  
6. Cleaned categorical columns (`item`, `payment_method`, `location`) with title case and filled missing values as "Unknown".  
7. Converted `transaction_date` to datetime format.

## Columns
- `transaction_id` (numeric/string)  
- `item` (string)  
- `quantity` (numeric)  
- `price_per_unit` (numeric)  
- `total_spent` (numeric)  
- `payment_method` (string)  
- `location` (string)  
- `transaction_date` (datetime)

## Summary
- Missing values in critical columns handled.  
- Dataset ready for analysis, visualization, and reporting.

