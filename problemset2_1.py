balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
mi = 0       
for i in range(1,13):
    mini = balance * monthlyPaymentRate 
    mini = round(mini,2)
    balance = round(balance,2)
    balance = balance - mini + (annualInterestRate/12)*(balance - mini)
    balance = round(balance, 2)
    print "Month: "+ str(i)
    print "Minimum monthly payment: " + str(mini)
    print "Remaining balance: " + str(balance)  
    mi +=mini 
print "Total paid: " + str(mi)
print "Remaining balance: " + str(balance)             
          