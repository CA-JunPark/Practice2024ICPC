# https://dmoj.ca/problem/cpc21c1p4

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
x = N

graph = {i: [] for i in range(1, N + 1)}
for edge in edges:
    u, v = edge
    graph[u].append(v)

def search(x):
    connected = set()
    m = x
    connected.add(x)
    
    for c in graph[x]:
        if c not in connected:
            m = max(m, search(c))
    return m

target = (0, 0)
for x in range(N-1, 0, -1):
    y = search(x)
    if y > x:
        target = (x, y)
        break

if (target == (0, 0)):
    print(-1)
else:
    print(*target)
        
# NOT DONE...
# 5 5
# 1 4
# 2 5
# 3 1
# 2 4
# 1 2