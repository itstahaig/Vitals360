import pandas as pd
import numpy as np

# 1. Load your chosen dataset
# We use try-except to handle potential file name issues
try:
    df = pd.read_csv("Activity.csv")
    print(f"✅ Loaded 'Activity.csv' with {len(df)} rows.")
except FileNotFoundError:
    print("❌ Error: Could not find 'Activity.csv'. Make sure it is in the same folder.")
    exit()

# 2. Rename columns to match Vitals360 requirements
# We map the columns from your file to the standard names we need
df.rename(columns={
    'Steps': 'DailySteps',
    'Calories_Burned': 'Calories',
    'Very_Active_Minutes': 'ActiveMinutes',
    'Fairly_Active_Minutes': 'ExerciseMinutes'
}, inplace=True)

print("Columns renamed to standard Vitals360 format.")

# 3. Data Enrichment (Adding missing Vitals)
# Your dataset doesn't have Weight/Height/Posture, so we simulate them.
# This is valid for a student project to demonstrate "Data Development".

np.random.seed(42) # Ensures the random numbers stay the same every time you run it

# Generate Weight (between 55kg and 95kg)
df['WeightKg'] = np.random.randint(55, 95, size=len(df))

# Generate Height (between 1.60m and 1.90m)
df['HeightM'] = np.round(np.random.uniform(1.60, 1.90, size=len(df)), 2)

# Generate Posture Score (0-100)
# Logic: People with more steps likely have slightly better posture on average
df['PostureScore'] = np.random.randint(60, 90, size=len(df))
# Add a small bonus for active people (capped at 100)
df.loc[df['DailySteps'] > 8000, 'PostureScore'] += 5
df['PostureScore'] = df['PostureScore'].clip(upper=100)

# 4. Calculate BMI (Body Mass Index)
# Formula: Weight / Height^2
df['BMI'] = round(df['WeightKg'] / (df['HeightM'] ** 2), 2)

# 5. Final Selection & Save
# We only keep the columns we need for the Database
required_columns = [
    'UserID', 'WeightKg', 'HeightM', 'DailySteps', 
    'ActiveMinutes', 'ExerciseMinutes', 'Calories', 'PostureScore', 'BMI'
]

# Create the final clean dataframe
df_clean = df[required_columns]

# Save to new CSV
df_clean.to_csv("cleaned_activity_data.csv", index=False)

print("\n✅ Data cleaning complete!")
print("File saved as: 'cleaned_activity_data.csv'")
print("-" * 30)
print(df_clean.head())
