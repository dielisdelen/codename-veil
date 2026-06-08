from pypdf import PdfReader
reader = PdfReader("test.pdf")
text = reader.pages[0].extract_text()
print(text)