# # Import Module
# import pdftables_api
  
# # API KEY VERIFICATION
# conversion = pdftables_api.Client('API KEY')
  
# # PDf to Excel 
# # (Hello.pdf, Hello)
# conversion.xlsx("address.pdf", "address.xlsx")


# Import Module 
import tabula
from tabula.io import read_pdf
  
# Read PDF File
# this contain a list
df = read_pdf("/home/praveen/Learning/python/Rough_task/image/address.pdf", pages = 1)
print(df)
# Convert into Excel File
df.to_excel('/home/praveen/Learning/python/Rough_task/image/saddress.xlsx')