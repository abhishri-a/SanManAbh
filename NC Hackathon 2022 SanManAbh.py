import csv



with open("med.csv", mode = 'w') as csv_file:
    
    fieldnames = ['med_name', 'Type', 'side_effect']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'med_name': 'Tylenol', 'Type': 'OTC', 'side_effect': 'Nausea, Stomach pain, Rash, Dark urine'})
    writer.writerow({'med_name': 'Advil', 'Type': 'OTC', 'side_effect': 'Nausea, Dizziness, High blood pressure, Kidney damage'})
    writer.writerow({'med_name': 'Claritin', 'Type': 'OTC', 'side_effect': 'Dry mouth, Mild stomach upset, Loss of appetite, Trouble sleeping'})
    writer.writerow({'med_name': 'Pepto-Bismol', 'Type': 'OTC', 'side_effect': 'Nausea, Hearing loss, Diarrhea for over 2 days, Stomach symptoms worsen'})
    writer.writerow({'med_name': 'Lisinopril', 'Type': 'PRES', 'side_effect': 'Dry cough, Lightheadedness, Vomiting, Blurred vision'})
    writer.writerow({'med_name': 'Spironolactone', 'Type': 'PRES', 'side_effect': 'Dizzyness, Muscle cramps, Fatigue, Breast pain'})
    writer.writerow({'med_name': 'Metformin', 'Type': 'PRES', 'side_effect': 'Stomach ache, Vomiting, Metallic taste in mouth, Low blood sugar when combined with other diabetes medicine'})
    writer.writerow({'med_name': 'Azithromycin', 'Type': 'PRES', 'side_effect': 'Nausea, Vomiting, Headaches, Change in sense of taste'})
    

def read_csv():
    new_Table = {}
    with open("med.csv", mode = 'r') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=fieldnames)
        #Skipping the header
        next(reader)
        for row in reader:
            new_Table[row['med_name']] = row['side_effect']
        return new_Table

x = read_csv()

def give_side_effects_info():
    """This function enables you to input the medicine name and should return the side effects written
    in the dataset of that specific medicine"""
    medicine = str(input("Enter Prescription Name: "))
    print("Side effects are: " + x[medicine])
    
    

read_csv()
give_side_effects_info()
