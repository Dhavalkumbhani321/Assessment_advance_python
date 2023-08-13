from database_connection import DatabaseConnection

class PharmacyManager:
    def __init__(self):
        self.db = DatabaseConnection("localhost", "username", "password", "pharmacy_db")

    def Register(self):
       username = input('enter your username')
    password = input('enter your password')
    if username == 'dhavalpatel' and password == '1234':
     print('Welcome !')
    elif username == 'dhavalpatel' and password != '1234':
     print('Incorrect password')
    elif password != '1234':
     print('confirm password')
    pass

    def Login(self):
        email = input('enter your email')
    password = input('enter your password')
    if email == 'dhavalpatel3906@gmail.com' and password == '1234':
     print('Welcome !')
    elif email == 'dhavalpatel3906@gmail.com' and password != '1234':
     print('Incorrect password')
    else:
     print('Not correct')
     
    pass

    def add_medicine(self, name, quantity, price):
        medicine = Medicine(name, quantity, price)
        self.medicines.append(medicine)
        print(f"{name} added to medicines.")
        pass

    def view_medicine(self):
        print("\nCurrent Medicines:")
        for medicine in self.medicines:
            print(f"Name: {medicine.name}, Quantity: {medicine.quantity}, Price: {medicine.price}")
        pass
            

    def delete_medicine(self):
        self.medicines = [medicine for medicine in self.medicines if medicine.name != name]
        print(f"{name} delete from the medicines.")
        pass

class Medicine:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.__qty = qty  # Private field for medicine quantity

    def get_qty(self):
        return self.__qty

    def set_qty(self, qty):
        self.__qty = qty

class PharmacyApp:
    def __init__(self):
        self.manager = PharmacyManager()

    def run(self):
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Add Medicine")
            print("4. View Medicine")
            print("5. Delete Medicine")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.manager.register()
            elif choice == "2":
                self.manager.login()
            elif choice == "3":
                self.manager.add_medicine()
            elif choice == "4":
                self.manager.view_medicine()
            elif choice == "5":
                self.manager.delete_medicine()
            elif choice == "6":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = PharmacyApp()
    app.run()
