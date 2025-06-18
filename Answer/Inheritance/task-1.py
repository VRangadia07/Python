class BankInfo:
    def __init__(self, fn, ln, gender, address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address
        
    def display_info(self):
        return f"{self.fn} {self.ln}, {self.gender}, {self.address}"
    
    
class BankAccount:
    def __init__(self, ac_no, amount, customer_info):
        self.ac_no = ac_no
        self.amount = amount
        self.customer_info = customer_info
        
    def display_account(self):
        return f"Account No: {self.ac_no}, Balance: Rs.{self.amount}"
    
    
class Saving(BankAccount):
    min_Amount = 10000
    rate = 0.06
    
    def __init__(self, ac_no, amount, customer_info):
        super().__init__(ac_no, amount, customer_info)
        
    def check_min_balance(self):
        return self.amount >= Saving.min_Amount
    
    def cal_interest(self, months):
        return (self.amount * Saving.rate * months) / 12
    
    
class Current(BankAccount):
    min_Amount = 5000
    rate = 0.00
    
    def __init__(self, ac_no, amount, customer_info):
        super().__init__(ac_no, amount, customer_info)
        
    def check_min_balance(self):
        return self.amount >= Current.min_Amount
    
    def cal_interest(self, months):
        return 0
    

def validate_amount(min_balance):
    chances = 3
    while chances > 0:
        amount = float(input(f"Enter amount Minimum Rs.{min_balance}: "))
        if amount >= min_balance:
            return amount
        else:
            print("Amount is low to minimum balance.")
            chances -= 1
    print("Exceeded maximum attempts.")
    exit()

        
    
    
    
print("Enter Customer Details: ")
fn = input("First Name: ")
ln = input("Last Name: ")
gender = input("Gender: ")
address = input("Address: ")

customer = BankInfo(fn, ln, gender, address)

print("\nAccount Type: ")
print("1. Saving")
print("2. Current")
choice = input("Choose account type (1/2): ")

ac_no = input("Enter Account Number: ")

if choice == "1":
    min_balance = Saving.min_Amount
    amount = validate_amount(min_balance)
    account = Saving(ac_no, amount, customer)
    account_type = "Saving"
elif choice == "2":
    min_balance = Current.min_Amount
    amount = validate_amount(min_balance)
    account = Current(ac_no, amount, customer)
    account_type = "Current"
else:
    print("Invalid choice.")
    exit()
    
months = int(input("Enter number of months for interest calculation: "))
interest = account.cal_interest(months)

print("\nAccount Summary: ")
print(f"Account Type: {account_type}")
print(account.customer_info.display_info())
print(account.display_account())
print("Minimum Balance Maintained:", "Yes" if account.check_min_balance() else "No")
print(f"Interest for {months} months : Rs.{interest:.2f}")
    