password = input("Enter your password: ")
print(password)
if len(password) >= 8:
    print("Length is good")
else:
    print("Password should contain at least 8 characters")
has_upper = False
has_lower = False
if password.isupper():
    has_upper = True
if password.islower():
    has_lower = True
has_digit = False
has_special = False
for char in password:
    if char.isdigit():
        has_digit = True 
    if char.isalnum():
        has_special = True 
