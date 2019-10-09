import openpyxl
import csv
import xlrd

#load workbook
wk = openpyxl.load_workbook("Sample form.xlsx")
#FIND SHEETS
print(wk.sheetnames)