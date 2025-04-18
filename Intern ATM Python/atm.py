import time

print("======================================================")
print("======================================================")

welcome_logo = """
                ATM MACHINE INTERFACE
                    -Made by Shree  
                         """
print(welcome_logo)

print("======================================================")
print("======================================================")

print("\n====------------------------- Please insert your Card ---------------------------====")
time.sleep(5)


password = 1010
balance = 10000

pin = int(input("\n\tEnter your ATM PIN: "))

if pin == password:
    while True:
        print('''
        1 : Check Balance
        2 : Withdraw
        3 : Deposit   
        4 : Exit
        ''')
        try:
            option = int(input("\tPlease select any one option: "))
            if option == 1:
                print("___________________________________________________________")
                print("***********************************************************")
                print(f"\n\tYour current balance is {balance}")
                print("___________________________________________________________")
                print("***********************************************************")
    
            if option == 2:
                 withdraw_amount = int(input("\n\tPlease enter your Withdraw Amount: "))
            balance = balance - withdraw_amount
            print("___________________________________________________________")
            print("***********************************************************")
            print(f"\t{withdraw_amount} is debited from your account")
            print("___________________________________________________________")
            print("***********************************************************")
            print("===========================================================")
            print("___________________________________________________________")
            print("***********************************************************")
            print(f"\tYour update current balance is {balance}")
            print("___________________________________________________________")
            print("***********************************************************")

            if option == 3:
                deposit_amount = int(input("\n\tPlease enter your Deposit Amount: "))
            balance = balance + deposit_amount
            print("___________________________________________________________")
            print("***********************************************************")
            print(f"\t{deposit_amount} is credited to your account")
            print("___________________________________________________________")
            print("***********************************************************")
            print("======================================================")
            print("___________________________________________________________")
            print("***********************************************************")
            print(f"\tYour updated current balance is {balance}") 
            print("___________________________________________________________")
            print("***********************************************************")

            if option == 4:
                break

        except:     
            print("\tPlease enter a valid option between 1 to 4")
        else:
            print("\n\tPIN inserted by you is not correct")

