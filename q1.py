#password strength checker
while True:
    password = input("Enter your password: ")
    
    # Check for empty input
    if password.strip() == "":
        print("Password cannot be empty. Please try again.\n")

    elif " " in password:
        print("Password cannot be space. Please try again.\n")    
    else:
        break

#Initialize condition
length = len(password)
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_alpha = any(char.isalpha() for char in password)

#Check password using conditinal logic check
if length < 6:
    print("Weak Password")

elif  6 <= length <= 10 and has_digit and has_alpha :
    print("Medium Passowrd")

elif length >10 and has_digit and has_upper:
    print("Strong Password")

else :
    print("Weak Password")


