import re
text = """
Hello my name is Rahul. Rahul is studying NLP.
Contact me at rahul123@gmail.com or call 9876543210.
I am working on detecting patterns using regex and learning.
Date of submission: 12/08/2025
"""
capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)
print("Capitalized Words:", capital_words)

repeated_words = re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE)
print("Repeated Words:", repeated_words)

emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
print("Emails:", emails)

phone_numbers = re.findall(r'\b\d{10}\b', text)
print("Phone Numbers:", phone_numbers)

ing_words = re.findall(r'\b\w+ing\b', text)
print("Words ending with 'ing':", ing_words)

dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
print("Dates:", dates)
