n, k, c = map(int, input().split()) # total, advance, limit

num = {i: [] for i in range(1, n + 1)} #key = school, value = id(s)
result = []
counter = 0
for i in range(n):
    id, school = map(int, input().split())
    if counter < k:
        if len(num[school]) < c:
            num[school].append(id)
            result.append(id)
            counter += 1
        
for j in result:
    print(j)
    
    
# 10 7 3
# 3 9
# 1 9
# 4 9
# 5 9
# 9 7
# 2 7
# 6 7
# 7 7
# 8 5
# 10 5