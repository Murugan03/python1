def option():
    choice = input("Register or Login:")
    if choice == "Register":
        Register()
    elif choice == "Login":
        login()
    else:
        print("value error")


def Register():
    name = input(" create your username, (eg:- murugan@gmail.com):")

    # name validation

    if name[0].isalpha() and "@" in name and "." in name:
        if (name.index("@")) + 1 != name.index("."):
            print("(5<password length<16,must have one upper case,one lower case,one digit,one special char) ")
            password = input("create your password:")
        else:
            print("enter a valid username")
    else:
        print("enter a valid username")

    # password validation

    lower, upper, digit, special = 0, 0, 0, 0
    special_char = "~!@#$%^&*<>?"
    if 5 < len(password) < 16:
        for i in password:
            if i.islower():
                lower += 1
            if i.isupper():
                upper += 1
            if i.isdigit():
                digit += 1
            if i in special_char:
                special += 1
    if lower and upper and digit and special >= 1:
        sign_up(name, password)
    else:
        print("invalid password")


# Registration after completed the username and password validation

def sign_up(name, password):
    f = open("customers.txt", "r")
    arr1 = []
    arr2 = []
    for i in f:
        x, y = i.split(", ")
        y = y.strip()
        arr1.append(x)
        arr2.append(y)
        info = dict(zip(arr1, arr2))
    if name in arr1:
        print("user name already exists,create different name")
        Register()
        f.close()
    else:
        f = open("customers.txt", "a")
        f.write(name + ", " + password + "\n")
        print("Registration success")


# login

def login():
    name = input("enter your user_name:")
    password = input("enter your password:")
    f = open("customers.txt", "r")
    arr1 = []
    arr2 = []
    for i in f:
        x, y = i.split(", ")
        y = y.strip()
        arr1.append(x)
        arr2.append(y)
        info = dict(zip(arr1, arr2))
    try:
        if info[name]:
            if password == info[name]:
                print("welcome you are successfully login")
            elif input("you are entered incorrect password,if want to give forgot password:") == "yes":
                print("your password is :", info.get(name))
            else:
                print("please provide a new password")
        else:
            print("user name not found go and Register")
            Register()
    except:
        print("user name not found go and Register")
        Register()


option()
