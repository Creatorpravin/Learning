from csv import writer
from operator import index
import tabula
from PIL import Image
import numpy as np
import pytesseract


def image_to_text(filename):
    
    img1 = np.array(Image.open(filename))
    
    return pytesseract.image_to_string(img1)

if __name__ == "__main__":
    #print(type(image_to_text("test.png")))
    #print(image_to_text("address.pdf"))
    print(image_to_text("demo.png"))
    print("="*50)
    datafile = image_to_text("bankdetails.png")
    print(datafile)
    li=list(datafile.split("\n"))
    print(li)
    li.to_excel(writer,'/home/praveen/Learning/python/Rough_task/image/saddress.xlsx',index=False)
# data_file = tabula.read_pdf("address.pdf", pages=1)
# #print(type(data_file))
# print(data_file)



#tabula.convert_into("address.pdf", "test_s.csv", output_format="csv")

# df = tabula.read_pdf("/home/praveen/Learning/python/Rough_task/image/address.pdf", encoding='utf-8', pages=1)
# print(df)
# # importing required modules 
# import PyPDF2 
    
# # creating a pdf file object 
# pdfFileObj = open('TE40E-000129_R00.pdf', 'rb') 
    
# # creating a pdf reader object 
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# # printing number of pages in pdf file 
# print(pdfReader.numPages) 
    
# # creating a page object 
# pageObj = pdfReader.getPage(0) 
    
# # extracting text from page 
# print(pageObj.extractText()) 
    
# # closing the pdf file object 
# pdfFileObj.close() 

# import pdftables_api

# c = pdftables_api.Client('my-api-key')
# c.xlsx('TE40E-000129_R00.pdf', 'output')

