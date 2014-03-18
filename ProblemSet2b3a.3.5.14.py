balance = 4577
annualInterestRate = 0.2
new_balance = balance
MonthlyInterestRate = annualInterestRate/12.0
MonthlyUnpaidBalance = 0
MonthlyPayment = 30

if balance < (MonthlyPayment*12)+1:
    MonthlyPayment = 0
else:
    MonthlyPayment = 30

#print "The MonthlyPayment guess is " + str(MonthlyPayment)

while True:
    if new_balance <= 0:
        break
    else:
        new_balance = balance
        MonthlyPayment +=10
        for month in range(1, 13):
            MonthlyUnpaidBalance = new_balance - MonthlyPayment
            new_balance = MonthlyUnpaidBalance + (MonthlyUnpaidBalance*MonthlyInterestRate) 

print "Lowest Payment: " + str(MonthlyPayment)
    