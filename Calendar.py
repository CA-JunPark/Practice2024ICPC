# https://dmoj.ca/problem/ccc00j1 /skip

week, days = map(int, input().split())
week -= 1

index = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
calendar = [["   "]*7 for i in range(5)]

calendar[0][week+1] = 1


line = 0
for i in range(1,days+1):
    s = ""
    if i > 9:
        s = " " + str(i)
    else:
        s = "  " + str(i)
    calendar[line][week] = s
    week = (week + 1) % 7
    if week == 0:
        line += 1

for i in range(7):
    if i != 6:
        print(index[i], end=" ")
    else:
        print(index[i])

for l in range(5):
    line = ""
    for n in range(7):
        num = calendar[l][n]
        line += num + " "
    line = line.rstrip()                
    print(line)