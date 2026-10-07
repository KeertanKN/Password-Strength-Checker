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
score = 0
if len(password) >= 8:
    score +=1
if has_upper:
    score +=1
if has_lower:
    score +=1
if has_digit:
    score +=1
if has_special:
    score +=1
if score <= 2:
    print("weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strog Password")
