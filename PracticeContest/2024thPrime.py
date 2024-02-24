from math import isqrt
n = 7920

count = 1000

def isPrime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


while True:
    if isPrime(n):
        count += 1
        if count == 2024:
            break
    n += 1
 
print(n)