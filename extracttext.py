from PyPDF2 import PdfReader

reader = PdfReader('1. Matter in Our Surroundings.pdf')

print(len(reader.pages))

for page in reader.pages:
    text = page.extract_text()
    print(text)
