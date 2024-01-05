import os
import pandas as pd

def update_column_names(file_path, column_mapping):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Display the current column names
    print("Current Column Names:")
    print(df.columns)

    # Update the column names based on the provided mapping
    for old_name, new_name in column_mapping.items():
        if old_name in df.columns:
            df.rename(columns={old_name: new_name}, inplace=True)
        else:
            print(f"Column '{old_name}' not found in the DataFrame.")

    # Display the updated DataFrame with new column names
    print("\nUpdated DataFrame with New Column Names:")
    print(df)

    # Save the updated DataFrame to a new Excel file
    dir_path, file_name = os.path.split(file_path)
    new_file_path = os.path.join(dir_path, "updated_" + file_name)
    df.to_excel(new_file_path, index=False)
    print(f"\nUpdated Excel file saved at: {new_file_path}")

# Specify the path to the Excel file
excel_file_path = r'C:\Users\91910\Documents\internship\Excel_to_sql\2017\Jan-2017.xlsx'

# Specify the column mapping (old_name: new_name)
column_mapping = {
    'Sr. No': 'SR_NO',
    'Bank Name': 'BANK_NAME',
    'On-site': 'NO_ATM_ONSITE_CNT',
    'Off-site': 'NO_ATM_OFFSITE_CNT',
    'On-line': 'On_line_POS',
    'NO_POS_CNT': 'NO_POS_CNT'
    'No .of outstanding cards as at the end of the month': 'No_OCEM_CC'
    '': 'BANK_NAME'
    # Add more columns as needed
}

update_column_names(excel_file_path, column_mapping)
