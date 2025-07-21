import re

def parse_text(text):
    result = {"vendor": None, "date": None, "amount": None, "category": None}

    vendor_match = re.search(r'(?:From|Vendor)[:\-]?\s*(.*)', text, re.IGNORECASE)
    date_match = re.search(r'(\d{2,4}[/-]\d{1,2}[/-]\d{2,4})', text)
    amount_match = re.search(r'(?:Total|Amount|TOTAL|Rs\.?|₹)?[\s:=₹$-]*([\d,]+\.\d{0,2})', text, re.IGNORECASE)

    if vendor_match:
        result['vendor'] = vendor_match.group(1).strip()
    if date_match:
        result['date'] = date_match.group(1)
    if amount_match:
        amt = amount_match.group(1).replace(",", "")
        try:
            result['amount'] = float(amt)
        except ValueError:
            result['amount'] = None

    if result['vendor']:
        v = result['vendor'].lower()
        if 'electricity' in v:
            result['category'] = 'Electricity'
        elif 'internet' in v:
            result['category'] = 'Internet'
        elif 'store' in v or 'mart' in v:
            result['category'] = 'Groceries'
        else:
            result['category'] = 'Other'

    return result
