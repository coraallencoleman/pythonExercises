MonthlyInterestRate = annualInterestRate/12.0
#want to find MonthPayment
#in increments of 10

guess = balance/12

while balance > 0:
    guess += 10
    for month in range(1,13):
            balance += (balance*MonthlyInterestRate) - guess
            print print "Remaining balance: " + str(balance) 
    
    if balance < 0:
        break
    else:
        x += 10
            
if x < 0:
                    MonthPayment = x
                    print "Lowest Payment: " + str(round(LowestPayment, 2))
                    break



MonthlyUnpaidBalance = balance - MinMonthPayment
BalanceNew = MonthlyUnpaidBalance + MonthlyInterestRate * MonthlyUnpaidBalance


for month in range(1, 13):
    MinMonthPayment = balance * monthlyPaymentRate
    MonthlyUnpaidBalance = balance - MinMonthPayment
    balance = MonthlyUnpaidBalance + MonthlyInterestRate * MonthlyUnpaidBalance
    totalPaid += MinMonthPayment
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(MinMonthPayment, 2))
    print "Remaining balance: " + str(round(balance, 2)) 


