# import dependencies
import getpass
from enum import Enum
import pandas as pd
from datetime import datetime, timedelta
import sqlite3
import sys

# connect the sqlitedb
conn = sqlite3.connect('project.db')
c = conn.cursor()

conn = sqlite3.connect('services.db')
# conn.close()
conn = sqlite3.connect('services.db')
c = conn.cursor()
c.execute('''SELECT * FROM service''')

print(c.fetchall())
c.execute('''SELECT * FROM type''')
print(c.fetchall())
c.execute('''SELECT * FROM users''')
names = list(map(lambda x: x[0], c.description))
print(names)
print(c.fetchall())

# create dataframe from csv files:
# clientdf = pd.read_csv('MOCK_DATA.csv')
# servicedf = pd.read_csv('service.csv')
# pricedf = pd.read_csv('price.csv')
# # get the date in right format
# clientdf['start_date'] =pd.to_datetime(clientdf['start_date'])
# clientdf['end_date'] =pd.to_datetime(clientdf['end_date'])
# # import csv into table 'clients', 'services', 'price' in sqlite3
# clientdf.to_sql('clients',conn, if_exists='replace',index = False)
# servicedf.to_sql('services',conn, if_exists='replace',index = False)
# pricedf.to_sql('price',conn,if_exists='replace',index = False)


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
#             1: '30',
#             2: '60'
#         }

#     def printOption(self,option=MenuOption.mainMenu.value):
#         """
#         functin to display differnt layers of menu
#         arguments: integer that matches the Menuoption enum class
#         """
#         if option == MenuOption.mainMenu.value:
#             print("Main Menu")
#             print()
#             for i in self.main_menu:
#                 print(i,self.main_menu[i])
#             print()
#         elif option == MenuOption.facial.value:
#             print("Facial Scheduling: Choose a time option. Input 1 for 30 min, 2 for 60 min.")
#             print()
#             for i in self.facial:
#                 print(i,self.facial[i])
#             print()

#     def chooseMenu(self):
#         self.printOption()
#         self.userChoice = input("Type the number of the option you want, then press ENTER or RETURN.")
#         self.response = True
#         while self.response:
#             if self.userChoice=='1':
#                 self.printOption(2)   # printout facial menu, 2 is number in MenuOption
#                 facial = Reservation()
#                 _min = input("Type the number of the option you want, then press ENTER or RETURN.")
#                 facial.facial('facial',_min)
#                 self.response = False

#             elif self.userChoice == '6': #ADDED MAINTENANCE MODULE HERE
#                 conn = sqlite3.connect('services.db')
#                 c = conn.cursor()

#                 class maint(object):
#                     def __init___(self):
#                         pass
#                     # adds a new service to SERVICE table
#                     def addNew(self):
#                         print("Adding a new service")
#                         conf = input("Is this what you want to do? Y/N ")
#                         if conf == "Y":
#                             c.execute('''SELECT MAX(service_id) FROM service''')
#                             max_id = c.fetchall()
#                             id = max_id[0][0] + 1
#                             name = input("Service Name: ")
#                             price = float(input("Service Rate per Minute: "))
#                             duration = int(input("Service Duration: "))
#                             type = int(input("Service Type (1: massage, 2: bath, 3: facial, 4: specialty): "))
#                             print("ID:",id,"NAME:",name,"RATE:",price,"DURATION:",duration,"TYPE:",type)
#                             conf_new = input("Confirm the new service? Y/N ")
#                             if conf_new == 'Y':
#                                 c.execute('''INSERT INTO service (service_id, service_name, price, duration, type)
#                                 VALUES(%d, '%s', %d, %d, %d)''' % (id, name, price, duration, type))
#                                 conn.commit()
#                                 print("New service has been added")
#                             elif conf_new == 'N':
#                                 print("New service has been cancelled")

#                         elif conf == "N":
#                             print("Returning to Maintenance Menu...")

