#week 1 : basic 
if type(varA) == str or type (varB) == str:
    print "string involved"
elif varA > varB:
    print "bigger"
elif varA == varB:
    print "equal"
elif varA < varB:
    print "smaller"
    
#week 2: 
x = 0
while x >=0 and x <= 8:
    x += 2
    print x
print "Goodbye!"

print "Hello!"
x = 12
while x <= 12 and x >= 4:
    x -= 2
    print x


total = 0
current = 1
while current <= end:
    total += current
    current += 1

print total


for i in range(2,12,2):
    print i
print "Goodbye!" 

print "Hello!"
for i in range(10,0,-2):
    print i
    
    
total = end
for next in range(end):
    total += next
print total


print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)/2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))



def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    result = x **2
    return result



def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    result = a * (x **2) + b * x + c
    return result 



def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    return min(max(x, lo), hi)



def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    result = square(square(x))
    return result 



def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return (x % 2 == 1)



def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False
    
    
    
def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if char in  ('a', 'e', 'i', 'o', 'u'):
        return True
    elif char in  ('A', 'E', 'I', 'O', 'U'):
        return True
    else: 
        return False
    
    
    
#week 3: iteration / function 
#write a function return exponential 
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1.0000
    exp = abs(int(exp))
    result = base
    for i in range(exp-1):
        result *= base
    return result


#print iterPower(-4.12,0)


