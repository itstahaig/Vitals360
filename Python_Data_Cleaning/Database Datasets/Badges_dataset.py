import pandas as pd
df = pd.read_csv('vitals360_cleaned_data.csv')

# Sirf wo rows jahan Badge field khali nahi hai
df_badges = df.dropna(subset=['BadgeEarned']).copy()

cols = ['UserID', 'BadgeEarned', 'BadgeEarnedDate']
df_badges[cols].to_csv('Badges_Log.csv', index=False)
print("Badges Log ready!")
