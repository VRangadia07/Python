class Max_AmountLimit_Exceeded(Exception):
    pass

class Max_TransactionLimit_Exceeded(Exception):
    pass


class Bank:
    def __init__(self, max_amount, max_transaction):
        self.__max_amount = max_amount
        self.__max_transaction = max_transaction
        self.__transaction_count = 0
        
    def withdraw(self, amount):
        if self.__transaction_count >= self.__max_transaction:
            raise Max_TransactionLimit_Exceeded("Transaction limit Exceeded.")
        if amount > self.__max_amount:
            raise Max_AmountLimit_Exceeded(f"Amount Exceed limit of rs.{self.__max_amount}.")
        
        self.__transaction_count += 1
        self.__max_amount -= amount
        
        print(f"\nTransaction Successful")
        print(f" Amount withdraw: Rs.{amount}")
        print(f" Remain Balance limit: Rs.{self.__max_amount}")
        print(f" Remain Transaction: {self.__max_transaction - self.__transaction_count}")
        
        
    def transaction(self):
        return self.__transaction_count < self.__max_transaction and self.__max_amount > 0
    
    
class HDFCBank(Bank):
    def __init__(self):
        super().__init__(20000, 3)
        
        
class AxisBank(Bank):
    def __init__(self):
        super().__init__(30000, 5)
        
        
class ATM:
    def __init__(self):
        self.bank = None
        
        
    def inputAmount(self):
        while True:
            choice = input("Enter Bank Name (HDFC/Axis): ")
            if choice == "HDFC":
                self.bank = HDFCBank()
                break
            elif choice == "Axis":
                self.bank = AxisBank()
                break
            else:
                print("Invalid Bank Name. Choice 'HDFC' or 'Axis'.")
                
        
        while True:
            try:
                amount = float(input("Enter Amount to withdraw: Rs."))
                self.bank.withdraw(amount)
            except Max_TransactionLimit_Exceeded as e:
                print(e)
                break
            except Max_AmountLimit_Exceeded as e:
                print(e)
                break
            
            if not self.bank.transaction():
                print("Limit reached. Can not Continue.")
                break
            
            next_transaction = input("Do you want to next transaction? (yes/no): ")
            if next_transaction != "yes":
                print("Thank you! Come again")
                break
            
            
            
if __name__ == "__main__":
    atm = ATM()
    atm.inputAmount()
        
        
        