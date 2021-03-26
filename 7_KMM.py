import termcolor2

x = int(input("Enter First Number: "))  # 20
y = int(input("Enter second Number: "))  # 40

if x > y:
    print(termcolor2.colored("Error! TryAgain", color="red"))
else:
    for i in range(y, x * y + 1):
        if i % x == 0 and i % y == 0:
            kmm = i
            break
print(f"KMM: {kmm}")