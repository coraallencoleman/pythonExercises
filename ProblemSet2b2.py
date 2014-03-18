balance = 3329
annualInterestRate = 0.2
MonthlyInterestRate = annualInterestRate/12.0
#want to find MonthPayment
#in increments of 10

guess = balance/12

while balance > 0:
    guess += 10
    for month in range(1,13):
            balance += (balance*MonthlyInterestRate) - guess
            print "Remaining balance: " + str(balance)
else:
    LowestPayment = guess


print "Lowest Payment: " + str(round(, 2))
             