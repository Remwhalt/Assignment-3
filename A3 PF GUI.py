import tkinter as tk
import pickle
from tkinter import ttk

class Employee:
    def __init__(self, EmployeeName="", EmployeeID="", EmployeeDepartment="", EmployeeAge=""):
        self.EmployeeName = EmployeeName
        self.EmployeeID = EmployeeID
        self.EmployeeDepartment = EmployeeDepartment
        self.EmployeeAge = EmployeeAge

    def getEmployeeName(self):
        return self.EmployeeName

    def getEmployeeID(self):
        return self.EmployeeID

    def getEmployeeDepartment(self):
        return self.EmployeeDepartment

    def getEmployeeAge(self):
        return self.EmployeeAge

class Event:
    def __init__(self, EventName="", EventDate="", EventLocation=""):
        self.EventName = EventName
        self.EventDate = EventDate
        self.EventLocation = EventLocation

    def getEventName(self):
        return self.EventName


    def getEventDate(self):
        return self.EventDate

    def getEventLocation(self):
        return self.EventLocation

class Client:
    def __init__(self, ClientName="", ClientID="", ClientEmail="", ClientPhone=""):
        self.ClientName = ClientName
        self.ClientID = ClientID
        self.ClientEmail = ClientEmail
        self.ClientPhone = ClientPhone

class Guest:
    def __init__(self, GuestName="", GuestID="", GuestEmail="", GuestPhone=""):
        self.GuestName = GuestName
        self.GuestID = GuestID
        self.GuestEmail = GuestEmail
        self.GuestPhone = GuestPhone

class Supplier:
    def __init__(self, name="", supplier_id="", email="", phone=""):
        self.name = name
        self.id = supplier_id
        self.email = email
        self.phone = phone

class EmployeeGUI:
    def __init__(self, employees):
        self.employees = employees
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Employee Form")
        self.EmployeeName_label = tk.Label(self.root, text="Employee Name:")
        self.EmployeeName_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.EmployeeName_entry = tk.Entry(self.root)
        self.EmployeeName_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        self.EmployeeID_label = tk.Label(self.root, text="Employee ID:")
        self.EmployeeID_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.EmployeeID_entry = tk.Entry(self.root)
        self.EmployeeID_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        self.EmployeeDepartment_label = tk.Label(self.root, text="Employee department:")
        self.EmployeeDepartment_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.EmployeeDepartment_entry = tk.Entry(self.root)
        self.EmployeeDepartment_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        self.EmployeeAge_label = tk.Label(self.root, text="Age:")
        self.EmployeeAge_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.EmployeeAge_entry = tk.Entry(self.root)
        self.EmployeeAge_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
        self.root.mainloop()

    def clearBoxes(self):
        self.EmployeeName_entry.delete(0, tk.END)
        self.EmployeeID_entry.delete(0, tk.END)
        self.EmployeeDepartment_entry.delete(0, tk.END)
        self.EmployeeAge_entry.delete(0, tk.END)

    def submit(self):
        EmployeeName = self.EmployeeName_entry.get()
        EmployeeID = self.EmployeeID_entry.get()
        EmployeeDepartment = self.EmployeeDepartment_entry.get()
        EmployeeAge = self.EmployeeAge_entry.get()

        employee_instance = Employee(EmployeeName, EmployeeID, EmployeeDepartment, EmployeeAge)
        self.employees[EmployeeID] = employee_instance
        self.clearBoxes()
        print("Employee added successfully. Name: " + EmployeeName)


class EventGUI:
    def __init__(self, events):
        self.events = events
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Event Form")

        self.EventName_label = tk.Label(self.root, text="Event Name:")
        self.EventName_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.EventName_entry = tk.Entry(self.root)
        self.EventName_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        self.EventDate_label = tk.Label(self.root, text="Event Date:")
        self.EventDate_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.EventDate_entry = tk.Entry(self.root)
        self.EventDate_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.EventLocation_label = tk.Label(self.root, text="Event Location:")
        self.EventLocation_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.EventLocation_entry = tk.Entry(self.root)
        self.EventLocation_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        self.EventName_entry.delete(0, tk.END)
        self.EventDate_entry.delete(0, tk.END)
        self.EventLocation_entry.delete(0, tk.END)

    def submit(self):
        EventName = self.EventName_entry.get()
        EventDate = self.EventDate_entry.get()
        EventLocation = self.EventLocation_entry.get()

        event_instance = Event(EventName, EventDate, EventLocation)
        event_id = len(self.events) + 1  # Generate a unique ID for the event
        self.events[event_id] = event_instance
        self.clearBoxes()
        print("Event added successfully. Name: " + EventName)

