import re
from pypdf import PdfReader
reader = PdfReader("test.pdf")
text = reader.pages[0].extract_text()
text = text.replace("Jansen", "[REDACTED]")

def redact_nine_digit_numbers(text):
    return re.sub(r"\b\d{9}\b", "[REDACTED]", text)

def redact_license_plates(text):
    pattern = r"\b(?:[A-Z]{2}-\d{2}-\d{2}|\d{2}-\d{2}-[A-Z]{2}|\d{2}-[A-Z]{2}-\d{2}|[A-Z]{2}-\d{2}-[A-Z]{2}|[A-Z]{2}-[A-Z]{2}-\d{2}|\d{2}-[A-Z]{2}-[A-Z]{2}|\d{2}-[A-Z]{3}-\d|\d-[A-Z]{3}-\d{2}|[A-Z]{2}-\d{3}-[A-Z]|[A-Z]-\d{3}-[A-Z]{2})\b"
    return re.sub(pattern, "[REDACTED]", text)

text = redact_nine_digit_numbers(text)
text = redact_license_plates(text)
with open("output.txt", "w") as f:
    f.write(text)
print(text)