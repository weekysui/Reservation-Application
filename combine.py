# import dependencies
import getpass
import sqlite3
from datetime import datetime, timedelta
from enum import Enum

import pandas as pd

# connect the sqlitedb
conn = sqlite3.connect('project1.db')
c = conn.cursor()

# create dataframe from csv files:
clientdf = pd.read_csv('MOCK_DATA.csv')
servicedf = pd.read_csv('service.csv')
pricedf = pd.read_csv('price.csv')
# get the date in right format
clientdf['start_date'] = pd.to_datetime(clientdf['start_date'])
clientdf['end_date'] = pd.to_datetime(clientdf['end_date'])
# import csv into table 'clients', 'services', 'price' in sqlite3
# clientdf.to_sql('clients', conn, if_exists='replace', index=False)
# servicedf.to_sql('services', conn, if_exists='replace', index=False)
# pricedf.to_sql('price', conn, if_exists='replace', index=False)


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
                print(f"{i-1}: {self.time[i]} min")
            print()
        elif option == MenuOption.specilty.value:
            print("Specialty Treatments Scheduling: Choose a time option below:")
            print('For example: 2')
            print()
            for i in range(2, 4):
                print(f"{i-1}: {self.time[i]} min")
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
                    if int(_min) <= len(self.time)-1:
                        reservation.main('normal facial', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue
                elif facialType == '2':
                    self.printOption(MenuOption.facial.value)  # printout facial menu, 2 is number in MenuOption
                    print("Type the number of the option you want, then press ENTER or RETURN.")
                    _min = input()
                    print()
                    if int(_min) <= len(self.time)-1:
                        reservation.main('collagen facial', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue
                else:
                    print("Sorry, your selection is not recognized.")
                    continue
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
                    if int(_min) <= len(self.time)-1:
                        reservation.main('swedish massage', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue
                elif massageType == '2':
                    self.printOption(MenuOption.massage.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    if int(_min) <= len(self.time)-1:
                        reservation.main('shiatsu massage', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue
                elif massageType == '3':
                    self.printOption(MenuOption.massage.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = input()
                    print()
                    if int(_min) <= len(self.time)-1:
                        reservation.main('deep tissue', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue
                else:
                    print("Sorry, your selection is not recognized.")
                    continue
            elif self.userChoice == '3':
                self.printOption(MenuOption.mineral.value)
                print('Type the number of the option you want, then press ENTER or RETURN.')
                _min = str(int(input())+1)
                print()
                if int(_min) <= len(self.time):
                    reservation.main('mineral bath', _min)
                    self.response = False
                else:
                    print('Sorry, your selection is not recognized.')
                    continue

            elif self.userChoice == '4':
                print(
                    'Would you like to choose 1. Hot Stone, 2. Sugar Scrub, 3. Herbal Body Wrap, 4. Botanical Mud Wrap.')
                print('Please enter the number [1/2/3/4]')
                specialtyType = input()
                print()
                if specialtyType == '1':
                    self.printOption(MenuOption.specilty.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = str(int(input())+1)
                    print()
                    if int(_min) <= len(self.time):
                        reservation.main('hot stone', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue

                elif specialtyType == '2':
                    self.printOption(MenuOption.specilty.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = str(int(input())+1)
                    print()
                    if int(_min) <= len(self.time):
                        reservation.main('sugar scrub', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue

                elif specialtyType == '3':
                    self.printOption(MenuOption.specilty.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = str(int(input())+1)
                    print()
                    if int(_min) <= len(self.time):
                        reservation.main('herbal body wrap', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue

                elif specialtyType == '4':
                    self.printOption(MenuOption.specilty.value)
                    print('Type the number of the option you want, then press ENTER or RETURN.')
                    _min = str(int(input())+1)
                    print()
                    if int(_min) <= len(self.time):
                        reservation.main('botanical mud wrap', _min)
                        self.response = False
                    else:
                        print('Sorry, your selection is not recognized.')
                        continue
                else:
                    print("Sorry, your selection is not recognized.")
                    continue
            elif self.userChoice == '6': #ADDED MAINTENANCE MODULE HERE
                maintenance = maint()
                maintenance.maintlogIn()
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
                    c.close()
                else:
                    print("You are leaving, good bye!")
                    self.response = False
                    c.close()
                    exit()
            else:
                print(
                    "Sorry, that is not a recognized command. Please type the number for one of the above options "
                    "and press ENTER or RETURN.")
                self.printOption()
                print("Type the number of the option you want, then press ENTER or RETURN.")
                self.userChoice = input()
                response = True

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

    def getInfoFromWhere(self, tableName, columnName, whereCol, whereVal):
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
        return self.unitPrice

    def checkDate(self, client):
        """
        this recursive function will check if the input date match with the client's stay at the resort;
        if yes, it will return the input date for service scheduling, if no, will prompt to select another date
        one argument: client's id
        """
        print('What date would you like to schedule the service? Please use the correct date format like mm/dd/yyyy')
        print('For example: 03/20/2020')
        self.date = input()
        print()
        try:
            self.date = datetime.strptime(self.date, '%m/%d/%Y').date()
            info = clientdf.loc[clientdf['id'] == client]
            self.startDate = info['start_date'][self.client - 1]
            self.endDate = info['end_date'][self.client - 1]
            if self.date >= self.startDate and self.date <= self.endDate:
                return self.date
            else:
                print(
                    f'You can choose date from {self.startDate.date()} to {self.endDate.date()}.')  
                print(
                    'Sorry, the selected date is not within your stay at the resort. Please select a date during the time you are here.')
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
        print()
        # startTime = time
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
        try:
            self.cidList = self.getInfoFromWhere('services', 'confirmation', 'service', service)
            self.serviceid = []
            for cid in self.cidList:
                self.serviceid.append(cid[0:3])
            self.serviceid.sort()
            return self.serviceid[-1]
        except:
            return 99

    def main(self, service, option):
        self.client = self.getClientID()
        if self.client:
            pricePerMin = self.getUnitPrice(service)
            info = clientdf.loc[clientdf['id'] == self.client]
            if self.checkDate(self.client):
                if service != 'mineral bath':
                    self.checkTime(service)
                try:
                    self.startTimeF = datetime.strptime(self.startTime, '%I:%M %p')
                    serviceType = Mainmenu()
                    duF = self.getDuration(serviceType, option)[0]
                    self.endTime = ((duF + self.startTimeF).time()).strftime('%I:%M %p')
                    self.unitPrice = self.getUnitPrice(service)
                    duration = self.getDuration(serviceType, option)[1]
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
                        "Client's ID": self.client,
                        'Name': f'{first_name} {last_name}',
                        'Date': self.date,
                        'Time': f'{start_time} - {self.endTime}',
                        'Duration': f'{duration} minutes',
                        'Service': service,
                        'Total price': f'$ {totalPrice}',
                        'Confirmation Number': str(conNum) + service.split(' ')[0]
                    }
                    newAddIn = {
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
                    print('-' * 40)
                    self.receipt = pd.DataFrame(data=newRecord, index=[' ']).T
                    print(self.receipt)
                    print()
                    columns = ', '.join(newAddIn.keys())
                    placeholders = ':' + ', :'.join(newAddIn.keys())
                    sql = 'INSERT INTO services ({}) VALUES ({})'.format(columns, placeholders)
                    c.execute(sql, newAddIn)
                    conn.commit()
                    main = Mainmenu()
                    main.chooseMenu()


class maint(object):
    def __init___(self):
        pass
    # adds a new service to SERVICE table
    def addNew(self):
        print("Adding a new service")
        conf = input("Is this what you want to do? Y/N ")
        if conf == "Y":
            c.execute('''SELECT MAX(service_id) FROM service''')
            max_id = c.fetchall()
            id = max_id[0][0] + 1
            name = input("Service Name: ")
            price = float(input("Service Rate per Minute: "))
            duration = int(input("Service Duration: "))
            type = int(input("Service Type (1: massage, 2: bath, 3: facial, 4: specialty): "))
            print("ID:",id,"NAME:",name,"RATE:",price,"DURATION:",duration,"TYPE:",type)
            conf_new = input("Confirm the new service? Y/N ")
            if conf_new == 'Y':
                c.execute('''INSERT INTO service (service_id, service_name, price, duration, type)
                VALUES(%d, '%s', %d, %d, %d)''' % (id, name, price, duration, type))
                conn.commit()
                print("New service has been added")
            elif conf_new == 'N':
                print("New service has been cancelled")

        elif conf == "N":
            print("Returning to Maintenance Menu...")

    # search the SERVICE table for a service
    def searchService(self):
        print("Search for a service")
        conf = input("Is this what you want to do? Y/N ")
        if conf == "Y":
            search_by = int(input("How would you like to search by? (1: ID, 2: name, 3: type) "))
            if search_by == 1:
                id = int(input("Service ID: "))
                c.execute('''SELECT * FROM service WHERE service_id = %d''' % (id))
            if search_by == 2:
                name = input("Service Name: ")
                c.execute('''SELECT * FROM service WHERE service_name = "%s"''' % (name))
            if search_by == 3:
                type = int(input("Service Type (1: massage, 2: bath, 3: facial, 4: specialty): "))
                c.execute('''SELECT * FROM service WHERE type = %d''' % (type))
            rows = c.fetchall()
            for row in rows:
                print("ID:",row[0],"|","NAME:", row[4], "|","Duration:",row[2],"|", "Rate: $",round(row[1], 2),"|","TYPE:",row[3])

        elif conf == "N":
            print("Returning to Maintenance Menu...")

    # update a service in SERVICE table
    def updateService(self):
        print("Updating a service")
        conf = input("Is this what you want to do? Y/N ")
        if conf == "Y":
            ask_id = int(input("Service ID: "))
            update_attribute = int(input("What do you need to edit? (1: duration, 2: name, 3: type, 4: price)"))
            if update_attribute == 1: #update DURATION attribute
                new_duration = int(input("Update duration to: "))
                c.execute('''UPDATE service SET duration = %d WHERE service_id = %d''' % (new_duration, ask_id))
                conn.commit()
                print("DURATION has been successfully changed to: ",new_duration, 'minutes')
            elif update_attribute == 2: #update NAME attribute
                new_name = input("Update name to: ")
                c.execute('''UPDATE service SET service_name = "%s" WHERE service_id = %d''' % (new_name, ask_id))
                conn.commit()
                print("NAME has been successfully changed to: ",new_name)
            elif update_attribute == 3: #update TYPE attribute
                new_type = int(input("Update type to (1: massage, 2: bath, 3: facial, 4: specialty): "))
                c.execute('''UPDATE service SET type = "%s" WHERE service_id = %d''' % (new_type, ask_id))
                conn.commit()
                print("TYPE has been successfully changed to: ",new_type)
            elif update_attribute == 4: #update PRICE attribute
                new_price = int(input("Update price to: "))
                c.execute('''UPDATE service SET price = %d WHERE service_id = %d''' % (new_price, ask_id))
                conn.commit()
                print("PRICE has been successfully changed to: $",float(new_price))
        elif conf == "N":
            print("Returning to Maintenance Menu...")

    def pricelist(self):
        print("\nMud In Your Eye - Services\n")
        c.execute('''SELECT service_name, duration, (duration*price) AS 'total price' FROM service ORDER BY type''')
        rows = c.fetchall()
        # new code for price list
        c.execute('''SELECT DISTINCT type.type, service.service_name FROM type JOIN service on type.type_id = service.type''')
        list = c.fetchall()
        c.execute('''SELECT DISTINCT type FROM type''')
        type = c.fetchall()

        service_listing = [] # list of all the services
        type_listing = []
        for x in list: # creating list of services
            service_listing.append(x[0:2])
        for j in type: # creating list of types: bath, massage, specialty, facial
            type_listing.append(j[0])
        #print("this is type list", type)
        #print("this is service list", list)
        #print("after append", service_listing)

        #creates list of services to print out
        for k in type_listing:
            print(k)
            for i in service_listing:
                if i[0] == k:
                    print("\t",i[1])
                    for row in rows:
                        if row[0] == i[1]:
                            print("\t\t","Duration:",row[1],"|", "Price: $",round(row[2], 2))
            print("\n")
        print("\n")


    def maintlogIn(self):
        print('Welcome to the Maintenance Module\nPlease type your USERNAME and PASSWORD below then press ENTER or RETURN.')
        #getpass library hides the password
        username = input("USERNAME: ")
        password = getpass.getpass('PASSWORD: ')
        c.execute('''SELECT * FROM users WHERE name = "%s"''' % (username))
        user = c.fetchall()
        if password == user[0][2]:
            self.maintMenu()
        else:
            print("Sorry, but that password is not recognized. Please try again.")
            self.logIn()

    def maintMenu(self):
        while True:
            print("""
            ***MAINTENANCE MENU***
            1. SEARCH for a service
            2. ADD a new service
            3. UPDATE a current service
            4. PRINT a list of ALL services
            5. Return to Scheduling System
            6. Sign Out or Quit\n""")

            selection = int(input("Select your Maintenance Menu option: "))
            if selection ==1:
                self.searchService()
            elif selection ==2:
                self.addNew()
            elif selection ==3:
                self.updateService()
            elif selection ==4:
                self.pricelist()
            elif selection ==5:
                print("Launching Scheduling System...")
                conn.close()
                login = Login()
                login.logIn()
            elif selection ==6:
                print("\n\nMiYE Application closing...\n")
                conn.close()
                print("Database connection closed...")
                sys.exit("\nGOODBYE!\n")
            else:
                print ("Invalid Choice. Please select an option from 1-6:")


login = Login()
login.logIn()

# conn = sqlite3.connect('project1.db')
# c = conn.cursor()
# table = c.execute('SELECT * FROM services')
# for row in table:
#     print(row)
