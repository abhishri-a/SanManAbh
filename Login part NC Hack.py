import json

logorsin = input("If you do not have an account, enter Sign Up, if you do, enter Log In: ")

if logorsin == "Sign Up":
    Firstnm = input("Enter your First Name: ")
    Lastnm = input("Enter your Last Name: ")
    username = input("Enter Username: ")
    passw = input ("Enter Password: ")
    

    with open("accounts.json", "r") as log:
        acc = json.load(log)
    
    acc[username] = passw
    acc[Firstnm] = Lastnm

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

