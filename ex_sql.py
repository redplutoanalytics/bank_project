import pandas as pd

# Replace 'your_file.xlsx' with the actual Excel file path
file_path = r'filepath'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Remove the first 6 rows
df = df.iloc[6:]

# Create a new row at position 1 with column names from B to Q
new_column_names = ['SR_NO', 'BANK_NAME', 'NO_ATM_ONSITE', 'NO_ATM_OFFSITE',
                    'On_line_POS', 'No_POS_CNT', 'CC_NO_OS_EM', 'CC_NO_TA_ATM',
                    'CC_NO_TA_POS', 'CC_AOT_ATM', 'CC_AOT_POS', 'DD_NO_OS_EM',
                    'DD_NO_TA_ATM', 'DD_NO_TA_POS', 'DD_AOT_ATM', 'DD_AOT_POS']

# Update column names
df.columns = new_column_names

# Reset the index after removing rows
df.reset_index(drop=True, inplace=True)

# Specify the new file path
new_file_path = r'filepath-new'

# Save the updated DataFrame to a new Excel file
df.to_excel(new_file_path, index=False)

print(f"Script executed successfully. Updated file saved at: {new_file_path}")
