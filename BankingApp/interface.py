from bank_class import Bank 

class Interface(Bank):
    def __init__(self):
        super().__init__()  

    def display(self):
        while True:
            print("\t\t **Welcome to the Micro Banking APP **")
            print("\n1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Transaction history")
            print("6. Exit")
        
            try:
                choice = int(input("Choose an option: "))
            
                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    self.deposit_money()
                elif choice == 3:
                    self.withdraw_money()
                elif choice == 4:
                    target_account = Bank("Noman", 0, 1234)
                    self.transfer_money(target_account, 2000)
                elif choice == 5:
                    print(f"Monthly statement: {self.monthly_statement()}")  
                elif choice == 6:
                    break  
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")


    def check_password(self, user_pass):
    
        if len(str(user_pass)) != 4 or not str(user_pass).isdigit():
            print("Wrong Password! Password should contain 4 digits.")
            return False  
        return True 

    def input_data(self):
        user_name = input("Enter your name: ")
      
        while True:
            try:
                user_password = int(input("Enter your 4-digit password: "))
                if self.check_password(user_password):
                    break 
            except ValueError:
                print("Invalid input! Please enter a valid 4-digit number.")
        
        super().__init__(user_name, 0, user_password)
        print(f"\t\t\t ** Hello {user_name}, your password is set successfully. **\n\n\n\n")
        self.display()  




obj = Interface()
obj.input_data()