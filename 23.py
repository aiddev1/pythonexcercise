nums = range(1,100)

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

primes = list(filter(is_prime,nums))
print(primes)