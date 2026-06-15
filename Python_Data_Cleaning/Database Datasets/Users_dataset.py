import pandas as pd

# 1. Load the data
df = pd.read_csv('vitals360_cleaned_data.csv')

# 2. Duplicate hatana (UserID ka pehla instance rakhna)
df_unique = df.drop_duplicates(subset=['UserID'], keep='first').copy()

# 3. BMI Calculate karna aur 2 decimal places tak round karna
# .round(2) function use kiya hai rounding ke liye
df_unique['BMI'] = (df_unique['WeightKg'] / (df_unique['HeightM'] ** 2)).round(2)

# 4. Result save karna (Sirf zaroori columns)
output_columns = ['UserID', 'Age', 'Gender', 'HeightM', 'WeightKg', 'BMI']
df_unique[output_columns].to_csv('vitals360_with_bmi_unique.csv', index=False)

print("Bhai, BMI round ho gaya aur duplicates khatam!")
print(df_unique[output_columns].head())
