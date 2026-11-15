import secrets
import string
print("PASSWORD GENERATOR AND STRENGTH CHECKER")
print("---------------------------------------")
def generate_funtion():
    characters=string.ascii_letters+string.digits+string.punctuation
    length=int(input("Enter the desired password length: "))
    password=''.join(secrets.choice(characters) for _ in range(length))
    print("Your generated password is :",password)






    

def check_strength():
    password=input("Enter a password to check")
    length=len(password)
    has_upper=any(char.isupper for char in password)
    has_lower=any(char.islower for char in password)
    has_digit=any(char.isdigit for char in password)
    has_special=any(char in string.punctuation for char in password)

    score=0

    if length >= 12:
        score+=1

    if  has_upper:
        score+=1

    if has_lower:
        score+=1

    if has_digit:
        score+=1

    if has_special:
        score+=1

    if score <=2:
        print("Password strength is WEAK")

    elif score <=4:
        print("Password strength is MEDIUM")

    else:
        print("Password strength is Strong")

    print("Password score",score,"/5")







def main():
    while True:
        print("\n 1. Generate password")
        print("\n 2.Check Password")
        print("\n 3.Exit")

        choice=input("Choose an option: ")
        if choice == "1":
            generate_funtion()

        elif choice =="2":
            check_strength

        elif choice=="3":
            print("Thank you for using the password generator")
            break
        else:
            print("Invalid Choice,please pick 1,2 or 3")










if __name__ == "__main__":
    main()







 