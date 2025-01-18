# Reading and Printing Data from an Excel File Using xlrd
# This script reads an Excel file (Email.xls) and prints the content of the first sheet,
# displaying values from column 0 and column 1 for each row.

import xlrd  # Import the xlrd library for working with Excel files

# Path to the Excel file
loc = "Email.xls"

# Open the workbook
wb = xlrd.open_workbook(loc)

# Select the first sheet (index 0)
sheet = wb.sheet_by_index(0)

# Access a specific cell value (e.g., cell at row 0, column 0)
sheet.cell_value(0, 0)

# Iterate through all rows and print data from column 0 and column 1
for row in range(sheet.nrows):
    # Print row and column information along with the cell values
    print("(Row, Col) = (" + str(row) + ", 0) \t\t\t" + "(Row, Col) = (" + str(row) + ", 1)")
    print(sheet.cell_value(row, 0) + "\t\t\t" + sheet.cell_value(row, 1))
