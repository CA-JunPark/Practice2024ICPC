n, k, c = map(int, input().split()) # total, advance, limit

advance = {i: [] for i in range(1, n + 1)} #key = school, value = id(s)
remaining = []
result = []
counter = 0
for i in range(n):
    id, school = map(int, input().split())
    if counter < k:
        if len(advance[school]) < c:
            advance[school].append(id)
            result.append((id, school))
            counter += 1
        else:
            remaining.append((id, school))

need = k - len(result) 
current = result[0][1]
for j in range(len(result)):
    print(result[j][0])
    if j < len(result)-1:
        if result[j][1] != result[j+1][1]:
            current = result[j+1][1]
            if need > 0:
                print(remaining[0][0])
                remaining.pop(0)
                need -=1


# 10 7 2
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