import pandas as pd

# Step 1: Load the dataset
file_path = r"C:\Users\Maruf Ajimati\Documents\Nexford Assignments\BAN6800 Business Analytics Capstone\Milestone 1\WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

# Step 2: Remove rows with missing values in TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)

# Step 3: Reset index after drop
df.reset_index(drop=True, inplace=True)

# Step 4: Create new features
df['AvgChargesPerMonth'] = df['TotalCharges'] / df['tenure']
df['IsSenior'] = df['SeniorCitizen'].apply(lambda x: 1 if x == 1 else 0)

# Step 5: Preview data
print("Data after cleaning and feature engineering:")
print(df.head())

# Step 6: Save cleaned dataset
output_path = r"C:\Users\Maruf Ajimati\Documents\Nexford Assignments\BAN6800 Business Analytics Capstone\Milestone 1\python_telco\cleaned_telco.csv"
df.to_csv(output_path, index=False)

print(f"\n✅ Cleaned dataset saved to: {output_path}")
