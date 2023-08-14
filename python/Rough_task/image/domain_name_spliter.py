# # Import Module
# import pdftables_api

# # API KEY VERIFICATION
# conversion = pdftables_api.Client('API KEY')

# # PDf to Excel
# # (Hello.pdf, Hello)
# conversion.xlsx("address.pdf", "address.xlsx")


# # Import Module
# import tabula
# from tabula.io import read_pdf

# # Read PDF File
# # this contain a list
# df = read_pdf("/home/praveen/Learning/python/Rough_task/image/address.pdf", pages = 1)
# print(df)
# # Convert into Excel File
# # df.to_excel('/home/praveen/Learning/python/Rough_task/image/saddress.xlsx')
# import pandas as pd
# import pdfplumber
# from collections import namedtuple

# lines = []
# Line = namedtuple('Line', 'EmployeeCode Name Location Department Gender')


# def pdf_to_excel(pdf_file_path):

#     with pdfplumber.open(pdf_file_path) as pdf:
#         for pages in pdf.pages:
#             text = pages.extract_text()
#             for line in text.split("\n"):
#                 if line.startswith("YT"):
#                     li = line.split(" ")
#                     lines.append(Line(*li))

#     df = pd.DataFrame(lines)
#     # print(df.head())
#     df.to_csv('test.csv', index=False)


# if __name__ == "__main__":
#     pdf_to_excel(
#         "/home/praveen/Learning/python/Rough_task/image/Employee_details.pdf")
    
def text_to_pdf(file_to_extract):
    with open(file_to_extract, 'r') as text_file:
      content = text_file.read()      
    domain_list = content.split('\n')  
    
    for i in range(0, len(domain_list), 5):                   
        print(','.join(domain_list[i:i+5]))
        
  
text_to_pdf("youtube.txt")

# domain_names = (
#     "youtube.com.lb,youtube.com.lv,youtube.com.ly,youtube.com.mk,youtube.com.mt,youtube.com.mx,youtube.com.my,youtube.com.ng,youtube.com.ni,youtube.com.om,youtube.com.pa,youtube.com.pe,youtube.com.ph,youtube.com.pk,youtube.com.pt,youtube.com.py,youtube.com.qa,youtube.com.ro,youtube.com.sa,youtube.com.sg,youtube.com.sv,youtube.com.tn,youtube.com.tr,youtube.com.tw,youtube.com.ua,youtube.com.uy,youtube.com.ve,youtube.co.nz,youtube.co.th,youtube.co.tz,youtube.co.ug,youtube.co.uk,youtube.co.ve,youtube.co.za,youtube.co.zw,youtube.cr,youtube.cz,youtube.de,youtube.dk,youtubeeducation.com,youtube.ee,youtubeembeddedplayer.googleapis.com,youtube.es,youtube.fi,youtube.fr,youtube.ge,youtube.googleapis.com,youtube.gr,youtube.gt,youtube.hk,youtube.hr,youtube.hu,youtube.ie,youtubei.googleapis.com,youtube.in,youtube.iq,youtube.is,youtube.it,youtube.jo,youtube.jp,youtubekids.com,youtube.kr,youtube.kz,youtube.la,youtube.lk,youtube.lt,youtube.lu,youtube.lv,youtube.ly,youtube.ma,youtube.md,youtube.me,youtube.mk,youtube.mn,youtube.mx,youtube.my,youtube.ng,youtube.ni,youtube.nl,youtube.no,youtube-nocookie.com,youtube.pa,youtube.pe,youtube.ph,youtube.pk,youtube.pl,youtube.pr,youtube.pt,youtube.qa,youtube.ro,youtube.rs,youtube.ru,youtube.sa,youtube.se,youtube.sg,youtube.si,youtube.sk,youtube.sn,youtube.soy,youtube.sv,youtube.tn,youtube.tv,youtube.ua,youtube.ug,youtube-ui.l.google.com,youtube.uy,youtube.vn,yt3.ggpht.com,yt.be,ytimg.com,ytimg.l.google.com,ytkids.app.goo.gl,yt-video-upload.l.google.com"
# )

# Split the domain names using a comma delimiter
# domain_list = domain_names.split(',')

# # Print five domain names per line
# for i in range(0, len(domain_list), 5):
#     print(','.join(domain_list[i:i+5]))