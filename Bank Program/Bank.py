import time
print("Please insert your card:")

time.sleep(3)

password = 0000

pin=int(input("-Enter your ATM PIN:"))

balance= 10000

if (pin == password):

    while True:

        print("""
    Enter 1 to check BALANCE
    Enter 2 to WITHDRAW BALANCE
    Enter 3 to DEPOSIT BALANCE
    Enter 4 to EXIT
    """)

        try:
            option = int(input("-Please enter your choice:"))

        except:
            print("-Please enter valid option:")

        if ( option == 1 ):
            print(f"-Your current account balance is {balance}")

        if ( option == 2 ):
            withdraw_amount = int(input("-Enter the amount you want to WITH-DRAW"))

            balance = balance - withdraw_amount

            print(f"-{withdraw_amount}) is debited from your account")

            print(f"-Your current balance is {balance}")

        if (option == 3):
            da = int(input("Please enter DEPOSIT AMOUNT"))

            balance = balance + da

            print(f"-{da} is credited in your account. ")

            print(f"-Your updated balance is {balance}.")

        if (option == 4):
            break

else:
    print("""
    *TRY AGAIN*
    the PIN entered in invalid
    """)