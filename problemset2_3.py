#bisection search:
#try to find exactly what number of minimum of pay each month. 
#increase calculation speed.
balance = 320000
obalance = balance
annualInterestRate = 0.2
rate = annualInterestRate / 12
low = obalance / 12
high = (obalance * (1 + rate)**12) / 12 
payment = (high + low) / 2
epsilon = 0.01
remain = obalance

while abs(remain) >= epsilon: 
    payment = (high + low) / 2
    for month in range(1,13):
        remain = (remain - payment) * (1 + rate)
    if remain < 0:
        high = payment
        remain =  obalance
    elif remain > epsilon:
        low = payment
        remain = obalance 
print "Lowest payment: " + str(round(payment,2)) 

# some thought : 
# first set payment to middle of high and low.
#set while standard epsilon 