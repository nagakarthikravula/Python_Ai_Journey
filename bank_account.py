
class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.transactions = []
    
    def check_balance(self):
        print(f"Account Holder : {self.name}")
        print(f"Balance: ₹{self.balance}")

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be positive.")
            return
        else:  
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully")
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance. Withdrawal denied.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew ₹{amount}")
        print(f"₹{amount} withdrawn successfully.")

    def show_history(self):
        if self.transactions:
            print("Transaction History: ")
            for index,transaction in enumerate(self.transactions):
                print(f"{index+1}. {transaction} ")
        else:
            print("No transactions yet.")


def main():
    uname = input("Enter Your UserName: ")
    bacnt = BankAccount(uname)

    while True:
        ip = input('''========================================
         Bank Account Manager
        ========================================
        1. Check Balance
        2. Deposit
        3. Withdraw
        4. Transaction History
        5. Exit
        Enter your choice: ''')

        if ip == "1":
            bacnt.check_balance()
        elif ip == "2":
            amnt = float(input("Enter amount to Deposit: "))
            bacnt.deposit(amnt)
        elif ip == "3":
            amntw = float(input("Enter amount to Withdraw: "))
            bacnt.withdraw(amntw)
        elif ip == "4":
            bacnt.show_history()
        elif ip == "5":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
