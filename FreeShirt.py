# https://dmoj.ca/problem/ecoo19r1p1 Completed

result = [0 for _ in range(10)]
for s in range(10):
    N, M, D = map(int, input().split())
    Ms = input().split()
    Ms = [int(m) for m in Ms]
    maxN = N

    for d in range(1, D+1):
        if N == 0: # wash
            N = maxN
            result[s] += 1
        if d in Ms: # event
            while (d in Ms):
                maxN += 1
                N += 1
                Ms.remove(d)

        N -= 1 # end of a day
        
for i in result:
    print(i)


# 1 1 10
# 10

# 9

#-----------

# 1 3 10
# 2 9 5

# 3
