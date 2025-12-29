import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/Mian Mohsin/Desktop/data_project/dirty_cafe_sales.csv')

# Clean column names
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(r"\s+", "_", regex=True)
    .str.replace(r"[^\w]", "", regex=True)
)

#convert Unknown or error values into NaN
df.replace(['UNKNOWN', 'ERROR', ''], np.nan, inplace=True)

# Convert required columns to numeric
numeric_cols= ['quantity','price_per_unit','total_spent']
for col in numeric_cols:
    df[col]=pd.to_numeric(df[col], errors='coerce')

# Identify rows with invalid total_spent values
invalid_spents=df[
    df['quantity'].notna() &
    df['price_per_unit'].notna() &
    df['total_spent'].notna()&
    (df['total_spent']!=df['quantity']*df['price_per_unit']) 
]
# print(invalid_spents.shape[0],'rows with invalid total_spent found.')

# Recalculate total_spent for those rows
mask=(
    df['quantity'].notna() &
    df['price_per_unit'].notna() &
    (df['total_spent'].isna()|
    (df['total_spent']!=df['quantity']*df['price_per_unit']))
)

df.loc[mask,'total_spent'] = df.loc[mask,'quantity'] * df.loc[mask,'price_per_unit']

# print(df['total_spent'].isna().sum(),'rows with NaN total_spent after cleaning.')

# drop rows with any remaining NaN values in total_spent columns
df=df.dropna(subset=['total_spent'])
# print(df['total_spent'].isna().sum(),'rows with NaN total_spent after dropping rows with NaN values.')

# Clean categorical columns
cat_col=['item','payment_method','location']
for col in cat_col:
    df[col]=(
        df[col]
        .str.title()
        .str.strip()
        .fillna('Unknown')
        
    )

# Convert transaction_date to datetime
df['transaction_date']=pd.to_datetime(df['transaction_date'], errors='coerce')

# save cleaned data to new CSV file
df.to_csv('C:/Users/Mian Mohsin/Desktop/data_project/clean_cafe_sales.csv', index=False)

