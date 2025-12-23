balance = 10000   # starting balance

amount = float(input("enter amount to withdraw:"))
if amount <= balance:
    balance -= amount
    print("withdraw_successful!")
    print("remaning_balance:",balance)
else:
    print("insuffficent_balance!")