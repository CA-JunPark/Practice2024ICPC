n, k, c = map(int, input().split()) # total, advance, limit

num = {i: [] for i in range(1, n + 1)} #key = school, value = id(s)
result = []
counter = 0
for i in range(n):
    id, school = map(int, input().split())
    if len(num[school]) < c:
        num[school].append(id)
        result.append(id)
        counter += 1
        if counter == k:
            break;

for j in result:
    print(j)