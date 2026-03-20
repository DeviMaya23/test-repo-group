#password strength checker
password = input("Enter the password : ")

#Initialize condition
length = len(password)
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

#Check password using conditinal logic check
if length < 6:
    print("Weak Password")

elif  6 <= length <= 10 and has_digit :
    print("Medium Passowrd")

elif length >10 and has_digit and has_upper:
    print("Strong Password")

else :
    print("Weak Password")


