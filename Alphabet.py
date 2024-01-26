# it works but Time Limit exceeded

s = input()
# aiemckgobjfndlhp
# xyzabcdefghijklmnopqrstuvw

mx = 0

def combinations(s, prefix=""):
    global mx
    
    if (len(s) == 0):
        mx = max(len(prefix), mx)
    else:
        for l in range(len(s)):
            if prefix == "" or ((s[l]) > (prefix[-1])):
                combinations(s[l+1:], prefix + s[l])

combinations(s)

print(26 - mx)