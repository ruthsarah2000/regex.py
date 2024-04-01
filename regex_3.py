'''
Problem Statement:
Develop a script to extract specific information from a formatted text. The text contains data entries delimited by semicolons and formatted 
as 'Key: Value'. Extract the value corresponding to a specific key.
'''

import re

def extract_value(text, key):
    pattern = r'{}: (.*?);'.format(re.escape(key))  
    match = re.search(pattern, text)  
    if match:
        return match.group(1)  
    else:
        return None  
text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key = "Occupation"
occupation = extract_value(text, key)
print(f"{key}: {occupation}")

'''
Problem Statement:
Write a Python program to validate a list of URLs. A valid URL should start with 'http://' or 'https://', followed by a domain name.
'''
import re

def validate_urls(urls):
    validated_urls = []
    for url in urls:
        # Define the regex pattern for validating URLs
        pattern = r'^(https?://)?([a-zA-Z0-9-]+\.)*[a-zA-Z]{2,}(/.*)?$'
        if re.match(pattern, url):
            validated_urls.append(url)
    return validated_urls

urls = ["https://example.com", "www.example.com", "http://test.com"]
validated_urls = validate_urls(urls)
print("Valid URLs:")
for url in validated_urls:
    print(url)
