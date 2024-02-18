# https://dmoj.ca/problem/wc99p4
# https://en.wikipedia.org/wiki/Primality_test
from math import isqrt
n = int(input())

result = []


def isPrime(n: int) -> bool:
    if n == 1:
        return True
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

while n != -1:
    temp = []
    a = n // 2
    b = n // 2
    
    while a > 0:
        if isPrime(a):
            if isPrime(b):
                temp.append((a,b))
        a -= 1
        b += 1

    n = int(input())
    
    
    temp = sorted(temp, key=lambda x: x[0])
    result.append(temp)
    
for i in range(len(result)):
    for a,b in result[i]:
        print(a,b)
    print()