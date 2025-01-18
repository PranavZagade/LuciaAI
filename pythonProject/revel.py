"""
This script reads data from an Excel file (`Email.xls`), searches for a specific name, 
and retrieves the associated email address from the same row. 
If the name is found, the email is passed to another function for further processing.
"""

import xlrd  # Library for reading Excel files

# Specify the path to the Excel file
loc = "Email.xls"

# Open the Excel workbook and access the first sheet
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)  # Access the first sheet in the workbook

# The name to search for in the Excel file
name = "sarvesh"

# Access a specific cell to verify the sheet structure
sheet.cell_value(0, 0)

def get_rownumber(row):
    """
    Retrieves the email address from the specified row.
    
    Args:
        row (int): The row index to retrieve the email address from.
    
    Returns:
        str: The email address from the specified row.
    """
    print(f"Row number: {row}")
    email = sheet.cell_value(row, 1)  # Retrieve the email from column 1 (second column)
    return email

def test(email):
    """
    Dummy function to simulate processing the email address.

    Args:
        email (str): The email address to process.
    """
    print("From function:")
    print(f"Email: {email}")

# Iterate through each row in the Excel sheet
for i in range(sheet.nrows):
    r = sheet.cell_value(i, 0)  # Retrieve the name from the first column
    nameList = r.lower()  # Convert to lowercase for case-insensitive comparison
    count = 0  # To ensure the block runs only once per match

    # Check if the target name exists in the current row
    if name in nameList:
        while True:  # Loop to simulate one-time execution
            if count == 0:
                value = get_rownumber(i)  # Get the email from the matched row
                test(value)  # Pass the email to the test function
                count = 1  # Prevent further iterations
                exit()  # Exit the script after processing the first match

# Placeholder for a future function to send an email
# def send_mail(subject, message, emailid, name):
