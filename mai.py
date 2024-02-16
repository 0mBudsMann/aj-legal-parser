import re
from PyPDF2 import PdfReader


regex_pattern = re.compile(r"[’“”]")

reader = PdfReader("VKR.pdf")
count = len(reader.pages)

with open("output.txt", "w") as f:
    for i in range(count):
        page = reader.pages[i]

        text = page.extract_text()


        text = regex_pattern.sub(lambda x: {
            '‘':"'",
            '’': "'",
            '“': '"',
            '”': '"'
        }[x.group(0)], text)


        print(text, file=f)
