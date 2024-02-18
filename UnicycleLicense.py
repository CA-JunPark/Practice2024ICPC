# https://dmoj.ca/problem/sac22cc3p2

M = int(input())

s = lambda t: 12*(t**2) - 5*t + 1 - M

ds = lambda t: 24*t - 5

x = 2


def f(x):
    return x - s(x)/ds(x)

# f = lambda x: x - s(x)/ds(x)

diff = float('inf')

while diff > 10**-6:
    newX = f(x)
    diff = abs(newX - x)
    x = newX
    
print(round(x,6))

