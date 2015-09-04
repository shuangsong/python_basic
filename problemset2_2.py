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

#below is that I wrote to submit :
#balance and annualinterestrate is already defined
# Paste your code into this box
rate = annualInterestRate/12
mini = 0
newbalance = balance
while (newbalance > 0):
    newbalance = balance
    mini += 10
    for i in range(1,13):
         newbalance = newbalance - mini + (newbalance - mini)*rate
print  'Lowest Payment: '  + str(mini)