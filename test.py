n = int(input())
bn = list(map(int, input().split()))
cn = list(map(int, input().split()))
k = int(input())

min_notes = float('inf')  # Initialize minimum number of notes to infinity

need = [0 for i in range(n)]

need[0] = min(cn[0], k//bn)

k -= bn[0] * need[0] 

i = 0

