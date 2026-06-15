import pandas as pd
df = pd.read_csv('vitals360_cleaned_data.csv')

# Sirf activity se related columns uthayein
cols = ['UserID', 'Avg DailySteps', 'Avg ActiveMinutes', 'Avg ExerciseMinutes', 'Avg Calories Burned']
df_activity = df[cols].copy()

# Save as CSV
df_activity.to_csv('Activity_Log.csv', index=False)
print("Activity Log file ready with all instances!")