class ClientGUI:
    def __init__(self, clients):
        self.clients = clients
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Client Form")

        self.ClientName_label = tk.Label(self.root, text="Client Name:")
        self.ClientName_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.ClientName_entry = tk.Entry(self.root)
        self.ClientName_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        self.ClientID_label = tk.Label(self.root, text="Client ID:")
        self.ClientID_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.ClientID_entry = tk.Entry(self.root)
        self.ClientID_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.ClientEmail_label = tk.Label(self.root, text="Client Email:")
        self.ClientEmail_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.ClientEmail_entry = tk.Entry(self.root)
        self.ClientEmail_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.ClientPhone_label = tk.Label(self.root, text="Client Phone:")
        self.ClientPhone_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.ClientPhone_entry = tk.Entry(self.root)
        self.ClientPhone_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        self.ClientName_entry.delete(0, tk.END)
        self.ClientID_entry.delete(0, tk.END)
        self.ClientEmail_entry.delete(0, tk.END)
        self.ClientPhone_entry.delete(0, tk.END)

    def submit(self):
        ClientName = self.ClientName_entry.get()
        ClientID = self.ClientID_entry.get()
        ClientEmail = self.ClientEmail_entry.get()
        ClientPhone = self.ClientPhone_entry.get()

        client_instance = Client(ClientName, ClientID, ClientEmail, ClientPhone)
        self.clients[ClientID] = client_instance  # Use ClientID as the key
        self.clearBoxes()
        print("Client added successfully. Name: " + ClientName)


class GuestGUI:
    def __init__(self, guests):
        self.guests = guests
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Guest Form")

        self.GuestName_label = tk.Label(self.root, text="Guest Name:")
        self.GuestName_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.GuestName_entry = tk.Entry(self.root)
        self.GuestName_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        self.GuestID_label = tk.Label(self.root, text="Guest ID:")
        self.GuestID_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.GuestID_entry = tk.Entry(self.root)
        self.GuestID_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.GuestEmail_label = tk.Label(self.root, text="Guest Email:")
        self.GuestEmail_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.GuestEmail_entry = tk.Entry(self.root)
        self.GuestEmail_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.GuestPhone_label = tk.Label(self.root, text="Guest Phone:")
        self.GuestPhone_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.GuestPhone_entry = tk.Entry(self.root)
        self.GuestPhone_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        self.GuestName_entry.delete(0, tk.END)
        self.GuestID_entry.delete(0, tk.END)
        self.GuestEmail_entry.delete(0, tk.END)
        self.GuestPhone_entry.delete(0, tk.END)

    def submit(self):
        GuestName = self.GuestName_entry.get()
        GuestID = self.GuestID_entry.get()
        GuestEmail = self.GuestEmail_entry.get()
        GuestPhone = self.GuestPhone_entry.get()

        guest_instance = Guest(GuestName, GuestID, GuestEmail, GuestPhone)
        self.guests[GuestID] = guest_instance
        self.clearBoxes()
        print("Guest added successfully. Name: " + GuestName)


class SupplierGUI:
    def __init__(self, suppliers):
        self.suppliers = suppliers
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Supplier Form")

        self.SupplierName_label = tk.Label(self.root, text="Supplier Name:")
        self.SupplierName_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.SupplierName_entry = tk.Entry(self.root)
        self.SupplierName_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        self.SupplierID_label = tk.Label(self.root, text="Supplier ID:")
        self.SupplierID_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.SupplierID_entry = tk.Entry(self.root)
        self.SupplierID_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.SupplierEmail_label = tk.Label(self.root, text="Supplier Email:")
        self.SupplierEmail_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.SupplierEmail_entry = tk.Entry(self.root)
        self.SupplierEmail_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        self.SupplierPhone_label = tk.Label(self.root, text="Supplier Phone:")
        self.SupplierPhone_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.SupplierPhone_entry = tk.Entry(self.root)
        self.SupplierPhone_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        self.root.mainloop()

    def clearBoxes(self):
        self.SupplierName_entry.delete(0, tk.END)
        self.SupplierID_entry.delete(0, tk.END)
        self.SupplierEmail_entry.delete(0, tk.END)
        self.SupplierPhone_entry.delete(0, tk.END)

    def submit(self):
        SupplierName = self.SupplierName_entry.get()
        SupplierID = self.SupplierID_entry.get()
        SupplierEmail = self.SupplierEmail_entry.get()
        SupplierPhone = self.SupplierPhone_entry.get()

        supplier_instance = Supplier(SupplierName, SupplierID, SupplierEmail, SupplierPhone)
        self.suppliers[SupplierID] = supplier_instance
        self.clearBoxes()
        print("Supplier added successfully. Name: " + SupplierName)



