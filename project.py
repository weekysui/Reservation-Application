import getpass
from enum import Enum
import pandas as pd
from datetime import datetime
from datetime import timedelta

# get client info from csv database:
clientdf = pd.read_csv('MOCK_DATA.csv')
clientdf['start_date'] =pd.to_datetime(clientdf['start_date'])
clientdf['end_date'] =pd.to_datetime(clientdf['end_date'])
servicedf = pd.read_csv('service.csv')
# servicedf['start_time'] = pd.to_datetime(servicedf['start_time']).dt.time
# servicedf['end_time'] = pd.to_datetime(servicedf['end_time']).dt.time


class MenuOption(Enum):
    """
    assign number to different layers of menu, easier for later modification.
    """
    mainMenu = 1
    facial = 2
    massage = 3
    miner = 4
    specilty = 5
    lookUp = 6
    maintenance = 7
    signOut = 8

class Mainmenu(object):
    def __init__(self):
        self.main_menu = {
            1: 'Facial Scheduling',
            2: 'Massage Scheduling',
            3: 'Mineral Bath Scheduling',
            4: 'Specialty Treatment Scheduling',
            5: 'Look Up or Edit an Appointment',
            6: 'Perform Maintenance',
            7: 'Sign Out or Quit'
        }
        self.facial = {
            1: '30',
            2: '60'
        }  
    def printOption(self,option=MenuOption.mainMenu.value):
        if option == MenuOption.mainMenu.value:
            print("Main Menu")
            print()
            for i in self.main_menu:
                print(i,self.main_menu[i])
            print()
        elif option == MenuOption.facial.value:
            print("Facial Scheduling: ")
            print()
            for i in self.facial:
                print(i,self.facial[i])
            print()
    
           
class Login(object):
    def __init__(self):
        self.password = None
        self.userChoice = None
    def logIn(self):
        # username = input('Username: ')
        # getpass library hides the password
        print('Please type your password below then press ENTER or RETURN.')
        self.password = getpass.getpass('Password: ') 
        if self.password == 'admin':
            main = Mainmenu()
            main.printOption()
            self.userChoice = input("Type the number of the option you want, then press ENTER or RETURN.")
            response = True
            while response:
                if self.userChoice=='1':  
                    main.printOption(2)   # printout facial menu, 2 is number in MenuOption
                    facial = Reservation()
                    _min = input("Type the number of the option you want, then press ENTER or RETURN.")
                    facial.facial('facial',_min)
                    response = False
                elif self.userChoice=='7':
                    print("You are signing out the program")
                    self.logIn()
                    response = False
                else:
                    print( "Sorry, that is not a recognized command. Please type the number for one of the above options and press ENTER or RETURN.")
                    main.printOption()
                    self.userChoice = input("Type the number of the option you want, then press ENTER or RETURN.")
                    response = True

        else:
            print("Sorry, but that password is not recognized. Please try again.")
            self.logIn()

class Reservation(object):
    def __init__(self):
        pass
    def facial(self,service,option):
        facial = Mainmenu()
        self.client = int(input("What is your client ID?"))
        if self.client in clientdf['id']:
            info = clientdf.loc[clientdf['id']==self.client]
            
#             print(info['start_date'])
          
#             print(self.date)
            self.response = True
            while self.response:
                self.date = input("What date?")
                self.date = datetime.strptime(self.date,'%m/%d/%Y').date()
                if self.date>= info['start_date'][self.client-1] and self.date <= info['end_date'][self.client-1]:
                    self.response = False
                    self.r = True
                    while self.r:
                        self.startTime = input("What is the start time?")
    #                     self.startTime = datetime.strptime(self.startTime,'%I:%M %p').time()
                        timeDf = servicedf.loc[servicedf['date']==self.date]
                        if self.startTime in str(timeDf['start_time']):
                            print('sorry this time is not available, please choose another time')
                            self.r = True
                        else:
                            self.startTimeF = datetime.strptime(self.startTime,'%I:%M %p')           
                            duration = facial.facial[int(option)]
#                             print(duration)
                            duF = timedelta(minutes=int(duration))
                            self.endTime = ((duF+self.startTimeF).time()).strftime('%I:%M %p')
#                             print(info['first_name'][1])
#                             print(info['last_name'][1])
                            self.servicedf = servicedf.append({
                                'id':self.client,
                                'first_name': info['first_name'][1],
                                'last_name': info['last_name'][1],
                                'date': self.date,
                                'start_time': self.startTimeF.time().strftime('%I:%M %p'),
                                'end_time': self.endTime,
                                'duration': duration,
                                'service': service
                            }, ignore_index=True)
                            print(self.servicedf.head())
                        self.r = False
                else:
                    print('wrong date')
                    self.response = True
                                                       
        else:
            print('not in the db')



login = Login()
login.logIn()



 