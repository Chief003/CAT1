patients = {
    "Patinet 1" : {
    "Name": "Samantha Boush",
    "Age": "27",
    "Illness": "Cold"
    },

    "Patient 2" : {
     "Name": "Anthony Nick",
     "Age": "50",
    "Illness": "Joint Pains"
    },

    "Patient 3" : {
     "Name": "Sunless",
     "Age": "20",
      "Illness": "Too Cool"
    }

}

def add_patient(patients_dict, patient_id, name, age, illness):
    patients_dict[patient_id] = {"Name": name, "Age": age, "Illness": illness}

def display_patients(patients_dict):
    if not patients_dict:
        print("No patients found.")
    for patient_id, patient in patients_dict.items():
        print(f"{patient_id} - Name: {patient['Name']}, Age: {patient['Age']}, Illness: {patient['Illness']}")

def search_patient(patients_dict, name):
    for patient_id, patient in patients_dict.items():
        if patient['Name'].lower() == name.lower():
            print(f"Found {patient_id} - Name: {patient['Name']}, Age: {patient['Age']}, Illness: {patient['Illness']}")
            return
    print("Patient not found.")

def remove_patient(patients_dict, name):
    for patient_id in list(patients_dict.keys()):
        if patients_dict[patient_id]['Name'].lower() == name.lower():
            del patients_dict[patient_id]
            print(f"Removed patient - Name: {name}")
            return
    print("Patient not found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Patient")
        print("2. Display All Patients")
        print("3. Search for a Patient")
        print("4. Remove a Patient")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = input("Enter patient ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            illness = input("Enter illness: ")
            add_patient(patients, patient_id, name, age, illness)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            name = input("Enter name to search: ")
            search_patient(patients, name)
        elif choice == '4':
            name = input("Enter name to remove: ")
            remove_patient(patients, name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




