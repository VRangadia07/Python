class BankInfo:
    def __init__(self, fn , ln, gender, address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address
        

class BankAccount(BankInfo):
    def __init__(self, fn, ln, gender, address, ac_no, amount):
        super().__init__(fn, ln, gender, address)
        self.ac_no = ac_no
        self.amount = amount
        
class Saving(BankAccount):
    min_amount = 10000
    rate = 6
    
    def calculate_interest(self, months):
        if self.amount >= Saving.min_amount:
            return(self.amount * Saving.rate * months) / 100
        else:
            return -1
        
class Current(BankAccount):
    min_amount = 5000
    rate = 0
    
    def calculate_interest(self, months):
        if self.amount >= Current.min_amount:
            return 0
        else:
            return -1
        
        
print("Bank Account Setup\n")
fn = input("Enter First Name: ")
ln = input("Enter Last Name: ")
gender = input("Entre Gender: ")
address = input("Enter Address: ")
while True:
    ac_no = input("Enter 12-digit Account Number: ")
    if ac_no.isdigit() and len(ac_no) == 12:
        break
    else:
        print("Invalid account number. Please enter exactly 12 digits.")
        
for attempt in range(3):
    amount = float(input("Enter Opening Amount: "))
    if amount > 0:
        break
    else:
        print("Invalid amount. Try again.")
else:
    print("Too many invalid attempts.")
    exit()


print("\nSelect Account Type: ")
print("1. Saving")
print("2. Current")
choice = input("Enter choice 1 or 2:")

months = int(input("Enter duration in months: "))

    
if choice == "1":
    acc = Saving(fn, ln, gender, address, ac_no, amount)
    interest = acc.calculate_interest(months)
    acc_type = "Saving"
    
elif choice == "2":
    acc = Current(fn, ln, gender, address, ac_no, amount)
    interest = acc.calculate_interest(months)
    acc_type = "Current"
else:
    print("Invalid choice")
    exit()
        
        
print("\n Account Summary:")
print("Name:", acc.fn, acc.ln)
print("Gender:", acc.gender)
print("Address:", acc.address)
print("Account No.:", acc.ac_no)
print("Account Type:", acc_type)
print("Amount:", acc.amount)


if interest == -1:
    print("Minimum Balance not maintained.")
else:
    print("Interest for", months, "months:", interest)
    
    