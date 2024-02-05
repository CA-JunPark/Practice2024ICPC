# https://dmoj.ca/problem/ccc21s3 ## passed only 4 marks

N = int(input())
PWD = []

for n in range(N): 
    P,W,D = map(int, input().split()) # initial pos (m), speed (m/s), hearing (m) 
    PWD.append((P,W,D))
PWD = sorted(PWD, key=lambda x: x[0])

def half(minP, maxP):
    return (maxP + minP)//2

def needTime(x,P,W,D):
    dist = abs(P-x)
    if (dist > D):
        return (abs(P-x) - D)*W
    else:
        return 0

def totalTime(x):
    s = 0
    for tuple in PWD:
        s += needTime(x,tuple[0],tuple[1],tuple[2])
    return s

minT = totalTime(PWD[0][0])
for i in range(PWD[0][0], PWD[-1][0]+1):
    t = totalTime(i)
    if minT > t:
        minT = t

print(minT)

# 1
# 0 1000 0

# 0
 
#---------

# 2
# 10 4 3
# 20 4 2

# 20

#--------
# 3
# 6 8 3
# 1 4 1
# 14 5 2

# 43