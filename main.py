import os
import re
from PyPDF2 import PdfReader
regex_pattern = re.compile(r"[’“”]")

def is_pdf(filename):
    return filename[-3:].lower() == 'pdf'

path="./Files"
#print(os.listdir(path))
dir_list=(os.listdir(path))

for dir in dir_list:
    files=os.listdir(path+"/"+dir)
    for pdf_names in files:
        if (is_pdf((path + "/" + dir + "/" + pdf_names)) == False):
            continue
        letters_before_pdf = pdf_names.split(".pdf")[0]
        print(path+"/"+dir+"/"+pdf_names)
        reader = PdfReader(path+"/"+dir+"/"+pdf_names)
        count = len(reader.pages)
       # f=open(path+"/"+dir+"/"+letters_before_pdf+".txt","x")
        #f=open(path+"/"+dir+"/")
        with open(path+"/"+dir+"/"+letters_before_pdf+".txt", "w") as f:
            for i in range(count):
                page = reader.pages[i]

                text = page.extract_text()

                text = regex_pattern.sub(lambda x: {
                    '‘': "'",
                    '’': "'",
                    '“': '"',
                    '”': '"'
                }[x.group(0)], text)

                print(text, file=f)



