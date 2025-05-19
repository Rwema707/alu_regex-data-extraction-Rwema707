import re

def extract_emails(data):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, data)

def extract_phone_numbers(data):
    pattern = r'(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, data)

def extract_urls(data):
    pattern = r'https?://(?:www\.)?[^\s]+\.[^\s]+'
    return re.findall(pattern, data)

def extract_dates(data):
    pattern = r'(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})'
    return re.findall(pattern, data)

def extract_currency(data):
    pattern = r'[$€£]\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, data)

if __name__ == "__main__":
    with open("sample_data.txt", "r") as f:
        content = f.read()

    print("== Emails ==")
    print(extract_emails(content))

    print("== Phones ==")
    print(extract_phone_numbers(content))

    print("== URLs ==")
    print(extract_urls(content))

    print("== Dates ==")
    print(extract_dates(content))

    print("== Currency ==")
    print(extract_currency(content))

