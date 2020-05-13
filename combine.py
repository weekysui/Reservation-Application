# import dependencies
import getpass
import sqlite3
from datetime import datetime, timedelta
from enum import Enum
import sys
import pandas as pd
import json

# connect the sqlitedb
conn = sqlite3.connect('project1.db')
c = conn.cursor()

# create dataframe from csv files:
clientdf = pd.read_csv('MOCK_DATA.csv')
servicedf = pd.read_csv('service.csv')
# pricedf = pd.read_csv('price.csv')
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
            5: 'Look Up an Appointment',
            6: 'Cancel an Appointment',
            7: 'Perform Maintenance',
            8: 'Sign Out or Quit'
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
            elif self.userChoice == '5': #ADDED SEARCH AND MODIFICATION 
                search = Modification()
                search.searchServices()
            elif self.userChoice == '6':
                conNum = input('Please enter the confirmation number to modify your appointment:')
                try:
                    tables = c.execute('SELECT * FROM services where confirmation = ?',(conNum,))
                except:
                    print(f'the confirmation number {conNum} is not available.')
                infor = []
                for t in tables:
                    infor.append(t)
                # print(infor[0][0])                    
                cur = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                current = datetime.strptime(cur,'%Y-%m-%d %H:%M:%S')
                time = datetime.strptime(infor[0][0],'%Y-%m-%d %H:%M:%S')
                sche = f"{infor[0][3]} {datetime.strftime(datetime.strptime(infor[0][4],'%I:%M %p'),'%H:%M:%S')}"
                service_time = datetime.strptime(sche,'%Y-%m-%d %H:%M:%S')
                _min = timedelta(minutes=10)
                _mm = timedelta(minutes = 90)
                if current- time  <= _min or current - service_time <= _mm:
                    # print('yes')
                    # self.printOption(self.change_menu)
                    names = [description[0] for description in c.description]
                    # print(f'names[0]': infor[0][0])
                    # print(f'names[1]': infor[0][1])
                    # print(f'names[2]': infor[0][2])
                    n = 0
                    while n <9:
                        print(f'{names[n]}: {infor[0][n]}')
                        n+=1
                    print()
                    print(
                    'Would you like to choose 1. cancel service')
                    # print('Please enter the number [1/2/3]') 
                    user = input()
                    if user == '1':
                        choice = input('Are you sure you would like to cancel the appointment? [Y/N]')
                        if choice == 'Y':
                            c.execute('DELETE FROM services WHERE confirmation = ?',(conNum, ))
                            print(f'Your appointment with {conNum} has been canceled.')
                            print()
                            self.chooseMenu()
                        elif choice == 'N':
                            self.chooseMenu()
                        self.response = False
                    else:
                        print('Sorry your input is not recognized')
                        self.response = True
                else:
                    print('Sorry, you can not modify your appointment now.')
                    self.response = True
                
          
            elif self.userChoice == '7': #ADDED MAINTENANCE MODULE HERE
                maintenance = maint()
                maintenance.maintlogIn()
            elif self.userChoice == '8':
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
        print('What date would you like to schedule the service? Please use the correct date format like yyyy-mm-dd')
        print('For example: 2020-03-20')
        self.date = input()
        print()
        try:
            self.date = datetime.strptime(self.date, '%Y-%m-%d').date()
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
            print('Please use the correct date format like yyyy-mm-dd')
            return self.checkDate(client)

    def checkTime(self, serviceType):
        """
        this recursive function will check if input time is available for this service, if yes will return the start time, if no will prompt user to select another time
        one argument: service like facial, massage, mineral bath or specialty treatment.
        """
        print("We open from 08:00 AM - 08:00 PM.")
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
            print(f'Sorry, {self.startTime}  is not available. Please select another time.')
            return self.checkTime(serviceType)
        try:
            self.startTimeF = datetime.strptime(self.startTime, '%I:%M %p')
            self.openTime = datetime.strptime('08:00 AM', '%I:%M %p')
            self.closeTime = datetime.strptime('08:00 PM', '%I:%M %p')
            if self.openTime <= self.startTimeF <self.closeTime:
                return self.startTime, self.startTimeF
            else:
                print('Sorry, we open from 08:00 AM till 08:00 PM, please schedule a service within our operation hours.')
                return self.checkTime(serviceType)
        except ValueError:
            print('Please use the correct date format like hh:mm AM/PM')
            return self.checkTime(serviceType)

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
                    self.time = self.checkTime(service)
                    self.startTime = self.time[0]
                    self.startTimeF = self.time[1]
                    serviceType = Mainmenu()
                    duF = self.getDuration(serviceType, option)[0]
                    self.endTime = ((duF + self.startTimeF).time()).strftime('%I:%M %p')
                    self.unitPrice = self.getUnitPrice(service)
                    duration = self.getDuration(serviceType, option)[1]
                    totalPrice = int(duration) * self.unitPrice
                    print(f'The total price is {totalPrice}')
                else:
                    print("We open from 08:00 AM - 08:00 PM.")
                    print("What is the start time? Please use the time format like hh:mm AM/PM")
                    print('For example: 08:00 AM')
                    self.startTime = input()
                    print()
                    self.startTimeF = datetime.strptime(self.startTime, '%I:%M %p')
                    serviceType = Mainmenu()
                    duF = self.getDuration(serviceType, option)[0]
                    self.endTime = ((duF + self.startTimeF).time()).strftime('%I:%M %p')
                    self.unitPrice = self.getUnitPrice(service)
                    duration = self.getDuration(serviceType, option)[1]
                    totalPrice = int(duration) * self.unitPrice
                    print(f'The total price is {totalPrice}')
                if self.confirmApp():
                    conNum = int(self.confirmationId(service)) + 1
                    first_name = info['first_name'][self.client - 1]
                    last_name = info['last_name'][self.client - 1]
                    # start_time = self.startTimeF.time().strftime('%I:%M %p')
                    newRecord = {
                        "Spa Name": "Mud in Your Eye (MiYE)",
                        "Schedule Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "Client's ID": self.client,
                        'Name': f'{first_name} {last_name}',
                        'Date': self.date,
                        'Service Time': f'{self.startTime} - {self.endTime}',
                        'Duration': f'{duration} minutes',
                        'Service': service,
                        'Total price': f'$ {totalPrice}',
                        'Confirmation Number': str(conNum) + service.split(' ')[0]
                    }
                    newAddIn = {
                        'schedule_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'id': self.client,
                        'date': self.date,
                        'start_time': self.startTime,
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
                    fo = open('receipt.txt', "w")
                    for k, v in newRecord.items():
                        fo.write(str(k) + ': ' + str(v) + '\n\n')
                    fo.close()
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
        if conf.lower() == "y":
            c.execute('''SELECT MAX(id) FROM duration_price''') #get max PK from duration_price
            max_id = c.fetchall()
            c.execute('''SELECT MAX(id) FROM price''') #get max PK from price
            serv_id = c.fetchall()
            id = max_id[0][0] + 1 #creates new ID for duration_price table
            service_id = serv_id[0][0] + 1 #creates new ID for price table
            name = input("What is the NAME of the NEW SERVICE? ")
            price = float(input("What is Rate per Minute? $ "))
            c.execute('''SELECT * from duration''')
            durations = c.fetchall()
            avail_duration = []
            print ("Available Durations:")
            for duration in durations:
                print("Enter",duration[0],"for",duration[1],"minutes")
                avail_duration.append(duration[0])
            duration = int(input("What is the DURATION of the service? (ENTER ID associated with DURATION): "))
            if duration in avail_duration:
                type = int(input("What is the SERVICE TYPE of the service? (1: massage, 2: bath, 3: facial, 4: specialty): "))
            print("\nID:",id,"\nNAME:",name,"\nRATE:",price,"\nDURATION:",duration,"\nTYPE:",type,"\n")
            conf_new = input("Confirm the new service? Y/N ")
            if conf_new.lower() == 'y':
                c.execute('''INSERT INTO price (id, service, unit_price, type_id)
                VALUES(%d, '%s', %d, %d)''' % (service_id, name, price, type))
                conn.commit()
                c.execute('''INSERT INTO duration_price (id, durationid, priceid)
                VALUES(%d, %d, %d)''' % (id, duration, service_id))
                conn.commit()
                print("NEW SERVICE has been ADDED")
            elif conf_new.lower() == 'n':
                print("ADD a NEW SERVICE has been CANCELLED")
            else:
                print("Sorry, your input is not recognized, please select (Y/N)")
                return self.addNew()
        elif conf.lower() == "n":
            print("Returning to Maintenance Menu...")
            self.maintMenu()
        else:
            print("Sorry, your input is not recognized, please select (Y/N)")
            return self.addNew()
    # SEARCH for a service
    def searchService(self):
        print("\nSEARCH for a Service")
        conf = input("Is this what you want to do? Y/N ")
        if conf.lower() == "y":
            search_by = input("How would you like to search by? (1: name, 2: type) ")
            if search_by == "1":
                name = input("Service Name (exact or partial SERVICE NAMES may be entered): ")
                c.execute('''SELECT price.*, duration.duration, duration_price.id FROM price JOIN duration_price ON duration_price.priceid = price.id JOIN duration ON duration_price.durationid = duration.id WHERE price.service LIKE "%s"''' % ('%'+name+'%'))
            elif search_by == "2":
                type = int(input("Service Type (1: massage, 2: bath, 3: facial, 4: specialty): "))
                c.execute('''SELECT price.*, duration.duration, duration_price.id FROM price JOIN duration_price ON duration_price.priceid = price.id JOIN duration ON duration_price.durationid = duration.id WHERE type_id = %d''' % (type))
            rows = c.fetchall()
            print(rows)
            for row in rows:
                print("\nID:",row[5],"\nName:", row[1].upper(),"\nDuration:",row[4],"minutes" "\nRate: ${:.2f}".format(round(row[2], 2),"\nTYPE:",row[3]))
            self.searchService()
        elif conf.lower() == "n":
            print("Returning to Maintenance Menu...")
            self.maintMenu()
        else:
            print("Sorry, your input is not recognized, please select (Y/N)")
            return self.searchService()

    # UPDATE a service
    def updateService(self):
        print("\nUPDATE a Service")
        conf = input("Is this what you want to do? Y/N ")
        if conf.lower() == "y":
            update_attribute = input("What do you need to edit? (1: duration, 2: name, 3: type, 4: price) [ENTER q to quit] ")
            if update_attribute == "1": #update DURATION attribute
                c.execute('''SELECT duration_price.id,type.name, price.service, duration.duration from duration_price join price on duration_price.priceid = price.id JOIN duration ON duration_price.durationid = duration.id JOIN type ON price.type_id = type.id  ORDER BY type.name;''')
                rows = c.fetchall()
                rows_id = []
                for row in rows:
                    print(row)
                    rows_id.append(row[0])
                ask_id = int(input("Please enter the Service ID of the service you want to update: "))
                if ask_id in rows_id:
                    c.execute('''SELECT * from duration''')
                    durations = c.fetchall()
                    avail_duration = []
                    print ("Available Durations:")
                    for duration in durations:
                        print("Enter",duration[0],"for",duration[1],"minutes")
                        avail_duration.append(duration[0])
                    new_duration = int(input("Update DURATION to (ENTER ID associated with DURATION): "))
                    if new_duration in avail_duration:
                        c.execute('''UPDATE duration_price SET durationid = %d WHERE id = %d''' % (new_duration, ask_id))
                        conn.commit()
                        print("DURATION has been successfully changed")
                        return self.maintMenu()
                    else:
                        print("Sorry, the DURATION ID you entered is not recognized, ENTER another DURATION ID")
                        self.updateService()
                else:
                    print("Sorry, the SERVICE ID you entered is not recognized, ENTER another SERVICE ID")
                    self.updateService()
            elif update_attribute == "2": #update NAME attribute
                c.execute('''select id, service, unit_price from price;''')
                names = c.fetchall()
                for name in names:
                    print(name)
                ask_id = int(input("Please enter the Service ID from above of the service you want to update: "))
                new_name = input("Update NAME to: ")
                c.execute('''UPDATE price SET service = "%s" WHERE id = %d''' % (new_name, ask_id))
                conn.commit()
                print("NAME has been successfully changed")
                return self.maintMenu()
            elif update_attribute == "3": #update TYPE attribute
                c.execute('''select price.id, price.service, type.name from price JOIN type ON price.type_id = type.id;''')
                names = c.fetchall()
                for name in names:
                    print(name)
                ask_id = int(input("Please enter the Service ID from above of the service you want to update: "))
                c.execute('''select * from type;''')
                types = c.fetchall()
                for type in types:
                    print(type)
                new_type = int(input("Update TYPE to (enter type ID from above): "))
                c.execute('''UPDATE price SET type_id = "%s" WHERE id = %d''' % (new_type, ask_id))
                conn.commit()
                print("TYPE has been successfully changed to: ",new_type)
                return self.maintMenu()
            elif update_attribute == "4": #update PRICE attribute
                c.execute('''select id, service, unit_price from price;''')
                prices = c.fetchall()
                for price in prices:
                    print(price)
                ask_id = int(input("Please enter the Service ID from above of the service you want to update: "))
                new_price = float(input("Update PRICE to (do not enter dollar sign ($)): "))
                c.execute('''UPDATE price SET unit_price = %d WHERE id = %d''' % ((new_price), ask_id))
                conn.commit()
                print("PRICE has been successfully changed to: ${:.2f}".format(new_price))
                return self.maintMenu()
            elif update_attribute.lower() == "q":
                print("Returning to Maintenance Menu...")
                return self.maintMenu()
            else:
                print("Sorry, your input is not recognized, please select (Y/N)")
                return
        elif conf.lower() == "n":
            print("Returning to Maintenance Menu...")
            return self.maintMenu()
        else:
            print("Sorry, your input is not recognized, please select (Y/N)")
            return self.updateService()

    #print a list of services and their prices
    def pricelist(self):
        print("\nMud In Your Eye - Services\n")
        c.execute('''SELECT duration_price.id,type.name, price.service, duration.duration, (duration.duration * price.unit_price) AS total from duration_price join price on duration_price.priceid = price.id JOIN duration ON duration_price.durationid = duration.id JOIN type ON price.type_id = type.id  ORDER BY type.name;''')
        rows = c.fetchall()
        # new code for price list
        c.execute('''SELECT DISTINCT type.name, price.service FROM type JOIN price on type.id = price.type_id''')
        list = c.fetchall()
        c.execute('''SELECT DISTINCT name FROM type''')
        type = c.fetchall()

        service_listing = [] # list of all the services
        type_listing = []
        for x in list: # creating list of services
            service_listing.append(x[0:2])
        for j in type: # creating list of types: bath, massage, specialty, facial
            type_listing.append(j[0])
        #creates list of services to print out
        for k in type_listing:
            print(k)
            for i in service_listing:
                if i[0] == k:
                    print("\t",i[1])
                    for row in rows:
                        if row[2] == i[1]:
                            print("\t\t","Duration:",row[3],"|", "Price: ${:.2f}".format(round(row[4], 2)))
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
            self.maintlogIn()

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
                # conn.close()
                login = Login()
                login.logIn()
                # self.maintMenu()
            elif selection ==6:
                print("\n\nMiYE Application closing...\n")
                conn.close()
                print("Database connection closed...")
                sys.exit("\nGOODBYE!\n")
            else:
                print ("Invalid Choice. Please select an option from 1-6:")


class Modification(object):
    def __init__(self):
        self.primary_query = """SELECT services.id, first_name, last_name, service, date, start_time, end_time, total_price, confirmation 
                FROM services 
                INNER JOIN clients 
                ON services.id = clients.id"""


    def lookupMenuOptions(self):
        print("\nLOOKUP\n")
        print("1. Search by date")
        print("2. Search by service type")
        print("3. Search by confirmation number")
        print("4. Search by client name")
        print("5. Search for open sessions\n")
        print("Please type the number of the search option you would like to use,")
        print("then press ENTER or RETURN.")

    def searchServices(self):
        loop = True
        while loop:
            self.lookupMenuOptions()
            choice = input()
            if choice == "1":
                self.searchByDate()
                main = Mainmenu()
                main.chooseMenu()
            elif choice == "2":
                self.searchServiceType()
                main = Mainmenu()
                main.chooseMenu()
            elif choice == "3":
                self.searchConfirmationNum()
                main = Mainmenu()
                main.chooseMenu()
            elif choice == "4":
                self.searchClientName()
                main = Mainmenu()
                main.chooseMenu()
            elif choice == "5":
                self.searchOpenSessions()
                login = Login()
                login.logIn()
            else:
                print("Sorry, we couldn't recognize that.")

    #get the date the user wants to search for
    #verifies that the date is in the correct format
    def getSearchDate(self):
        loop = True
        while loop:
            print("\n")
            print("Please enter the date you would like to search for in YYYY-MM-DD format.")
            print("For example: 2020-03-21")
            raw_date = input()
            try:
                search_date = datetime.strptime(raw_date, '%Y-%m-%d')
            except ValueError:
                print("Sorry, we could not recognize that.")
            else:
                return(search_date)

    #allows the user to search for all services scheduled on a given day
    def searchByDate(self):
        search_date = self.getSearchDate()
        # conn = sqlite3.connect(project_database)
        cursor = conn.execute(self.primary_query)
        for row in cursor:
            schedules_date = datetime.strptime(row[4], '%Y-%m-%d')
            if schedules_date == search_date:
                self.printSearchResult(row)
        print("\nEND OF RESULTS")
        # conn.close()

    #allows the user to search for all services of a specific type
    #and that are scheduled on a particular day
    def searchServiceType(self):
        print("\n")
        print("Please enter the service type you would like to search for.")
        search_service = input()
        search_date = self.getSearchDate()

        # conn = sqlite3.connect(project_database)
        cursor = conn.execute(self.primary_query)
        for row in cursor:
            schedules_date = datetime.strptime(row[4], '%Y-%m-%d')
            if schedules_date == search_date:
                if search_service == row[3]:
                    self.printSearchResult(row)
        print("\nEND OF RESULTS")
        # conn.close()

    #allows the user to find a service by its confirmation id
    def searchConfirmationNum(self):
        print("\n")
        print("Please enter the confirmation number you would like to search for.")
        search_conf_num = input()

        # conn = sqlite3.connect(project_database)
        cursor = conn.execute(self.primary_query)
        for row in cursor:
            if search_conf_num == row[8]:
                self.printSearchResult(row)
        print("\nEND OF RESULTS")
        # conn.close() 

    def searchClientName(self):
        print("\n")
        print("Please enter the client's first name.")
        first_name = input()
        print("\nPlease enter the client's last name.")
        last_name = input()

        # conn = sqlite3.connect(project_database)
        cursor = conn.execute(self.primary_query)
        for row in cursor:
            if last_name == row[2] and first_name == row[1]:
                self.printSearchResult(row)
        print("\nEND OF RESULTS")
        # conn.close() 

    def searchOpenSessions(self):
        availability_dict = {
            '08:00 AM' : 'Available',
            '08:30 AM' : 'Available',
            '09:00 AM' : 'Available',
            '09:30 AM' : 'Available',
            '10:00 AM' : 'Available',
            '10:30 AM' : 'Available',
            '11:30 AM' : 'Available',
            '12:00 PM' : 'Available',
            '12:30 PM' : 'Available',
            '01:00 PM' : 'Available',
            '01:30 PM' : 'Available',
            '02:00 PM' : 'Available',
            '02:30 PM' : 'Available',
            '03:00 PM' : 'Available',
            '03:30 PM' : 'Available',
            '04:00 PM' : 'Available',
            '04:30 PM' : 'Available',
            '05:00 PM' : 'Available',
            '05:30 PM' : 'Available',
            '06:00 PM' : 'Available',
            '06:30 PM' : 'Available',
            '07:00 PM' : 'Available',
            '07:30 PM' : 'Available'
        }

        print("\n")
        print("Please enter the client's ID.")
        client_id = input()
        search_date = self.getSearchDate()
        print("\nPlease enter the service to search for.")
        search_service = input()

        # conn = sqlite3.connect(project_database)
        cursor = conn.execute(self.primary_query)
        for row in cursor:
            schedules_date = datetime.strptime(row[4], '%Y-%m-%d')
            if schedules_date == search_date:
                if search_service == row[3] or int(client_id) == int(row[0]):
                    availability_dict[row[5]] = '-'
        
        print("\nAvailable sessions for " + search_service)
        for i in availability_dict:
            print(i, availability_dict[i])

                    


    #this function takes in a row from the database and 
    #prints out the services in an easy to read format
    def printSearchResult(self, row):
            print("\n")
            print(" Client ID: ", row[0])
            print("First Name: ", row[1])
            print(" Last Name: ", row[2])
            print("   Service: ", row[3])
            print("      Date: ", row[4])
            print("      Time: ", row[5],"-",row[6])
            print("     Price: ", ("$"+str(row[7])))
            print(" Confirm #: ", (row[8]))

class Change(object):
    def __init__(self):
        pass
    

login = Login()
login.logIn()

# conn = sqlite3.connect('project1.db')
# c = conn.cursor()
# table = c.execute('SELECT * FROM services')
# for row in table:
#     print(row)
