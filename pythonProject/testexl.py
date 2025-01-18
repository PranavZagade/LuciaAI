"""
This script reads data from an Excel file (`Email.xls`) using the `xlrd` library.
It iterates through all rows in the sheet and prints the data along with its location
in the row-column format.
"""

import xlrd  # Import the xlrd library for reading Excel files

# Define the path to the Excel file
loc = ("Email.xls")  # Replace with the path to your file if not in the same directory

# Open the Excel workbook
wb = xlrd.open_workbook(loc)  # Load the workbook into memory

# Select the first sheet by index (0 for the first sheet)
sheet = wb.sheet_by_index(0)  # Access the first sheet of the workbook

# Read the value from the top-left cell (row 0, column 0)
# This demonstrates how to fetch a specific cell value
print(sheet.cell_value(0, 0))  # Prints the value of the first cell (Row 0, Column 0)

# Iterate through all rows in the sheet
for row in range(sheet.nrows):  # `sheet.nrows` gives the total number of rows in the sheet
    # Print the current row and column locations
    print(f"(Row, Col) = ({row},0) \t\t\t (Row, Col) = ({row},1)")
    
    # Print the data from the first and second columns of the current row
    print(sheet.cell_value(row, 0) + "\t\t\t" + sheet.cell_value(row, 1))
    
    # Incrementing `row` is unnecessary in the loop, as `for` automatically handles this

# Note:
# - `sheet.cell_value(row, col)` retrieves the value from a specific cell (row, col).
# - The script assumes that the file `Email.xls` exists and has at least two columns.
