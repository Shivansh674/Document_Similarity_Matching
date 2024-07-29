import re

def extract_features(text):
    keywords = re.findall(r'\b\w+\b', text)
    invoice_number = re.search(r'Invoice Number:\s*(\w+)', text)
    date = re.search(r'Date:\s*(\d{2}/\d{2}/\d{4})', text)
    amount = re.search(r'Amount:\s*\$([\d,]+\.\d{2})', text)
    return {
        'keywords': keywords,
        'invoice_number': invoice_number.group(1) if invoice_number else '',
        'date': date.group(1) if date else '',
        'amount': amount.group(1) if amount else ''
    }
