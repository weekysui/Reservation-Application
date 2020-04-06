# import project

def maintMenu():
    print("""
    ***MAINTENANCE MENU***
    1. Edit Facial Services
    2. Edit Massage Services
    3. Edit Mineral Bath Services
    4. Edit Specialty Treatment Services
    5. Return to Scheduling System
    6. Sign Out or Quit""")

def editFacial():
    print("EDIT FACIAL SERVICES")
    print("1. Edit Price")
    print("2. Edit Services")
    print(input("Edit Facial Selection: "))

def editMassage():
    print("EDIT MASSAGE SERVICES")
    print("1. Edit Price")
    print("2. Edit Services")
    print("3. Back to Maintenance Menu")
    print(input("Edit Massage Selection: "))

def editMinBath():
    print("EDIT MINERAL BATH SERVICES")
    print("1. Edit Price")
    print("2. Edit Services")
    print("3. Back to Maintenance Menu")
    print(input("Edit Mineral Bath Selection: "))

def editSpecialty():
    print("EDIT SPECIALTY SERVICES")
    print("1. Edit Price")
    print("2. Edit Services")
    print("3. Back to Maintenance Menu")
    print(input("Edit Specialties Selection: "))

def runMaint():
    while True:
        maintMenu()
        selection = int(input("Select your Maintenance Menu option: "))
        if selection ==1:
            editFacial()
        elif selection ==2:
            editMassage()
        elif selection ==3:
            editMinBath()
        elif selection ==4:
            editSpecialty()
        elif selection ==5:
            print("Launching Scheduling System...")
            # login = project.Login()
            # login.logIn()
            break
        elif selection ==6:
            print("\n GOODBYE!\n")
            quit()
        else:
            print ("Invalid Choice. Please select an option from 1-6:")

