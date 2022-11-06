#dosage, frequesncy, time, duration
import json

logorsin = input("Write 1 to enter or edit prescription information or 2 to move on: ")

if logorsin == "1":
    Dose = input("Enter Dosage: ")
    Freq = input("Enter Frequency: ")
    Time = input("Enter Time: ")
    Dur = input ("Enter Duration: ")
    

    with open("prescr.json", "r") as log:
        acc = json.load(log)
    
    tw = {"prescrinfo": [Dose, Freq, Time, Dur]}

    acc = json.dumps(acc)

    with open("prescr.json", "w") as log:
        log.write(acc)

elif logorsin == "2":
    pass
else:
    print("You need to either enter info or something")