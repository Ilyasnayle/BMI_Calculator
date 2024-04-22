#Exercise: Extracting email addresses from text

#Given a text below,write a regular expression pattern to extract all emails from a text.

#email_text = "Contact us at support@example.com or at helpdesk@mysite.org."

#Expected Output ['support@example.com', 'helpdesk@mysite.org']


import re

email = "Contact us at support@example.com or at helpdesk@mysite.org."

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

extract_emails = re.findall(pattern, email)

print(extract_emails)
