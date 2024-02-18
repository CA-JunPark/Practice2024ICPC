# https://dmoj.ca/problem/pie

N, M = map(int, input().split())

ap = []

for i in range(M):
    a, p = map(int, input().split())
    ap.append((a, p))



total = 1 

obtain = [0 for i in range(N)]

for a,p in ap:
    prop = (total * p/100)
    obtain[a-1] += prop
    total -= prop

for o in obtain:
    print(round(o,6))