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

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    exp = abs(int(exp))
    if exp == 0:
        return 1.0000
    return base * recurPower(base,exp-1)



# use recursive call and another way to compute expo:

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    exp = abs(int(exp))
    if exp == 0:
        return 1.0000
    elif exp > 0 and exp % 2 == 0: # even number
        return recurPowerNew(base*base, exp/2)
    else:
        return base * recurPowerNew(base, exp - 1)
    
    
#Write an iterative function, gcdIter(a, b), that implements this idea. One easy way 
#to do this is to begin with a test value equal to the smaller of the two input arguments,
# and iteratively reduce this test value by 1 until you either reach a case where the test divides
# both a and b without remainder, or you reach 1. 

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    a = abs(a)
    b = abs(b)
    start = min(a,b)
    for i in range(1,start + 1):
        if a % start == 0 and b % start == 0:
            return start
        else:
            start -= 1
    return start
            
# use Euclidean algorithm :
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    a = abs(a)
    b = abs(b)
    if b == 0 :
        return a 
    else:
        return gcdRecur(b, a % b)
    

#Write an iterative function, lenIter, which computes the length of an input argument (a string), by counting up the
# number of characters in the string. 
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    char = []
    count = 0
    for i in aStr:
        char.append(i)
        count += 1
    return count


#use recursive method :
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == " ":
        return 0
    return lenRecur(aStr[1:])


#print lenRecur('')
#print lenRecur('mlosxeqmtbuujsmy')




#below is to find whether char is in a string, and if string is smaller than char or char is smaller than
#string , what happened.

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)/2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])
  
  
  
  #tuple exercise:(lecture 6)
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    if aTup == ():
        return ()
    l = []
    keep = [i for i in range(len(aTup)) if i % 2 == 0]
    for x in keep:
        l.append(aTup[x])
        mytuple = tuple(l)
    return mytuple
    

# assume testList = [1, -4, 8, -9]
#use applytoeach function to apply each element in the list.  
 # Your Code Here
def absolute(a):
    return abs(a)
    
applyToEach(testList, absolute) 
  
  
  
  
  
  




















