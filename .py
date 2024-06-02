class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []
    def check_pin(self, pin):
        return self.pin == pin
    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)
class ATM:
    def __init__(self):
        self.users = {}
        self.current_user = None
    def add_user(self, user):
        self.users[user.user_id] = user
    def login(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.check_pin(pin):
            self.current_user = user
            return True
        return False
    def logout(self):
        self.current_user = None
class ATMOperations:
    @staticmethod
    def show_transaction_history(user):
        if not user.transaction_history:
            print("No transactions found.")
        else:
            for transaction in user.transaction_history:
                print(transaction)
    @staticmethod
    def withdraw(user, amount):
        if amount > user.balance:
            print("Insufficient funds.")
        else:
            user.balance -= amount
            user.add_transaction(f"Withdrew: ${amount}")
            print(f"Withdrew: ${amount}")
    @staticmethod
    def deposit(user, amount):
        user.balance += amount
        user.add_transaction(f"Deposited: ${amount}")
        print(f"Deposited: ${amount}")
    @staticmethod
    def transfer(user, recipient, amount):
        if amount > user.balance:
            print("Insufficient funds.")
        else:
            user.balance -= amount
            recipient.balance += amount
            user.add_transaction(f"Transferred: ${amount} to {recipient.user_id}")
            recipient.add_transaction(f"Received: ${amount} from {user.user_id}")
            print(f"Transferred: ${amount} to {recipient.user_id}")
class ATMInterface:
    def __init__(self):
        self.atm = ATM()
    def start(self):
        print("Welcome to the ATM!")
        while True:
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")
            if self.atm.login(user_id, pin):
                print("Login successful!")
                self.main_menu()
            else:
                print("Invalid user ID or PIN. Please try again.")
    def main_menu(self):
        while self.atm.current_user:
            print("\nMain Menu:")
            print("1. Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")
            choice = input("Choose an option: ")
            if choice == '1':
                ATMOperations.show_transaction_history(self.atm.current_user)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                ATMOperations.withdraw(self.atm.current_user, amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                ATMOperations.deposit(self.atm.current_user, amount)
            elif choice == '4':
                recipient_id = input("Enter recipient user ID: ")
                recipient = self.atm.users.get(recipient_id)
                if recipient:
                    amount = float(input("Enter amount to transfer: "))
                    ATMOperations.transfer(self.atm.current_user, recipient, amount)
                else:
                    print("Recipient not found.")
            elif choice == '5':
                self.atm.logout()
                print("Logged out successfully.")
            else:
                print("Invalid choice. Please try again.")
user1 = User("user1", "1111", 500)
user2 = User("user2", "2222", 1000)
atm_interface = ATMInterface()
atm_interface.atm.add_user(user1)
atm_interface.atm.add_user(user2)
atm_interface.start()
