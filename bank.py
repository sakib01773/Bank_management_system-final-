from abc import ABC
import random


class Bank:
    def __init__(self):
        self.accounts = []  
        self.total_loan_amount = 0  
        self.balance = 0 
        self.loan_feature_enabled = True 
        



class User(ABC):
    def __init__(self,name,email,addres):
        self.name=name
        self.email=email
        self.addres=addres



class Acount_Holder(User):
    def __init__(self, name, email, addres,account_type):
        super().__init__(name, email, addres)
        self.balance = 0
        self.transaction_history = [] 
        self.loan_count = 0
        self.account_type=account_type
        self.account_number = str(random.randint(1000000000, 9999999999))


    def create_account(self,bank):
        bank.accounts.append(self)
        print(f"Account created for {self.name} with account number {self.account_number}")



    def deposite(self,bank,amount):
        if amount>0:
            self.balance +=amount
            bank.balance += amount
            self.transaction_history.append({
                'type': 'deposite',
                'amount': amount,
                'Current_blance': self.balance
            })
            print(f"Amount Deposite: {amount}\tCurrent balance: {self.balance}")
        else:
            print("invalid Deposite")



    def withdraw(self,bank,amount):
        if amount<self.balance:
            if bank.balance<amount:
                print("Bank is bankcrupt")
                return
            else:
                bank.balance -= amount
            self.balance -=amount
            self.transaction_history.append({
                'type': 'withdraw',
                'amount': amount,
                'Current_blance': self.balance
            })
            print(f"Amount withdraw: {amount}\tCurrent balance: {self.balance}")
        else:
            print("Withdrawal amount exceeded")



    def check_balance(self):
        print(f"Current balance: {self.balance}")




    def check_transaction_history(self):
        for i in self.transaction_history:
            print(f"{i['type']}\t{i['amount']}\t{i['Current_blance']}")



    def request_loan(self, bank, amount):
        if self.loan_count >= 2:
            print("Maximum loan limit reached.")
        elif bank.loan_feature_enabled == False:
            print("TakeLoan Not Possible  at this time") 
        else:
            self.balance += amount
            bank.balance -= amount 
            self.loan_count += 1
            self.transaction_history.append({
                'type': 'loan',
                'amount': amount,
                'Current_blance': self.balance
            })
            bank.total_loan_amount += amount  
            print(f"Loan of {amount} granted. Current balance: {self.balance}")


    def transfer(self, bank, account_number, amount):
        flag = 0
        for i in bank.accounts:
            if account_number == i.account_number:
               flag =1
        if flag==0:
            print("account not Exist")
        else:
            if amount > self.balance:
                print("Insufficient funds to transfer.")

            else:
                self.balance -= amount
                bank.balance -= amount # transfer tai minus korte hobe
                for i in bank.accounts:
                    if i.account_number==account_number:
                        i.balance += amount
                bank.balance += amount # alada bank hole o kaj korbe balance thik thakbe
                self.transaction_history.append({
                    'type': 'transfer',
                    'amount': amount,
                    'Current_blance': self.balance,
                    'account': account_number
                })
                print(f"Transferred Amount: {amount} To Acount {account_number}. Current balance is: {self.balance}")






class Admin(User):
    def __init__(self, name, email, addres):
        super().__init__(name, email, addres)
    
    def create_account(self, bank, name, email, address, account_type):
        new_account = Acount_Holder(name, email, address, account_type)
        bank.accounts.append(new_account)
        print(f"Account created for {name} with account number {new_account.account_number}")

    def delete_account(self, bank, account_number):
        flag = 0
        for i in bank.accounts:
            if account_number == i.account_number:
                print(f"Deleted account{i.account_number}\t{i.name}")
                flag=1
                bank.accounts.remove(i)
                break
        if flag ==0:
            print("Account Number does not Exist")     


    def view_all_accounts(self, bank):
        for i in bank.accounts:
            print("name: \t Email: \t Addres: \t Account_type: ")
            print(f"{i.name}\t{i.email}\t{i.addres}\t{i.account_type}")
        


    def check_total_bank__balance(self, bank):
        print(f"Total available balance in the bank: {bank.balance}") 
    

    def check_total_loan_amount(self, bank):
        print(f"Total loan amount issued by bank: {bank.total_loan_amount}")


    def loan_feature_ON_OFF(self, bank, flag):
        if flag == 1:
            bank.loan_feature_enabled = True
            print('loan enabled')
        elif flag == 0:
            bank.loan_feature_enabled = False
            print('loan disabled')

        
