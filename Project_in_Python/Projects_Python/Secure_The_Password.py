'''Creata a Python Program to secure the Passwords'''

SECURE = (('s','$'),('and','&'),('a','@'),('i','1'),('o','0')) # --> Tuple --> Used To replace the some chaaracter in password and secure the password

def SecurePassword(Password):
    # Password --> BlackBoards123 --> Secure Password --> BlackBoard$123
    # Password --> BlackAndWhites --> Secure Password --> Black&White$
    for a,b in SECURE:
        password = Password.replace(a,b)
        return password
    

password = input("Enter your password\t")
print(SecurePassword(password))