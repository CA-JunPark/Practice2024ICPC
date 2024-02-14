# https://dmoj.ca/problem/banknotes 13/19 right only

n = int(input())
bn = list(map(int, input().split()))
cn = list(map(int, input().split()))
k = int(input())

total = k

bc = [(bn[i],cn[i]) for i in range(n)]
bc = sorted(bc, key=lambda x:x[0], reverse=True)

empty = [0 for i in range(n)]

need = empty.copy()

fixed = 0

answer = sum(cn)


def calc(current,need, k, stop=n-1):
    for i in range(current + 1, n): 
        k += bc[i][0] * need[i] 
        need[i] = min(bc[i][1], k//bc[i][0])
        k -= bc[i][0] * need[i]
        if i == stop:
            break

    return k, need 

# while fixed < n:
#     need = [0 for _ in range(n)]
#     need[fixed] = min(bc[fixed][1], k//bc[fixed][0])
    
#     k = total - bc[fixed][0] * need[fixed]
#     k, need = calc(fixed, need, k)
#     sub = fixed + 1
#     while need[fixed] > 0:
#         if k > 0:
#             k, need = calc(fixed, need, k, sub)
#             while sub < n-1:
#                 k, need = calc(sub, need, k)
#                 if k == 0:
#                     break
#                 if need[sub] > 0:
#                     need[sub] -= 1
#                     k += bc[sub][0]
#                 else:
#                     sub += 1
#         if k == 0:
#             if sum(need) < answer:
#                 answer = sum(need)
        
#         need[fixed] -= 1
#         k += bc[fixed][0]
#         sub = fixed + 1
            
#     k = total
#     fixed += 1

for q in range(n):
    need = empty.copy()
    need[q] = min(bc[q][1], k//bc[q][0])
    # k = total - bc[q][0] * need[q]
    # k, need = calc(q, need, k)

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
            if sum(need) < answer:
                answer = sum(need)
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
