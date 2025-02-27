#!/usr/bin/env python
def is_prime(n):
    
    is_prime = True
    
    def is_divisible(n,divisor):
        if n<2*divisor: return False
        if n%divisor==0: return True
        else:
            divisor += 1
            return is_divisible(n,divisor)

    if is_divisible(n,divisor=2): is_prime=False
    return is_prime

def get_primes(n):
    if n == 1:
        return
    else:
        if is_prime(n):
            print(n)
        n -= 1
        get_primes(n)

if __name__ == "__main__":
    import sys
    if len( sys.argv ) != 2: # check the number of arguments to be exactly 2.
        print('''
    Error: Exactly two arguments must be given on the command line.
    Usage:''')
        print("     ", sys.argv[0], "<a positive integer number>", '\n')
        sys.exit('     Program stopped.\n')
    else:
        try:
            n = int(sys.argv[1])
            print('Here is a list of all prime numbers smaller than {}:'.format(n))
            get_primes(n)
        except ValueError as err:
            print(err)
            sys.exit(1)