import re

def extract_phone_numbers(string):
    # Regular expression to extract phone numbers 
    phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
    phone_numbers = re.findall(phone_pattern, string)
    return phone_numbers

def extract_email_addresses(string):
    # Regular expression to extract email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_addresses = re.findall(email_pattern, string)
    return email_addresses

def replace_email_addresses(string, replacement):
    # Regular expression to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Replace email addresses with the replacement string
    result = re.sub(email_pattern, replacement, string)
    return result

string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"

phoneno = extract_phone_numbers (string)
emailad = extract_email_addresses ( string)
replacement = 'info@notexample.com'
replacemail = replace_email_addresses (string,replacement)

print (phoneno)
print (emailad)
print (replacemail)