class ListEmployeesGUI:
    def __init__(self, employees):
        self.employees = employees
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title("Employee Details")

        self.table = ttk.Treeview(self.root, columns=('Name', 'ID', 'Department', 'Age'), show='headings')
        self.table.heading('Name', text='Name')
        self.table.heading('ID', text='ID')
        self.table.heading('Department', text='Department')
        self.table.heading('Age', text='Age')
        self.table.pack(pady=20)

        for employee_id, employee in self.employees.items():
            self.table.insert('', 'end', values=(employee.getEmployeeName(), employee.getEmployeeID(), employee.getEmployeeDepartment(), employee.getEmployeeAge()))

        self.root.mainloop()


class ListEventsGUI:
    def __init__(self, events):
        self.events = events
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title("Event Details")

        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Date', 'Location'), show='headings')
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Date', text='Date')
        self.table.heading('Location', text='Location')
        self.table.pack(pady=20)

        for event_id, event in self.events.items():
            self.table.insert('', 'end', values=(event.getEventName(), event.getEventDate(), event.getEventLocation()))
        self.root.mainloop()


class ListClientsGUI:
    def __init__(self, clients):
        self.clients = clients
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title("Client Details")

        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Email', 'Phone'), show='headings')
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Email', text='Email')
        self.table.heading('Phone', text='Phone')
        self.table.pack(pady=20)

        for client_id, client in self.clients.items():
            self.table.insert('', 'end', values=(client.ClientID, client.ClientName, client.ClientEmail, client.ClientPhone))

        self.root.mainloop()


class ListGuestsGUI:
    def __init__(self, guests):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title("Guest Details")

        self.guests = guests

        self.table = ttk.Treeview(self.root, columns=('Name', 'ID', 'Email', 'Phone'), show='headings')
        self.table.heading('Name', text='Name')
        self.table.heading('ID', text='ID')
        self.table.heading('Email', text='Email')
        self.table.heading('Phone', text='Phone')
        self.table.pack(pady=20)

        for guest_id, guest in self.guests.items():
            self.table.insert('', 'end', values=(guest.GuestName, guest.GuestID, guest.GuestEmail, guest.GuestPhone))

        self.root.mainloop()


# Update the ListSuppliersGUI class
class ListSuppliersGUI:
    def __init__(self, suppliers):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title("Supplier Details")

        self.suppliers = suppliers

        self.table = ttk.Treeview(self.root, columns=('ID', 'Name', 'Email', 'Phone'), show='headings')
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Email', text='Email')
        self.table.heading('Phone', text='Phone')
        self.table.pack(pady=20)

        for supplier_id, supplier in self.suppliers.items():
            self.table.insert('', 'end', values=(supplier.id, supplier.name, supplier.email, supplier.phone))

        self.root.mainloop()

def write_employees_to_file(employees, filename):
    with open(filename, 'wb') as f:
        pickle.dump(employees, f)

def write_events_to_file(events, filename):
    with open(filename, 'wb') as f:
        pickle.dump(events, f)

def write_clients_to_file(clients, filename):
    with open(filename, 'wb') as f:
        pickle.dump(clients, f)

def write_guests_to_file(guests, filename):
    with open(filename, 'wb') as f:
        pickle.dump(guests, f)

def write_suppliers_to_file(suppliers, filename):
    with open(filename, 'wb') as f:
        pickle.dump(suppliers, f)

allemployees = {}
events = {}
clients = {}
guests = {}
suppliers = {}

form = EmployeeGUI(allemployees)
write_employees_to_file(allemployees, "employees_details.pickle")
showemployees = ListEmployeesGUI(allemployees)

event_form = EventGUI(events)
write_events_to_file(events, "events_details.pickle")
showevents = ListEventsGUI(events)

client_form = ClientGUI(clients)
write_clients_to_file(clients, "clients_details.pickle")
showclients = ListClientsGUI(clients)  # Pass clients dictionary itself

guest_form = GuestGUI(guests)
write_guests_to_file(guests, "guests_details.pickle")
showguests = ListGuestsGUI(guests)

supplier_form = SupplierGUI(suppliers)
write_suppliers_to_file(suppliers, "suppliers_details.pickle")
showsuppliers = ListSuppliersGUI(suppliers)