bank=Bank()

admin = Admin('sakib',"sakib@gmail.com","dhaka",)
user= Acount_Holder('Rakib',"Rakib@gmail.com","dhaka","current")



# def signup_user():
#     name = input("Enter Your name: ")
#     email = input("Enter Your email: ")
#     addres = input("Enter Your addres: ")
#     account_type = input("Enter Your accunt_type(savings/current): ")
#     user= Acount_Holder(name,email,addres,account_type)
#     print("succesfully Signup")
#     return user


# def signup_admin():
#     name = input("Enter Your name: ")
#     email = input("Enter Your email: ")
#     addres = input("Enter Your addres: ")
#     admin= Acount_Holder(name,email,addres)
#     print("succesfully Signup")
#     return admin



        








while True:

    print("\n**********************************************")
    print("*********WelCome To Banking System************")
    print("**********************************************\n")

    print("1. View As A USER")
    print("2. View As A ADMIN")
    print("3. Exit")

    ch=int(input())
    if ch == 1:
        print("\n***********************************************************")
        print(f"*********WelCome To Banking System {user.name}************")
        print("***********************************************************\n")
        while True:
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Widthdraw Money")
            print("4. Check Avilable Balance")
            print("5. Check transaction history")
            print("6. Take a loan")
            print("7. Transfer Money")
            print("8. Exit As User")
            ch=int(input())
            if ch == 1:
                user.create_account(bank)
            elif ch == 2:
                amount =int(input("Enter Amount: "))
                user.deposite(bank,amount)
            elif ch == 3:
                amount =int(input("Enter Amount: "))
                user.withdraw(bank,amount)
            elif ch == 4:
                user.check_balance()
            elif ch == 5:
                user.check_transaction_history()
            elif ch == 6:
                amount =int(input("Enter Amount: "))
                user.request_loan(bank,amount)
            elif ch == 7:
                account_number =input("Enter Account Number: ")
                amount =int(input("Enter Amount: "))
                user.transfer(bank,account_number,amount)
            elif ch == 8:
                break
            else:
                print("Invalid Choice")
    elif ch == 2:
        print("\n***********************************************************")
        print(f"*********WelCome To Banking System {admin.name}************")
        print("***********************************************************\n")
        while True:
            print("1. Create Account")
            print("2. Delete Account")
            print("3. View All User Account")
            print("4. Check the total available balance of the bank")
            print("5. Check the total loan Issued Amount")
            print("6. Loan feature(on/of)")
            print("7. Exit As Admin")
            cho=int(input())
            if cho == 1:
                name = input("please Enter name: ")
                email = input("please Enter email: ")
                addres = input("please Enter addres: ")
                account_type = input("please Enter account_type: ")
                admin.create_account(bank,name,email,addres,account_type)
            elif cho == 2:
                account_number=input("Enter account number: ")
                admin.delete_account(bank,account_number)
            elif cho == 3:
                admin.view_all_accounts(bank)
            elif cho == 4:
                admin.check_total_bank__balance(bank)
            elif cho == 5:
                admin.check_total_loan_amount(bank)
            elif cho == 6:
                flag=int(input("Type 0  for (disable)/ 1 for enable: "))
                admin.loan_feature_ON_OFF(bank,flag)
            elif cho == 7:
                break
            else:
                print("Invalid Choice")
    elif ch == 3:
        break
    else:
        print("invalid number")