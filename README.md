# Mud In Your Eye SPA Reservation CML Application: 

## Objective: CML Application for Scheduling, availabile timeslot checking, appointment modification, system maintenance by manager
1. Mud in your eye operation hours: 08:00 AM - 08:00 PM
2. Services offered: 
  - Facial: normal facial & collagen facial
  - Massage: sedish massage & shiatsu massage & deep tissue
  - Mineral Bath
  - Sepcialty Treatment: hot stone & sugar scrub & herbal body wrap & botanical mud wrap
3. Login system: 
  - all front desk staffs have one password to access to the main menu: services scheduling and availability checking, appointment modification
  - Manager has access to the system maintenance menu: price, service, time adjustment
## Implementation: 
 - Python: Pandas, datetime, getpass, enum
 - Database: SQLite
 - Testing: Unit test with print out certain instances, system test with running the application directly (follow a user's case to run the application) 
### Main menu display:
<img src='main_menu.JPG'>
 
#### Application is able to check if the client is in our resort database, and if the service date is within the range of client's stay, example shows below:
<img src='check_date.jpg'>

#### Application is able to check if appointment time is booked by other clients, and if the time is within the operation hours, example shows below:
<img src='check_time.jpg'>

#### Application is able to generate a receipt with scheduling details and confirmation number, and it will save as a text file, so staffs are able to print out for client.
<img src = 'receipt.jpg'>

#### The end of the day, staffs are able to quit the system. 
<img src = 'quit.jpg'>
