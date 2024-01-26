# https://dmoj.ca/problem/cpc21c1p4

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
x = N

graph = {}
for e in edges:
    if e[0] in graph:
        graph[e[0]].append(e[1])
    else:
        graph[e[0]] = [e[1]]

while x > 0:
    y = 0
    if (x in graph):
        candidates = []
        candidates.extend(graph[x])
        
        i = 0
        while i < len(candidates):
            if candidates[i] in graph:
                for yy in graph[candidates[i]]:
                    if yy not in candidates:
                        candidates.append(yy)
            i += 1
        
        y = max(candidates)
        
        if (x < y):
            print(x, y)
            break
        
    x -= 1
        
if (x == 0):
    print(-1)
        
        

    