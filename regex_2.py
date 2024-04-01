'''
Problem Statement:
You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., 'exclude.com').
Modify the script to extract all email addresses except those from the specified domain.
'''

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
excluded_domain = 'exclude.com'

# Define the regular expression pattern with negative lookahead to exclude email addresses from the specified domain
pattern = r'\b[A-Za-z0-9._%+-]+@(?!{})(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b'.format(re.escape(excluded_domain))

# Find all email addresses except those from the specified domain
emails = re.findall(pattern, text)
print(emails)
