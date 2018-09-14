# importing datetime and defining current date

from datetime import datetime
today = datetime.now().strftime("%Y-%b-%d")

# making definition for new balance

def calculate(totalBalance):
    chop = 600000
    tax = 218543
    newBalance = totalBalance - chop - tax
    newBalance = "{:,}".format(newBalance)
    return (newBalance)

# receiving user input for current balance and giving new balance as output

balance = int(input("Type in your current balance: "))
print("New balance is: ", calculate(balance), "on", today)