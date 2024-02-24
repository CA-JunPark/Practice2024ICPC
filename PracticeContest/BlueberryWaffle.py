r, f = map(int, input().split())

b = f // (r/2)

c = b % 4

if c == 0 or c == 3:
    print('up')
else:
    print('down')

