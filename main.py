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

def redact_phone_numbers(text):
    # Dutch phone numbers: +31 / 0031 / 0 prefix, mobile and landline, optional spaces/dashes
    pattern = r"(?:\+31|0031|0)[\s-]?(?:\d[\s-]?){9}\b"
    return re.sub(pattern, "[REDACTED]", text)

def redact_email_addresses(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.sub(pattern, "[REDACTED]", text)

def redact_postal_codes(text):
    # Dutch postal code: 4 digits + 2 letters, optional space (e.g. 1234 AB)
    pattern = r"\b\d{4}\s?[A-Za-z]{2}\b"
    return re.sub(pattern, "[REDACTED]", text)

def redact_ibans(text):
    # Dutch IBAN: NL + 2 check digits + 4 letter bank code + 10 digits, optional spaces
    pattern = r"\bNL\d{2}\s?[A-Z]{4}(?:\s?\d){10}\b"
    return re.sub(pattern, "[REDACTED]", text)

text = redact_phone_numbers(text)
text = redact_ibans(text)
text = redact_nine_digit_numbers(text)
text = redact_license_plates(text)
text = redact_email_addresses(text)
text = redact_postal_codes(text)
with open("output.txt", "w") as f:
    f.write(text)
print(text)