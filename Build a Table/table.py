import math
import pandas as pd
import sys
import numpy as np
from scipy.special import lambertw

sys.set_int_max_str_digits(2000000000)

second = 1
minute = second*60
hour = minute*60
day = hour*24
month = day*30
year = day*365
century = year*100

def calculate_largest_n(f, t_seconds, upper_bound=1e18):
    # Convert time to microseconds
    t_microseconds = t_seconds * 1e6

    try:
        # Calculate n, with an upper bound to avoid too large numbers
        n = f(t_microseconds)
        if n > upper_bound:
            return f"Approximately {n}, exceeds practical computation limits"
        return n
    except OverflowError:
        return "Number too large to compute"

def lg(n):
    """Logarithm base 2 of n."""
    # return math.log2(n)
    return f"2^{n}"

def sqrt(n):
    """Square root of n."""
    return str(n**2)

def linear(n):
    """Linear function, simply returns n."""
    return n

def nlg(n):
    """n times the logarithm base 2 of n."""
    if n == 0:
        return 0
    return str(int(math.e ** lambertw(n * math.log2(math.e)).real)/2)

def squared(n):
    """n squared."""
    return str(int(math.sqrt(n)))

def cubed(n):
    """n cubed."""
    return str(int(np.cbrt(n)))

def two_power_n(n):
    """2 raised to the power of n."""
    return str(int(math.log2(n)))

def factorial(n):
    """Factorial of n."""
    num = 1
    i = 1
    while num < n:
        i += 1   
        num *= i
    return str(i)


# Times in seconds (1 second, 1 minute, 1 hour)
times = [second, minute, hour, day, month, year, century]

# Functions
functions = [lg, sqrt, linear, nlg, squared, cubed, two_power_n, factorial]

def main():
    # Calculating and printing the results
    for func in functions:
        for time in times:
            time =  time * 1e6
            largest_n = func(time)
            print(f"Function {func.__name__}, Time {time} sec: Largest n = {largest_n}")
            
if __name__ == "__main__":
    main()
