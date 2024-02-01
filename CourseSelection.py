# https://dmoj.ca/problem/waterloo2022fd  # Complete!

c, s = map(int, input().split()) # max#, student#
classes = [int(input()) for i in range(c)]
students = [input().split() for i in range(s)]
students = [[int(wish) for wish in student] for student in students] 


counter = 0
for i in range(len(students)):
    for j in range(len(students[i])):
        if classes[students[i][j]-1] == 0:
            students[i][j] = " "
        else:
            classes[students[i][j]-1] -= 1
            counter += 1

print(counter)
for student in students:
    print(" ".join(map(str,student)).strip())



# 6 3
# 1
# 1
# 1
# 1
# 1
# 1
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 6


# 6
# 1 2 3 4 5

# 6