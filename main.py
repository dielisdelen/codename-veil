import re
from pypdf import PdfReader
reader = PdfReader("test.pdf")
text = reader.pages[0].extract_text()
text = text.replace("Jansen", "[REDACTED]")

def redact_nine_digit_numbers(text):
    return re.sub(r"\b\d{9}\b", "[REDACTED]", text)

text = redact_nine_digit_numbers(text)
with open("output.txt", "w") as f:
    f.write(text)
print(text)