target = "3" # complete!
n = int(input())
for i in range(n):
    swap = input()
    index = swap.find(target)
    if index > -1:
        if index == 2:
            target = swap[0]
        else:
            target = swap[2]
print(target)
