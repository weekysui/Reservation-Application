import getpass
from enum import Enum
import pandas as pd
from datetime import datetime, timedelta
import sqlite3


# connect the sqlitedb
conn = sqlite3.connect('project.db')
c = conn.cursor()

# create dataframe from csv files:
clientdf = pd.read_csv('MOCK_DATA.csv')
servicedf = pd.read_csv('service.csv')
pricedf = pd.read_csv('price.csv')
# import csv into table 'clients', 'services', 'price' in sqlite3
clientdf.to_sql('clients',conn, if_exists='replace',index = False)
servicedf.to_sql('services',conn, if_exists='replace',index = False)
pricedf.to_sql('price',conn,if_exists='replace',index = False)
# clientdf['start_date'] =pd.to_datetime(clientdf['start_date'])
# clientdf['end_date'] =pd.to_datetime(clientdf['end_date'])

# function to show all records including header in sqlite3 db
# def showTable(table):
#     values = c.execute(f"SELECT * FROM {table}")
#     col_name_list = [tuple[0] for tuple in c.description]
#     print(col_name_list)
#     for row in values:
#         print(row)

# showTable('clients')


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
            print("Facial Scheduling: Choose a time option. Input 1 for 30 min, 2 for 60 min.")
            print()
            for i in self.facial:
                print(i,self.facial[i])
            print()
    
           
class Login(object):
    def __init__(self):
        self.password = None
        self.userChoice = None
    def logIn(self):
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
    def getClientID(self):
        self.client = int(input("What is your client ID?"))
        idList = c.
        if self.client in clientdf['id']:
            return(self.client)
        else:
            print("Sorry, the client's ID is not in the Resert Database.")
            self.getClientID()
    def getUnitPrice(self,service):
        self.unitPrice = pricedf.loc[pricedf['service']==service]
        self.unitPrice = int(self.unitPrice['unit_price'])
        return self.unitPrice
    def checkDate(self,client):
        self.date = input('What date would like to schedule the service?')
        self.date = datetime.strptime(self.date,'%m/%d/%Y').date()
        info = clientdf.loc[clientdf['id']==self.client]
        if self.date>= info['start_date'][self.client-1] and self.date <= info['end_date'][self.client-1]:
            return self.date
        else:
            print('Sorry, the selected date is not within your stay at the resort. Please select a date during the time you are here.')
            self.checkDate(client)
    def checkTime(self,service):
        self.startTime = input("What is the start time?")
        timeDf = servicedf.loc[servicedf['date']==self.date]
        if self.startTime in str(timeDf['start_time']):
            print('Sorry, the selected time is not available. Please select another time.')
            self.checkTime(service)
        else:
            return self.startTime
    
    def getDuration(self,service,option):
        self.duration = service.facial[int(option)]
        duF = timedelta(minutes=int(self.duration))
        return duF, self.duration
    def confirmApp(self,service):
        confInput = input('Would you like to confirm your appointment? (Y/N)')
        if confInput == 'Y':
            return True
        else:
            print('No? Ok')

    def facial(self,service,option):
        self.client = self.getClientID()
        if self.client:
            pricePerMin = self.getUnitPrice(service)
            info = clientdf.loc[clientdf['id']== self.client]
            if self.checkDate(self.client):
                if self.checkTime(service):
                    self.startTimeF = datetime.strptime(self.startTime,'%I:%M %p')   
                    facial = Mainmenu()
                    duF = self.getDuration(facial,option)[0]
                    self.endTime = ((duF+self.startTimeF).time()).strftime('%I:%M %p')
                    self.unitPrice = self.getUnitPrice(service)
                    duration = self.getDuration(facial,option)[1]
                    totalPrice = int(duration)*self.unitPrice
                    print(f'The total price is {totalPrice}')
                    # confInput = input('Would you like to confirm your appointment? (Y/N)')
                    if self.confirmApp(service):
                        print(f'Your confirmation code is {str(101)+service}.')       #要改confirmation number
                        self.servicedf = servicedf.append({
                            'id':self.client,
                            'first_name': info['first_name'][1],
                            'last_name': info['last_name'][1],
                            'date': self.date,
                            'start_time': self.startTimeF.time().strftime('%I:%M %p'),
                            'end_time': self.endTime,
                            'duration': duration,
                            'service': service,
                            'total_price': totalPrice,
                            'confirmation': str(101)+service
                        }, ignore_index=True)
                        print(self.servicedf) 

login = Login()
login.logIn()



 