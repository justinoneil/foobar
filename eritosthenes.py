# Find all the prime numbers between 2 and another number
from math import sqrt

primes = []
max_number = 1000000

working_number = 2
while working_number <= max_number:
    # Assume the number could be prime until we know it isn't
    maybe_prime = True
    
    # Check to see if the number is divisible by any already known lesser primes
    max_divisor = sqrt(working_number)
    for p in primes:
        if working_number % p == 0:
            maybe_prime = False
            break # stop looking once we know there is a factor
        # stop looking when no greater number is a factor
        elif p > max_divisor:
            break
            
    # At this point, the number is known to be prime or not prime
    if maybe_prime:
        primes.append(working_number)
    working_number += 1

print(primes)