#                     # search the SERVICE table for a service
#                     def searchService(self):
#                         print("Search for a service")
#                         conf = input("Is this what you want to do? Y/N ")
#                         if conf == "Y":
#                             search_by = int(input("How would you like to search by? (1: ID, 2: name, 3: type) "))
#                             if search_by == 1:
#                                 id = int(input("Service ID: "))
#                                 c.execute('''SELECT * FROM service WHERE service_id = %d''' % (id))
#                             if search_by == 2:
#                                 name = input("Service Name: ")
#                                 c.execute('''SELECT * FROM service WHERE service_name = "%s"''' % (name))
#                             if search_by == 3:
#                                 type = int(input("Service Type (1: massage, 2: bath, 3: facial, 4: specialty): "))
#                                 c.execute('''SELECT * FROM service WHERE type = %d''' % (type))
#                             rows = c.fetchall()
#                             for row in rows:
#                                 print("ID:",row[0],"|","NAME:", row[4], "|","Duration:",row[2],"|", "Rate: $",round(row[1], 2),"|","TYPE:",row[3])

#                         elif conf == "N":
#                             print("Returning to Maintenance Menu...")

#                     # update a service in SERVICE table
#                     def updateService(self):
#                         print("Updating a service")
#                         conf = input("Is this what you want to do? Y/N ")
#                         if conf == "Y":
#                             ask_id = int(input("Service ID: "))
#                             update_attribute = int(input("What do you need to edit? (1: duration, 2: name, 3: type, 4: price)"))
#                             if update_attribute == 1: #update DURATION attribute
#                                 new_duration = int(input("Update duration to: "))
#                                 c.execute('''UPDATE service SET duration = %d WHERE service_id = %d''' % (new_duration, ask_id))
#                                 conn.commit()
#                                 print("DURATION has been successfully changed to: ",new_duration, 'minutes')
#                             elif update_attribute == 2: #update NAME attribute
#                                 new_name = input("Update name to: ")
#                                 c.execute('''UPDATE service SET service_name = "%s" WHERE service_id = %d''' % (new_name, ask_id))
#                                 conn.commit()
#                                 print("NAME has been successfully changed to: ",new_name)
#                             elif update_attribute == 3: #update TYPE attribute
#                                 new_type = int(input("Update type to (1: massage, 2: bath, 3: facial, 4: specialty): "))
#                                 c.execute('''UPDATE service SET type = "%s" WHERE service_id = %d''' % (new_type, ask_id))
#                                 conn.commit()
#                                 print("TYPE has been successfully changed to: ",new_type)
#                             elif update_attribute == 4: #update PRICE attribute
#                                 new_price = int(input("Update price to: "))
#                                 c.execute('''UPDATE service SET price = %d WHERE service_id = %d''' % (new_price, ask_id))
#                                 conn.commit()
#                                 print("PRICE has been successfully changed to: $",float(new_price))
#                         elif conf == "N":
#                             print("Returning to Maintenance Menu...")

#                     def pricelist(self):
#                         print("\nMud In Your Eye - Services\n")
#                         c.execute('''SELECT service_name, duration, (duration*price) AS 'total price' FROM service ORDER BY type''')
#                         rows = c.fetchall()
#                         # new code for price list
#                         c.execute('''SELECT DISTINCT type.type, service.service_name FROM type JOIN service on type.type_id = service.type''')
#                         list = c.fetchall()
#                         c.execute('''SELECT DISTINCT type FROM type''')
#                         type = c.fetchall()

#                         service_listing = [] # list of all the services
#                         type_listing = []
#                         for x in list: # creating list of services
#                             service_listing.append(x[0:2])
#                         for j in type: # creating list of types: bath, massage, specialty, facial
#                             type_listing.append(j[0])
#                         #print("this is type list", type)
#                         #print("this is service list", list)
#                         #print("after append", service_listing)

#                         #creates list of services to print out
#                         for k in type_listing:
#                             print(k)
#                             for i in service_listing:
#                                 if i[0] == k:
#                                     print("\t",i[1])
#                                     for row in rows:
#                                         if row[0] == i[1]:
#                                             print("\t\t","Duration:",row[1],"|", "Price: $",round(row[2], 2))
#                             print("\n")
#                         print("\n")


