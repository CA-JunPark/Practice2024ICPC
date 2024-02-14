# https://dmoj.ca/problem/banknotes 15/19 scored

n = int(input())
bn = list(map(int, input().split()))
cn = list(map(int, input().split()))
k = int(input())

total = k

bc = [(bn[i],cn[i]) for i in range(n)]
bc = sorted(bc, key=lambda x:x[0], reverse=True)

empty = [0 for i in range(n)]

need = empty.copy()

answer = float('inf')

def calc(current,need, k):
    for i in range(current + 1, n): 
        k += bc[i][0] * need[i] 
        need[i] = min(bc[i][1], k//bc[i][0])
        k -= bc[i][0] * need[i]
    return k, need 

for q in range(n):
    need = empty.copy()
    need[q] = min(bc[q][1], k//bc[q][0])
    
    for w in range(need[q],-1,-1):
        need[q] = w
        k = total - bc[q][0] * need[q]
        sub = q + 1
        k, need = calc(q, need, k)
        if k > 0:
            while sub < n-1:
                k, need = calc(sub, need, k)
                if k == 0:
                    break
                if need[sub] > 0:
                    need[sub] -= 1
                    k += bc[sub][0]
                else:
                    sub += 1
        if k == 0:
            s = sum(need)
            if s < answer:
                answer = s
        need = empty.copy()

print(answer)

# 3
# 2 3 5
# 2 2 1
# 10

# 3 


# 3
# 4 11 1
# 3 1 2
# 13

# 3

# 4
# 21 13 11 18
# 1 2 3 4
# 54

# Sum: 54, [(11, 11, 11, 21), (18, 18, 18)]
# 3

# 6 
# 21 13 11 18 16 19
# 1 2 3 4 3 2
# 58

# Sum: 58, Subsets: [(18, 19, 21), (11, 13, 16, 18), (11, 11, 18, 18), (13, 13, 16, 16), (11, 13, 13, 21)]
# 3