def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    start = int(start)
    stop = int(stop)
    step = float(step)
    result = 0
    for i in frange(start, stop, step):
          result += f(i) * step
    return round(result, 2)

print radiationExposure(0, 4, 0.25)
    
    
    
    
    