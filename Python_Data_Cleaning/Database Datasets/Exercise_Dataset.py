import pandas as pd
df = pd.read_csv('vitals360_cleaned_data.csv')

# Sirf wo rows jahan Exercise type mention hai
df_exercise = df.dropna(subset=['ExerciseType']).copy()

cols = ['UserID', 'ExerciseType', 'ExerciseDurationMinutes']
df_exercise[cols].to_csv('Exercise_Log.csv', index=False)
print("Exercise Log ready!")
