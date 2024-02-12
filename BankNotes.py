# https://dmoj.ca/problem/banknotes 13/19 right only

n = int(input())
bn = list(map(int, input().split()))
cn = list(map(int, input().split()))
k = int(input())

total = k

bc = [(bn[i],cn[i]) for i in range(n)]
bc = sorted(bc, key=lambda x:x[0], reverse=True)

need = [0 for i in range(n)]

fixed = 0

answer = [sum(cn)]

def calc(current,need, k):
    for i in range(current + 1, n):
        k += bc[i][0] * need[i] 
        need[i] = min(bc[i][1], k//bc[i][0])
        k -= bc[i][0] * need[i] 

    return k, need 

while fixed < n:
    need[fixed] = min(bc[fixed][1], k//bc[fixed][0])
    for t in range(n):
        if t != fixed:
            need[t] = 0
    k -= bc[fixed][0] * need[fixed]
    k, need = calc(fixed, need, k)
    sub = fixed + 1
    while need[fixed] > 0:
        if k >= 0:
            while sub < n:
                k, need = calc(sub, need, k)
                if k == 0:
                    if sum(need) < sum(answer):
                        answer = need.copy()
                    break
                
                if need[sub] > 0:
                    need[sub] -= 1
                    k += bc[sub][0]
                else:
                    sub += 1
        need[fixed] -= 1
        k += bc[fixed][0]
    k = total         
    fixed += 1
    

print(sum(answer))

# 3
# 2 3 5
# 2 2 1
# 10

# 3 


# 3
# 4 11 1
# 3 1 2
# 13

# 2

# 4
# 21 13 11 18
# 1 2 3 4
# 54

# Sum: 54, [(11, 11, 11, 21), (18, 18, 18)]
# 3
