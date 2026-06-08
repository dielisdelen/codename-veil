from pypdf import PdfReader
reader = PdfReader("test.pdf")
text = reader.pages[0].extract_text()
text = text.replace("Jansen", "[REDACTED]")
with open("output.txt", "w") as f:
    f.write(text)
print(text)