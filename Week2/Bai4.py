import re

# s = input()

emailPattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email1 = "dhcnhn@gmail.com"
if re.fullmatch(emailPattern, email1):
    print(f"{email1} is valid")
else:
    print(f"{email1} is not valid")

email2 = "dhcnhn@.com"
if re.fullmatch(emailPattern, email2):
    print(f"{email2} is valid")
else:
    print(f"{email2} is not valid")

email3 = "hitpythonprivate"
if re.fullmatch(emailPattern, email3):
    print(f"{email3} is valid")
else:
    print(f"{email3} is not valid")