# import getpass
# from enum import Enum
import pandas as pd

# # get client info from csv database:
clientdf = pd.read_csv('MOCK_DATA.csv')
clientdf.head()
# clientDict = clientdf.to_dict()
# # list of clientID
# clientID = list(clientDict['id'].values())

# class MenuOption(Enum):
#     """
#     assign number to different layers of menu, easier for later modification.
#     """
#     mainMenu = 1
#     facial = 2
#     massage = 3
#     miner = 4
#     specilty = 5
#     lookUp = 6
#     maintenance = 7
#     signOut = 8

# class Mainmenu(object):
#     def __init__(self):
#         self.main_menu = {
#             1: 'Facial Scheduling',
#             2: 'Massage Scheduling',
#             3: 'Mineral Bath Scheduling',
#             4: 'Specialty Treatment Scheduling',
#             5: 'Look Up or Edit an Appointment',
#             6: 'Perform Maintenance',
#             7: 'Sign Out or Quit'
#         }
#         self.facial = {
#             1: '30min',
#             2: '60min'
#         }  
#     def printOption(self,option=MenuOption.mainMenu.value):
#         if option == MenuOption.mainMenu.value:
#             print("Main Menu")
#             print()
#             for i in self.main_menu:
#                 print(i,self.main_menu[i])
#             print()
#         elif option == MenuOption.facial.value:
#             print("Facial Scheduling")
#             print()
#             for i in self.facial:
#                 print(i,self.facial[i])
#             print()
    
           
# class Login(object):
#     def __init__(self):
#         self.password = None
#         self.userChoice = None
#     def logIn(self):
#         # username = input('Username: ')
#         # getpass library hides the password
#         print('Please type your password below then press ENTER or RETURN.')
#         self.password = getpass.getpass('Password: ') 
        
#         if self.password == 'admin':
#             main = Mainmenu()
#             main.printOption()
#             self.userChoice = input("Type the number of the option you want, then press ENTER or RETURN.")
#             response = True
#             while response:
#                 if self.userChoice=='1':  
#                     main.printOption(2)   # printout facial menu, 2 is number in MenuOption
#                     facial = Reservation()

#                     response = False
#                 elif self.userChoice=='7':
#                     print("You are signing out the program")
#                     self.logIn()
#                     response = False
#                 else:
#                     print( "Sorry, that is not a recognized command. Please type the number for one of the above options and press ENTER or RETURN.")
#                     main.printOption()
#                     self.userChoice = input("Type the number of the option you want, then press ENTER or RETURN.")
#                     response = True

#         else:
#             print("Sorry, but that password is not recognized. Please try again.")
#             self.logIn()


# class Reservation(object):
#     def __init__(self):

#     def reservation(self):
#         _id = input("What is the clientID?")
#         if _id in clientID:




# login = Login()
# login.logIn()



 