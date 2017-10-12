print("Enter two numbers:")
a = int(input("a = "))
b = int(input("b = "))
ans = 0

for i in range(a, b+1):
    if i % 2 == 0:
        ans += i

print("The sum is:",ans)