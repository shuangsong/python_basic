balance = 4773
annualInterestRate = 0.2
rate = annualInterestRate/12
mini = 0
while balance > 0: 
    balance = 4773
    mini += 10
    for i in range(1,13):
         balance = balance - mini + (balance - mini)*rate
       
print  'Lowest Payment: '  + str(mini)
