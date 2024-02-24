n = int(input())

correct = 0

for i in range(n):
    ans = ""
    guess = 500
    min = 0
    max = 1000
    while ans != "correct":
        print(guess)
        ans = input()
        if ans == "lower":
            max = guess - 1
        elif ans == "higher":
            min = guess + 1
        guess = (min + max) // 2