#                     def maintlogIn(self):
#                         print('Welcome to the Maintenance Module\nPlease type your USERNAME and PASSWORD below then press ENTER or RETURN.')
#                         #getpass library hides the password
#                         username = input("USERNAME: ")
#                         password = getpass.getpass('PASSWORD: ')
#                         c.execute('''SELECT * FROM users WHERE name = "%s"''' % (username))
#                         user = c.fetchall()
#                         if password == user[0][2]:
#                             self.maintMenu()
#                         else:
#                             print("Sorry, but that password is not recognized. Please try again.")
#                             self.logIn()

#                     def maintMenu(self):
#                         while True:
#                             print("""
#                             ***MAINTENANCE MENU***
#                             1. SEARCH for a service
#                             2. ADD a new service
#                             3. UPDATE a current service
#                             4. PRINT a list of ALL services
#                             5. Return to Scheduling System
#                             6. Sign Out or Quit\n""")

#                             selection = int(input("Select your Maintenance Menu option: "))
#                             if selection ==1:
#                                 self.searchService()
#                             elif selection ==2:
#                                 self.addNew()
#                             elif selection ==3:
#                                 self.updateService()
#                             elif selection ==4:
#                                 self.pricelist()
#                             elif selection ==5:
#                                 print("Launching Scheduling System...")
#                                 conn.close()
#                                 login = Login()
#                                 login.logIn()
#                             elif selection ==6:
#                                 print("\n\nMiYE Application closing...\n")
#                                 conn.close()
#                                 print("Database connection closed...")
#                                 sys.exit("\nGOODBYE!\n")
#                             else:
#                                 print ("Invalid Choice. Please select an option from 1-6:")
#                 maintenance = maint()
#                 maintenance.maintlogIn()

#             elif self.userChoice=='7':
#                 user = input("Do you want to quit or logout? 1. Sign Out or 2. Quit.")
#                 if user == '1':
#                     login = Login()
#                     login.logIn()
#                     self.response = False
#                 else:
#                     print("You are leaving, good bye!")
#                     exit()

#             else:
#                 print( "Sorry, that is not a recognized command. Please type the number for one of the above options and press ENTER or RETURN.")
#                 self.printOption()
#                 self.userChoice = input("Type the number of the option you want, then press ENTER or RETURN.")
#                 response = True

# # Login class handles all the login function and handling login errors
# class Login(object):
#     def __init__(self):
#         self.password = None
#         self.userChoice = None

#     def logIn(self):
#         print('Please type your password below then press ENTER or RETURN.')
#         # getpass library hides the password
#         self.password = getpass.getpass('Password: ')
#         if self.password == 'admin':
#             main = Mainmenu()
#             main.chooseMenu()
#         else:
#             print("Sorry, but that password is not recognized. Please try again.")
#             self.logIn()

# class Reservation(object):
#     def __init__(self):
#         pass
#     def getInfoFromTable(self,tableName,columnName):
#         """
#         This function is able to return the informatin that you query
#         takes 2 arguements, the table's name, and the column's name, and return a list of records.
#         """
#         infor = []
#         clientTable = c.execute(f'SELECT {columnName} FROM {tableName}')
#         for row in clientTable:
#             infor.append(row[0])
#         return infor
#     # def getDateFromTable(self, tableName,columnName,matchcolumn,where):
#     #     dateInfo = []
#     #     values = c.execute(f'SELECT {columnName} FROM {tableName} WHERE {matchcolumn} = {where}')
#     #     for value in values:
#     #         dateInfo.append(value[0])
#     #     print(dateInfo)

