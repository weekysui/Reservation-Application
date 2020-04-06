# import dependencies
import getpass
from enum import Enum
import pandas as pd
from datetime import datetime, timedelta
import sqlite3

# connect the sqlitedb
conn = sqlite3.connect('project1.db')
c = conn.cursor()

# create dataframe from csv files:
clientdf = pd.read_csv('MOCK_DATA.csv')
servicedf = pd.read_csv('service.csv')
pricedf = pd.read_csv('price.csv')
# get the date in right format
clientdf['start_date'] =pd.to_datetime(clientdf['start_date'])
clientdf['end_date'] =pd.to_datetime(clientdf['end_date'])
# import csv into table 'clients', 'services', 'price' in sqlite3
clientdf.to_sql('clients',conn, if_exists='replace',index = False)
servicedf.to_sql('services',conn, if_exists='replace',index = False)
pricedf.to_sql('price',conn,if_exists='replace',index = False)


class MenuOption(Enum):
    """
    assign number to different layers of menu, easier for later modification.
    """
    mainMenu = 1
    facial = 2
    massage = 3
    mineral = 4
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
        self.time = {
            1: '30',
            2: '60',
            3: '90'
        }

    def printOption(self, option=MenuOption.mainMenu.value):
        """
        functin to display differnt layers of menu
        arguments: integer that matches the Menuoption enum class
        """
        if option == MenuOption.mainMenu.value:
            print("Main Menu")
            print()
            for i in self.main_menu:
                print(i, self.main_menu[i])
            print()
        elif option == MenuOption.facial.value:
            print("Facial Scheduling: Choose a time option below:")
            print('For example: 2')
            print()
            for i in range(1, 3):
                print(f"{i}: {self.time[i]} min")
            print()
        elif option == MenuOption.massage.value:
            print("Massage Scheduling: Choose a time option below:")
            print('For example: 2')
            print()
            for i in range(1, 3):
                print(f"{i}: {self.time[i]} min")
            print()
        elif option == MenuOption.mineral.value:
            print("Mineral Bath Scheduling: Choose a time option below:")
            print('For example: 2')
            print()
            for i in range(2, 4):
                print(f"{i}: {self.time[i]} min")
            print()
        elif option == MenuOption.specilty.value:
            print("Specialty Treatments Scheduling: Choose a time option below:")
            print('For example: 2')
            print()
            for i in range(2, 4):
                print(f"{i}: {self.time[i]} min")
            print()

    def chooseMenu(self):
        self.printOption()
        print("Type the number of the option you want, then press ENTER or RETURN.")
        self.userChoice = input()
        print()
        self.response = True
        reservation = Reservation()
        while self.response:
            if self.userChoice == '1':
                print('Would you like to choose 1. normal facial 2. collagen facial.')
                print('Please enter the number [1/2]')
                facialType = input()
                print()
                if facialType == '1':
                    # print(_min)
                    self.printOption(MenuOption.facial.value)  # printout facial menu, 2 is number in MenuOption
                    print("Type the number of the option you want, then press ENTER or RETURN.")
                    _min = input()
                    print()
                    reservation.facial('normal facial', _min)
                    self.response = False
                else:
                    self.printOption(MenuOption.facial.value)  # printout facial menu, 2 is number in MenuOption
                    print("Type the number of the option you want, then press ENTER or RETURN.")
                    _min = input()
                    print()
                    reservation.facial('collagen facial', _min)
                    self.response = False
            elif self.userChoice == '2':
                print('Would you like to choose 1. Swedish Massage, 2. Shiatsu Massage, 3. Deep Tissue.')
                print('Please enter the number [1/2/3]')
                massageType = input()
                print()
                if massageType == '1':
                    self.printOption(MenuOption.massage.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    reservation.massage('swedish massage', _min)
                    self.response = False
                elif massageType == '2':
                    self.printOption(MenuOption.massage.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    reservation.massage('shiatsu massage', _min)
                    self.response = False
                else:
                    self.printOption(MenuOption.massage.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    reservation.massage('deep tissue', _min)
                    self.response = False
            elif self.userChoice == '3':
                self.printOption(MenuOption.mineral.value)
                print('Type the number of the option you want, then press ENTER or RETURN.')
                _min = input()
                print()
                reservation.mineral('mineral bath', _min)
                self.response = False
            elif self.userChoice == '4':
                print('Would you like to choose 1. Hot Stone, 2. Sugar Scrub, 3. Herbal Body Wrap, 4. Botanical Mud Wrap.')
                print('Please enter the number [1/2/3/4]')
                specialtyType = input()
                print()
                if specialtyType == '1':
                    self.printOption(MenuOption.specilty.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    reservation.massage('hot stone', _min)
                    self.response = False
                elif specialtyType == '2':
                    self.printOption(MenuOption.specilty.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    reservation.massage('sugar scrub', _min)
                    self.response = False
                elif specialtyType == '3':
                    self.printOption(MenuOption.specilty.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    reservation.massage('herbal body wrap', _min)
                    self.response = False
                else:
                    self.printOption(MenuOption.specilty.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    reservation.specialty('botanical mud wrap', _min)
                    self.response = False
            elif self.userChoice == '7':
                print("Do you want to quit or logout?")
                print("1. Sign Out.")
                print("2. Quit.")
                user = input()
                print()
                if user == '1':
                    login = Login()
                    login.logIn()
                    self.response = False
                else:
                    print("You are leaving, good bye!")
                    self.response = False
                    exit()
            else:
                print(
                    "Sorry, that is not a recognized command. Please type the number for one of the above options and press ENTER or RETURN.")
                self.printOption()
                print("Type the number of the option you want, then press ENTER or RETURN.")
                self.userChoice = input()
                response = True

# Login class handles all the login function and handling login errors 
# Login class handles all the login function and handling login errors
class Login(object):
    def __init__(self):
        self.password = None
        self.userChoice = None

    def logIn(self):
        print('Please type your password below then press ENTER or RETURN.')
        # getpass library hides the password
        self.password = getpass.getpass('Password: ')
        if self.password == 'admin':
            main = Mainmenu()
            main.chooseMenu()
        else:
            print("Sorry, but that password is not recognized. Please try again.")
            self.logIn()


class Reservation(object):
    def __init__(self):
        pass

    def getInfoFromTable(self, tableName, columnName):
        """ 
        This function is able to return the informatin that you query
        takes 2 arguements, the table's name, and the column's name, and return a list of records.
        """
        infor = []
        clientTable = c.execute(f'SELECT {columnName} FROM {tableName}')
        for row in clientTable:
            infor.append(row[0])
        return infor

    def getInfoFromWhere(self,tableName,columnName,whereCol, whereVal):
        infor = []
        table = c.execute(f'SELECT {columnName} FROM {tableName} WHERE {whereCol} = ?', (whereVal,))
        for row in table:
            infor.append(row[0])
        return infor

    def getClientID(self):
        """
        this recursive function is able to check if the client's id is in the db;
        if yes, will return the client's id; if no, will throw an error msg and ask to try again
        """
        print("What is your client ID? Please input numbers only")
        print("For example: 1")
        self.client = int(input())
        print()
        self.clientID = self.getInfoFromTable('clients', 'id')
        if self.client in self.clientID:
            return (self.client)
        else:
            print("Sorry, the client's ID is not in the Resert Database.")
            return self.getClientID()

    def getUnitPrice(self, service):
        """
        this function return the unit price that matches with the service
        one argument: string, service like facial, massage, mineral bath, specialty treatment
        """
        self.unitPrice = float(self.getInfoFromWhere('price', 'unit_price', 'service', service)[0])
        # print(self.unitPrice)
        # self.unitPrice = int(self.getInfoFromTable('price', 'unit_price')[0])
        return self.unitPrice

    def checkDate(self, client):
        """
        this recursive function will check if the input date match with the client's stay at the resort;
        if yes, it will return the input date for service scheduling, if no, will prompt to select another date
        one argument: client's id
        """
        print('What date would like to schedule the service? Please use the correct date format like mm/dd/yyyy')
        print('For example: 03/20/2020')
        self.date = input()
        print()
        try:
            self.date = datetime.strptime(self.date, '%m/%d/%Y').date()
            info = clientdf.loc[clientdf['id']==client]
            self.startDate = info['start_date'][self.client-1]
            self.endDate = info['end_date'][self.client-1]
            if self.date >= self.startDate and self.date <= self.endDate:
                return self.date
            else:
                print(f'You can choose date from {self.startDate} to {self.endDate}.') #要解决后面会出来时间的问题，现在是2020-03-20 00:00:00
                print('Sorry, the selected date is not within your stay at the resort. Please select a date during the time you are here.')
                return self.checkDate(client)
        except ValueError:
            print('Please use the correct date format like mm/dd/yyyy')
            return self.checkDate(client)

    def checkTime(self, serviceType):
        """
        this recursive function will check if input time is available for this service, if yes will return the start time, if no will prompt user to select another time
        one argument: service like facial, massage, mineral bath or specialty treatment.
        也要查结束时间是否可行
        """
        print("What is the start time? Please use the time format like hh:mm AM/PM")
        print('For example: 08:00 AM')
        self.startTime = input()
        #         self.startTimeF = datetime.strptime(self.startTime,'%I:%M %p')
        print()
        infor = []
        timeTable = c.execute("select start_time from services where service = ?", (serviceType,))
        for row in timeTable:
            infor.append(row[0])
        if self.startTime in infor:
            print('Sorry, the selected time is not available. Please select another time.')
            return self.checkTime(serviceType)
        else:
            return self.startTime

    def getDuration(self, service, option):
        """
        this function return service duration that selected from the menu option
        it return 1. formated duration time 2. string of duration
        2 arguments: service, menuOption of duration
        这个service的选项有必要吗？
        """
        main = Mainmenu()
        self.duration = service.time[int(option)]
        duF = timedelta(minutes=int(self.duration))
        return duF, self.duration

    def confirmApp(self):
        """
        this function will prompt user to confirm the appointment, if yes, return True, if no, return to the main menu
        one argument: service
        """
        print('Would you like to confirm your appointment? (Y/N)')
        confInput = input()
        print()
        if confInput == 'Y':
            return True
        elif confInput == 'N':
            main = Mainmenu()
            main.chooseMenu()
        else:
            print("Sorry, your input is not recognized, please select (Y/N)")
            return self.confirmApp()

    def confirmationId(self, service):
        self.cidList = self.getInfoFromTable('services', 'confirmation')
        self.serviceid = []
        for cid in self.cidList:
            if cid[3:] == service:
                self.serviceid.append(cid[0:3])
        self.serviceid.sort()
        if self.serviceid:
            return self.serviceid[-1]
        else:
            return 99

    def facial(self, service, option):
        self.client = self.getClientID()
        if self.client:
            pricePerMin = self.getUnitPrice(service)
            info = clientdf.loc[clientdf['id'] == self.client]
            if self.checkDate(self.client):
                if self.checkTime(service):
                    try:
                        self.startTimeF = datetime.strptime(self.startTime, '%I:%M %p')
                        facial = Mainmenu()
                        duF = self.getDuration(facial, option)[0]
                        self.endTime = ((duF + self.startTimeF).time()).strftime('%I:%M %p')
                        self.unitPrice = self.getUnitPrice(service)
                        duration = self.getDuration(facial, option)[1]
                        totalPrice = int(duration) * self.unitPrice
                        #                     first_name = self.get
                        print(f'The total price is {totalPrice}')
                    except:
                        print('Please use the correct time format hh:mm AM/PM')
                        self.checkTime(service)
                    # confInput = input('Would you like to confirm your appointment? (Y/N)')
                    if self.confirmApp():
                        conNum = int(self.confirmationId(service)) + 1
                        first_name = info['first_name'][self.client - 1]
                        last_name = info['last_name'][self.client - 1]
                        start_time = self.startTimeF.time().strftime('%I:%M %p')
                        newRecord = {
                            'id': self.client,
                            'date': self.date,
                            'start_time': start_time,
                            'end_time': self.endTime,
                            'duration': duration,
                            'service': service,
                            'total_price': totalPrice,
                            'confirmation': str(conNum) + service.split(' ')[0]
                        }
                        print('Receipt:')
                        print('-' * 30)
                        self.receipt = pd.DataFrame(data=newRecord, index=[' ']).T
                        print(self.receipt)
                        columns = ', '.join(newRecord.keys())
                        placeholders = ':' + ', :'.join(newRecord.keys())
                        sql = 'INSERT INTO services ({}) VALUES ({})'.format(columns, placeholders)
                        c.execute(sql, newRecord)
                        conn.commit()

    def massage(self, service, option):
        self.client = self.getClientID()
        if self.client:
            pricePerMin = self.getUnitPrice(service)
            info = clientdf.loc[clientdf['id'] == self.client]
            if self.checkDate(self.client):
                if self.checkTime(service):
                    try:
                        self.startTimeF = datetime.strptime(self.startTime, '%I:%M %p')
                        massage = Mainmenu()
                        duF = self.getDuration(massage, option)[0]
                        self.endTime = ((duF + self.startTimeF).time()).strftime('%I:%M %p')
                        self.unitPrice = self.getUnitPrice(service)
                        duration = self.getDuration(massage, option)[1]
                        totalPrice = int(duration) * self.unitPrice
                        print(f'The total price is {totalPrice}')
                    except:
                        print('Please use the correct time format hh:mm AM/PM')
                        self.checkTime(service)
                    # confInput = input('Would you like to confirm your appointment? (Y/N)')
                    if self.confirmApp():
                        conNum = int(self.confirmationId(service)) + 1
                        first_name = info['first_name'][self.client - 1]
                        last_name = info['last_name'][self.client - 1]
                        start_time = self.startTimeF.time().strftime('%I:%M %p')
                        newRecord = {
                            'id': self.client,
                            'date': self.date,
                            'start_time': start_time,
                            'end_time': self.endTime,
                            'duration': duration,
                            'service': service,
                            'total_price': totalPrice,
                            'confirmation': str(conNum) + service.split(' ')[0]
                        }
                        print('Receipt:')
                        print('-' * 25)
                        self.receipt = pd.DataFrame(data=newRecord, index=[' ']).T
                        print(self.receipt)
                        columns = ', '.join(newRecord.keys())
                        placeholders = ':' + ', :'.join(newRecord.keys())
                        sql = 'INSERT INTO services ({}) VALUES ({})'.format(columns, placeholders)
                        c.execute(sql, newRecord)
                        conn.commit()
                        c.close()
    def mineral(self, service, option):
        self.client = self.getClientID()
        if self.client:
            pricePerMin = self.getUnitPrice(service)
            info = clientdf.loc[clientdf['id'] == self.client]
            if self.checkDate(self.client):
                print("What is the start time? Please use the time format like hh:mm AM/PM")
                print('For example: 08:00 AM')
                self.startTime = input()
                try:
                    self.startTimeF = datetime.strptime(self.startTime, '%I:%M %p')
                    mineral = Mainmenu()
                    duF = self.getDuration(mineral, option)[0]
                    self.endTime = ((duF + self.startTimeF).time()).strftime('%I:%M %p')
                    self.unitPrice = self.getUnitPrice(service)
                    duration = self.getDuration(mineral, option)[1]
                    totalPrice = int(duration) * self.unitPrice
                    print(f'The total price is {totalPrice}')
                except:
                    print('Please use the correct time format hh:mm AM/PM')
                    self.checkTime(service)
                    # confInput = input('Would you like to confirm your appointment? (Y/N)')
                if self.confirmApp():
                    conNum = int(self.confirmationId(service)) + 1
                    first_name = info['first_name'][self.client - 1]
                    last_name = info['last_name'][self.client - 1]
                    start_time = self.startTimeF.time().strftime('%I:%M %p')
                    newRecord = {
                        'id': self.client,
                        'date': self.date,
                        'start_time': start_time,
                        'end_time': self.endTime,
                        'duration': duration,
                        'service': service,
                        'total_price': totalPrice,
                        'confirmation': str(conNum) + service.split(' ')[0]
                    }
                    print('Receipt:')
                    print('-' * 25)
                    self.receipt = pd.DataFrame(data=newRecord, index=[' ']).T
                    print(self.receipt)
                    columns = ', '.join(newRecord.keys())
                    placeholders = ':' + ', :'.join(newRecord.keys())
                    sql = 'INSERT INTO services ({}) VALUES ({})'.format(columns, placeholders)
                    c.execute(sql, newRecord)
                    conn.commit()
                    c.close()
    def specialty(self, service, option):
        self.client = self.getClientID()
        if self.client:
            pricePerMin = self.getUnitPrice(service)
            info = clientdf.loc[clientdf['id'] == self.client]
            if self.checkDate(self.client):
                if self.checkTime(service):
                    try:
                        self.startTimeF = datetime.strptime(self.startTime, '%I:%M %p')
                        specialty = Mainmenu()
                        duF = self.getDuration(specialty, option)[0]
                        self.endTime = ((duF + self.startTimeF).time()).strftime('%I:%M %p')
                        self.unitPrice = self.getUnitPrice(service)
                        duration = self.getDuration(specialty, option)[1]
                        totalPrice = int(duration) * self.unitPrice
                        print(f'The total price is {totalPrice}')
                    except:
                        print('Please use the correct time format hh:mm AM/PM')
                        self.checkTime(service)
                    # confInput = input('Would you like to confirm your appointment? (Y/N)')
                    if self.confirmApp():
                        conNum = int(self.confirmationId(service)) + 1
                        first_name = info['first_name'][self.client - 1]
                        last_name = info['last_name'][self.client - 1]
                        start_time = self.startTimeF.time().strftime('%I:%M %p')
                        newRecord = {
                            'id': self.client,
                            'date': self.date,
                            'start_time': start_time,
                            'end_time': self.endTime,
                            'duration': duration,
                            'service': service,
                            'total_price': totalPrice,
                            'confirmation': str(conNum) + service.split(' ')[0]
                        }
                        print('Receipt:')
                        print('-' * 30)
                        self.receipt = pd.DataFrame(data=newRecord, index=[' ']).T
                        print(self.receipt)
                        columns = ', '.join(newRecord.keys())
                        placeholders = ':' + ', :'.join(newRecord.keys())
                        sql = 'INSERT INTO services ({}) VALUES ({})'.format(columns, placeholders)
                        c.execute(sql, newRecord)
                        conn.commit()
                        c.close()


login = Login()
login.logIn()

# conn = sqlite3.connect('project.db')
# c = conn.cursor()
# table = c.execute('SELECT * FROM services')
# for row in table:
#     print(row)