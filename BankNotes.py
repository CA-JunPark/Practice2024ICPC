# https://dmoj.ca/problem/banknotes 7/19 right only

n = int(input())
bn = list(map(int, input().split()))
cn = list(map(int, input().split()))
k = int(input())

bc = [(bn[i],cn[i]) for i in range(n)]
bc = sorted(bc, key=lambda x:x[0], reverse=True)

need = [0 for i in range(n)]

need[0] = min(bc[0][1], k//bc[0][0])

k -= bc[0][0] * need[0]

current = 0

def calc(current, need, k):
    for i in range(current + 1, n):
        if k == 0:
            break
        need[i] = min(bc[i][1], k//bc[i][0])
        k -= bc[i][0] * need[i]
    return k, need   

while True:
    s, need = calc(current, need, k)
    if s > 0:
        try:
            k += bc[current][0]
        except:
            print(k)
        need[current] -= 1
        if need[current] < 1:
            current += 1
    else:
        break

print(sum(need))

# 3
# 2 3 5
# 2 2 1
# 10

# 3 


# 3
# 11 4 1
# 1 3 1
# 12

# 2



