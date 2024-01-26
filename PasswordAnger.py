# Passed! 

N = int(input())
M = int(input())

def get_hash(s):
    hash = 0
    for i in range(len(s)):
        hash = hash * 13 + ord(s[i]) - ord('a') + 1
    return hash

count = 0

p = ["a"] * N
for i in range(26):
    p[0] = chr(ord("a") + i)
    if N == 1:
        if (get_hash("".join(p)) == M):
            count += 1
    for j in range(26):
        if (N < 2):
            break
        p[1] = chr(ord("a") + j)
        if N == 2:
            if (get_hash("".join(p)) == M):
                count += 1
        for k in range(26):
            if (N < 3):
                break
            p[2] = chr(ord("a") + k)
            if N == 3:
                if (get_hash("".join(p)) == M):
                    count += 1
            for l in range(26):
                if N != 4:
                    break
                p[3] = chr(ord("a") + l)
                if N == 4:
                    if (get_hash("".join(p)) == M):
                        count += 1
       
print(count)
    

