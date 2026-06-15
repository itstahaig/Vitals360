import pandas as pd
df = pd.read_csv('vitals360_cleaned_data.csv')

cols = ['UserID', 'PostureScore', 'AlertTriggered', 'AlertTriggeredDate']
df_posture = df[cols].copy()

df_posture.to_csv('Posture_Log.csv', index=False)
print("Posture and Alerts Log ready!")
