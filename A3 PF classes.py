class Employee:
    def __init__(self, EmployeeName="", EmployeeID="", EmployeeDepartment="", EmployeeAge=""):
        self.EmployeeName = EmployeeName
        self.EmployeeID = EmployeeID
        self.EmployeeDepartment = EmployeeDepartment
        self.EmployeeAge = EmployeeAge

    def getEmployeeName(self):
        return self.EmployeeName

    def setEmployeeName(self, name):
        self.EmployeeName = name

    def getEmployeeID(self):
        return self.EmployeeID

    def setEmployeeID(self, id):
        self.EmployeeID = id

    def getEmployeeDepartment(self):
        return self.EmployeeDepartment

    def setEmployeeDepartment(self, department):
        self.EmployeeDepartment = department

    def getEmployeeAge(self):
        return self.EmployeeAge

    def setEmployeeAge(self, age):
        self.EmployeeAge = age


class Event:
    def __init__(self, EventName="", EventDate="", EventLocation=""):
        self.EventName = EventName
        self.EventDate = EventDate
        self.EventLocation = EventLocation

    def getEventName(self):
        return self.EventName

    def setEventName(self, name):
        self.EventName = name

    def getEventDate(self):
        return self.EventDate

    def setEventDate(self, date):
        self.EventDate = date

    def getEventLocation(self):
        return self.EventLocation

    def setEventLocation(self, location):
        self.EventLocation = location


class Client:
    def __init__(self, ClientName="", ClientID="", ClientEmail="", ClientPhone=""):
        self.ClientName = ClientName
        self.ClientID = ClientID
        self.ClientEmail = ClientEmail
        self.ClientPhone = ClientPhone

    def getClientName(self):
        return self.ClientName

    def setClientName(self, name):
        self.ClientName = name

    def getClientID(self):
        return self.ClientID

    def setClientID(self, id):
        self.ClientID = id

    def getClientEmail(self):
        return self.ClientEmail

    def setClientEmail(self, email):
        self.ClientEmail = email

    def getClientPhone(self):
        return self.ClientPhone

    def setClientPhone(self, phone):
        self.ClientPhone = phone


class Guest:
    def __init__(self, GuestName="", GuestID="", GuestEmail="", GuestPhone=""):
        self.GuestName = GuestName
        self.GuestID = GuestID
        self.GuestEmail = GuestEmail
        self.GuestPhone = GuestPhone

    def getGuestName(self):
        return self.GuestName

    def setGuestName(self, name):
        self.GuestName = name

    def getGuestID(self):
        return self.GuestID

    def setGuestID(self, id):
        self.GuestID = id

    def getGuestEmail(self):
        return self.GuestEmail

    def setGuestEmail(self, email):
        self.GuestEmail = email

    def getGuestPhone(self):
        return self.GuestPhone

    def setGuestPhone(self, phone):
        self.GuestPhone = phone


class Supplier:
    def __init__(self, name="", supplier_id="", email="", phone=""):
        self.name = name
        self.id = supplier_id
        self.email = email
        self.phone = phone

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

from datetime import datetime

class Employee:
    def __init__(self, EmployeeName="", EmployeeID="", EmployeeDepartment="", EmployeeAge=""):
        self.EmployeeName = EmployeeName
        self.EmployeeID = EmployeeID
        self.EmployeeDepartment = EmployeeDepartment
        self.EmployeeAge = EmployeeAge

    def display_info(self):
        print("Name:", self.EmployeeName)
        print("ID:", self.EmployeeID)
        print("Department:", self.EmployeeDepartment)
        print("Age:", self.EmployeeAge)

class Event:
    def __init__(self, EventName="", EventDate="", EventLocation=""):
        self.EventName = EventName
        self.EventDate = EventDate
        self.EventLocation = EventLocation

    def display_info(self):
        print("Name:", self.EventName)
        print("Date:", self.EventDate)
        print("Location:", self.EventLocation)

class Client:
    def __init__(self, ClientName="", ClientID="", ClientEmail="", ClientPhone=""):
        self.ClientName = ClientName
        self.ClientID = ClientID
        self.ClientEmail = ClientEmail
        self.ClientPhone = ClientPhone

    def display_info(self):
        print("Name:", self.ClientName)
        print("ID:", self.ClientID)
        print("Email:", self.ClientEmail)
        print("Phone:", self.ClientPhone)

class Guest:
    def __init__(self, GuestName="", GuestID="", GuestEmail="", GuestPhone=""):
        self.GuestName = GuestName
        self.GuestID = GuestID
        self.GuestEmail = GuestEmail
        self.GuestPhone = GuestPhone

    def display_info(self):
        print("Name:", self.GuestName)
        print("ID:", self.GuestID)
        print("Email:", self.GuestEmail)
        print("Phone:", self.GuestPhone)

class Supplier:
    def __init__(self, name="", supplier_id="", email="", phone=""):
        self.name = name
        self.id = supplier_id
        self.email = email
        self.phone = phone

    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Email:", self.email)
        print("Phone:", self.phone)

# Test Cases
# Creating objects of the Employee class
employee1 = Employee("Reem", "E001", "HR", 30)
employee2 = Employee("Majed", "E002", "Finance", 35)

# Creating objects of the Event class
event1 = Event("Conference", "2024-06-15", "Convention Center")
event2 = Event("Product Launch", "2024-07-20", "Exhibition Hall")

# Creating objects of the Client class
client1 = Client("Nouf", "C001", "xyz@example.com", "123-456-7890")
client2 = Client("Hajer", "C002", "abc@example.com", "987-654-3210")

# Creating objects of the Guest class
guest1 = Guest("Reem", "G001", "alice@example.com", "111-222-3333")
guest2 = Guest("Hajer", "G002", "bob@example.com", "444-555-6666")

# Creating objects of the Supplier class
supplier1 = Supplier("coffee truck", "S001", "supplier1@example.com", "999-888-7777")
supplier2 = Supplier("Supplier 2", "S002", "supplier2@example.com", "777-888-9999")

# Displaying Employee info
print("Employee Info:")
employee1.display_info()
employee2.display_info()
print()

# Displaying Event info
print("Event Info:")
event1.display_info()
event2.display_info()
print()

# Displaying Client info
print("Client Info:")
client1.display_info()
client2.display_info()
print()

# Displaying Guest info
print("Guest Info:")
guest1.display_info()
guest2.display_info()
print()

# Displaying Supplier info
print("Supplier Info:")
supplier1.display_info()
supplier2.display_info()