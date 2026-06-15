import csv

print("--- Starting Data Cleaning ---")

# 1. Open the raw file to read
input_file = open('vitals360_raw_dataset.csv', 'r')
reader = csv.DictReader(input_file)

# 2. Open the new file to write
output_file = open('vitals360_cleaned_data.csv', 'w', newline='')
writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
writer.writeheader()

# Variables to keep track of numbers
total_rows = 0
saved_rows = 0

# We use this list to remember which users we have already seen to avoid duplicates
seen_users = []

# 3. Loop through every row in the dataset
for row in reader:
    total_rows = total_rows + 1

    # --- CHECK 1: REMOVE DUPLICATES ---
    # We create a unique ID string for this row
    unique_check = row['UserID'] + row['BadgeEarnedDate'] + row['AlertTriggeredDate']

    if unique_check in seen_users:
        continue  # Skip this loop because we have seen this record before

    seen_users.append(unique_check)  # Add to list so we remember it

    # --- CHECK 2: REMOVE EMPTY NAMES OR IDs ---
    if row['Name'] == "" or row['UserID'] == "":
        continue

    # --- CHECK 3: FIX IMPOSSIBLE NUMBERS ---
    # We convert text to numbers to check them
    try:
        age = int(row['Age'])
        weight = int(row['WeightKg'])
        height = float(row['HeightM'])
    except:
        continue  # If the number is broken (like text), skip the row

    # Logic: Age must be realistic (between 10 and 100)
    if age < 10 or age > 100:
        continue

    # Logic: Weight must be realistic
    if weight < 30 or weight > 300:
        continue

    # Logic: Height must be realistic
    if height < 1.0 or height > 2.5:
        continue

    # --- CHECK 4: FIX GENDER TEXT ---
    # Change "m", "male", "Maleee" to just "Male"
    gender_text = row['Gender'].lower()  # make it small letters

    if "f" in gender_text:
        row['Gender'] = "Female"
    elif "m" in gender_text:
        row['Gender'] = "Male"
    else:
        continue  # If we can't tell the gender, skip the row

    # --- CHECK 5: FIX ALERTS ---
    # Change "y", "1", "true" to "Yes"
    alert_text = row['AlertTriggered'].lower()

    if "y" in alert_text or "1" in alert_text or "true" in alert_text:
        row['AlertTriggered'] = "Yes"
    else:
        row['AlertTriggered'] = "No"

    # --- SAVE THE ROW ---
    # If the code gets here, the row is clean and good
    writer.writerow(row)
    saved_rows = saved_rows + 1

# 4. Close the files
input_file.close()
output_file.close()

print("Cleaning Finished!")
print("Total Rows Read: " + str(total_rows))
print("Rows Saved: " + str(saved_rows))