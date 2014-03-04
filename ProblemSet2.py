balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
MonthlyInterestRate = annualInterestRate/12.0
MinMonthPayment = monthlyPaymentRate * balance
totalPaid = 0 

Month = range(0, 12)

#MinMonthPayment = balance * MonthPaymentRate
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

#end
print "Total paid: " + str(round(totalPaid, 2))
print "Remaining balance: " + str(round(balance, 2))
