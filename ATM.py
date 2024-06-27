from abc import ABC, abstractmethod
import random 

class ATM(ABC):

    @abstractmethod
    def Withdrawal(self):
        pass

    @abstractmethod
    def Deposit(self):
        pass
    
    @abstractmethod
    def Balance(self):
        pass

    @abstractmethod
    def Validation(self):
        pass

    @abstractmethod
    def AccountCreation(self):
        pass

class SBI_ATM(ATM):

    def __init__(self):

        print("Welcome to SBI ATM!..")
        self.account_details = {}
        self.isvalidated = False
        self.amount_balance = 0
    
    def AccountCreation(self):
    
        print("Create an account to continue your operation")
        self.username = input("Enter your name: ")
        self.userphonenumber = input("Enter your phonenumber: ")   
        self.account_details[self.username] = [self.userphonenumber]
        print("Account Created Successfully!!.. ")

    def Validation(self):
        
        self.val_name = input("Enter your name: ")
        if self.val_name == self.username:
            print("Username Fetched!..")
            print("OTP Verification Required!!")
            self.display_otp = random.randint(1000,9999)
            print(f"Your 4 Digit OTP here! : {self.display_otp}")
            self.user_otp = int(input("OTP:  "))

            if self.user_otp == self.display_otp:
                print("Success!..")
                self.isvalidated = True
        else:
            print("Enter your Name Correctly!..")

    def Deposit(self):

        self.amount = int(input("Enter an amount to deposit!.."))
        self.amount_balance+=self.amount


    def Withdrawal(self):

        self.amount = int(input("Enter an amount to withdrawal!.."))
        print(f"{self.amount} is withrawed from the {self.amount_balance}")
        self.amount_balance-=self.amount
        print(f"Your New Account Balance: {self.amount_balance}")


    def Balance(self):
        print(f"Your Account Balance: {self.amount_balance}")


user1 = SBI_ATM()
user1.AccountCreation()
user1.Validation()

while True:
    event = input("Please select the Operations below!. \n1.Deposit\n2.Withdrawal\n3.Balance\n4.Quit").strip()

    if event == '1':
        user1.Deposit()
    elif event == '2':
        user1.Withdrawal()
    elif event == '3':
        user1.Balance()
    elif event == '4':
        quit()
    else:
        print("Invalid Input operations..")

