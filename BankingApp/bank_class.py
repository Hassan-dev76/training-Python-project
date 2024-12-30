class Bank:
    def __init__(self, account_title=None, balance: float = 0, password=None):
        self.account_title = account_title
        self.balance = balance
        self.password = password
        self.transaction_history = []

    def check_balance(self):
        print(f"\n\n\t\t\t ---------")
        print(f"\t\t\t Hi, {self.account_title}. Your current balance is Rs. {self.balance}")
        print(f"\t\t\t ---------")

    def withdraw_money(self):
        withdraw_amount = float(input("Enter the amount you want to withdraw: "))
        if withdraw_amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= withdraw_amount  
            self.transaction_history.append(f"Withdrew Rs. {withdraw_amount}")
            return f"Withdrew Rs. {withdraw_amount}. New balance: Rs. {self.balance}"

    def deposit_money(self):
        amount = float(input("Enter the amount you want to deposit: "))
        self.balance += amount  
        self.transaction_history.append(f"Deposited Rs. {amount}")
        return f"Deposited Rs. {amount}. New balance: Rs. {self.balance}"

    def transfer_money(self, target_account, amount: float):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount  
            target_account.balance += amount  
            self.transaction_history.append(f"Transferred Rs. {amount} to {target_account.account_title}")
            target_account.transaction_history.append(f"Received Rs. {amount} from {self.account_title}")
            return f"Transferred Rs. {amount} to {target_account.account_title}. New balance: Rs. {self.balance}"

    def monthly_statement(self):
        if not self.transaction_history:
            return "No transactions yet."
        return "\n".join(self.transaction_history)

    def check_password(self, entered_password):
        if self.password == entered_password:
            return True
        else:
            return False
