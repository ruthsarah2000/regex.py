'''
Problem Statement: You have a log file represented as a string, containing timestamps and messages. Write a script to reformat the 
timestamps from 'MM-DD-YYYY' to 'YYYY-MM-DD' and anonymize any usernames mentioned in the log (format: '@username').
'''
import re

def reformat_log(log_data):
    timestamp_pattern = r'(\d{2})-(\d{2})-(\d{4})'
    timestamps = re.findall(timestamp_pattern, log_data)
    reformatted_log = re.sub(timestamp_pattern, r'\3-\1-\2', log_data)
    username_pattern = r'@(\w+)'
    anonymized_log = re.sub(username_pattern, '@username', reformatted_log)
    return anonymized_log

log_data = "12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."
reformatted_log = reformat_log(log_data)
print(reformatted_log)
