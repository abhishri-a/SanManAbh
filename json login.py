import json

logorsin = input("If you do not have an account, enter Sign Up, if you do, enter Log In: ")

if logorsin == "Sign Up":
    Firstnm = input("Enter your First Name: ")
    Lastnm = input("Enter your Last Name: ")
    Email = input("Enter your email: ")
    Phone = input("Enter your phone number: ")
    username = input("Enter Username: ")
    passw = input ("Enter Password: ")
    

    with open("accounts.json", "r") as log:
        acc = json.load(log)
        if username in acc:
            print("This username is already taken!")
            username = input("Enter Username: ")
            if len(passw) <6:
                print("This Password is too short")
            else:
                pass
        else:
            pass
    
    acc[username] = passw
    acc[Firstnm] = Lastnm
    acc[Email] = Phone

    acc = json.dumps(acc)

    with open("accounts.json", "w") as log:
        log.write(acc)

elif logorsin == "Log In":
    username = input("Enter Username: ")
    passw = input ("Enter Password: ")
    with open("accounts.json", "r") as log:
        acc = json.load(log)
        if username in acc:
            if passw == acc[username]:
                print("You are Logged in!")
            else:
                print("Password Incorrect")
        else:
            print("Username does not exist")
else:
    print("You need to either enter Sign Up or Log In")