#     def getClientID(self):
#         """
#         this recursive function is able to check if the client's id is in the db;
#         if yes, will return the client's id; if no, will throw an error msg and ask to try again
#         """
#         self.client = int(input("What is your client ID? Please input numbers only"))
#         self.clientID = self.getInfoFromTable('clients','id')
#         if self.client in self.clientID:
#             return(self.client)
#         else:
#             print("Sorry, the client's ID is not in the Resert Database.")
#             self.getClientID()
#     def getUnitPrice(self,service):
#         """
#         this function return the unit price that matches with the service
#         one argument: string, service like facial, massage, mineral bath, specialty treatment
#         """
#         self.unitPrice = int(self.getInfoFromTable('price','unit_price')[0])
#         return self.unitPrice
#     def checkDate(self,client):
#         """
#         this recursive function will check if the input date match with the client's stay at the resort;
#         if yes, it will return the input date for service scheduling, if no, will prompt to select another date
#         one argument: client's id
#         """
#         self.date = input('What date would like to schedule the service?')
#         self.date = datetime.strptime(self.date,'%m/%d/%Y').date()
#         info = clientdf.loc[clientdf['id']==client]
#         if self.date>= info['start_date'][self.client-1] and self.date <= info['end_date'][self.client-1]:
#             return self.date
#         else:
#             print('Sorry, the selected date is not within your stay at the resort. Please select a date during the time you are here.')
#             self.checkDate(client)
#     def checkTime(self,service):
#         """
#         this recursive function will check if input time is available for this service, if yes will return the start time, if no will prompt user to select another time
#         one argument: service like facial, massage, mineral bath or specialty treatment.
#         也要查结束时间是否可行
#         """
#         self.startTime = input("What is the start time?")
#         timeDf = servicedf.loc[servicedf['date']==self.date]
#         if self.startTime in str(timeDf['start_time']):
#             print('Sorry, the selected time is not available. Please select another time.')
#             self.checkTime(service)
#         else:
#             return self.startTime

#     def getDuration(self,service,option):
#         """
#         this function return service duration that selected from the menu option
#         it return 1. formated duration time 2. string of duration
#         2 arguments: service, menuOption of duration
#         这个service的选项有必要吗？
#         """
#         self.duration = service.facial[int(option)]
#         duF = timedelta(minutes=int(self.duration))
#         return duF, self.duration
#     def confirmApp(self,service):
#         """
#         this function will prompt user to confirm the appointment, if yes, return True, if no, return to the main menu
#         one argument: service
#         这个service选项有必要吗？
#         """
#         confInput = input('Would you like to confirm your appointment? (Y/N)')
#         if confInput == 'Y':
#             return True
#         elif confInput == 'N':
#             main = Mainmenu()
#             main.chooseMenu()
#         else:
#             print("Sorry, your input is not recognized, please select (Y/N)")
#             self.confirmApp()

#     def facial(self,service,option):
#         self.client = self.getClientID()
#         if self.client:
#             pricePerMin = self.getUnitPrice(service)
#             info = clientdf.loc[clientdf['id']== self.client]
#             if self.checkDate(self.client):
#                 if self.checkTime(service):
#                     self.startTimeF = datetime.strptime(self.startTime,'%I:%M %p')
#                     facial = Mainmenu()
#                     duF = self.getDuration(facial,option)[0]
#                     self.endTime = ((duF+self.startTimeF).time()).strftime('%I:%M %p')
#                     self.unitPrice = self.getUnitPrice(service)
#                     duration = self.getDuration(facial,option)[1]
#                     totalPrice = int(duration)*self.unitPrice
#                     print(f'The total price is {totalPrice}')
#                     # confInput = input('Would you like to confirm your appointment? (Y/N)')
#                     if self.confirmApp(service):
#                         print(f'Your confirmation code is {str(101)+service}.')       #要改confirmation number
#                         self.servicedf = servicedf.append({
#                             'id':self.client,
#                             'first_name': info['first_name'][1],
#                             'last_name': info['last_name'][1],
#                             'date': self.date,
#                             'start_time': self.startTimeF.time().strftime('%I:%M %p'),
#                             'end_time': self.endTime,
#                             'duration': duration,
#                             'service': service,
#                             'total_price': totalPrice,
#                             'confirmation': str(101)+service
#                         }, ignore_index=True)
#                         print(self.servicedf)

# login = Login()
# login.logIn()
