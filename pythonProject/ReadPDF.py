"""
Program to Extract and Filter Data from the First Column of an Excel Sheet
This script reads an Excel file containing stock data, processes the first column, 
and identifies rows containing a specific keyword (e.g., 'berkshire').
"""

import xlrd  # Library to read data from Excel files

# Specify the path to the Excel file
loc = "Stocks.xls"

# Open the Excel workbook
wb = xlrd.open_workbook(loc)

# Access the first sheet in the workbook
sheet = wb.sheet_by_index(0)

# Access the value of the first cell in the first column for validation
sheet.cell_value(0, 0)

def print_rownumber(row):
    """
    Prints the row number and the values from the first and second columns of the specified row.

    Args:
        row (int): The row index to process.
    """
    print(f"Row number: {row}")
    print(f"Stock Name: {sheet.cell_value(row, 0)}")
    print(f"Additional Data: {sheet.cell_value(row, 1)}")  # Modify column index as needed

# Iterate through all rows in the sheet
for i in range(sheet.nrows):
    s = sheet.cell_value(i, 0)  # Extract the value from the first column
    Stock_names = s.lower()  # Convert to lowercase for case-insensitive comparison
    
    # Check if the keyword 'berkshire' exists in the stock name
    if "berkshire" in Stock_names:
        print_rownumber(i)  # Print the row details if the condition is met
