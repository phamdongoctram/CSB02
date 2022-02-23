import re
dt = input("Date in MM/DD/YYYY: ")
print("Date in DD/MM/YYYY format:", re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4})', '\\2/\\1/\\3', dt))
