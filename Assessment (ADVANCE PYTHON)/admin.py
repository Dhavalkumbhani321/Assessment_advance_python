from database_connection import DatabaseConnection

class Admin:
    def __init__(self):
        self.db = DatabaseConnection("localhost", "username", "password", "pharmacy_db")

    def register(self):
        username = input('enter your username')
    password = input('enter your password')
    if username == 'Robert parker' and password == '98765':
     print('Welcome !')
    elif username == 'Robert parker' and password != '98765':
     print('Incorrect password')
    elif  password != '98765':
     print('confirm password')
    pass
      
        

    def login(self):
        email = input('enter your email')
    password = input('enter your password')
    if email == 'robertparker@gmail.com' and password == '12345':
     print('Welcome !')
    elif email == 'robertparker@gmail.com' and password != '12345':
     print('Incorrect password')
    else:
     print('Not correct')
    pass

    def viewall_medicine(self):
        print("\nCurrent Medicines:")
        for medicine in self.medicines:
            print(f"Name: {medicine.name}, Quantity: {medicine.quantity}, Price: {medicine.price}")
        pass
    
    
    def viewall_manager(self):
         print("\nCurrent Medicines:")
         for medicine in self.medicines:
            print(f"Name: {medicine.name}, Quantity: {medicine.quantity}, Price: {medicine.price}")
         pass
   
