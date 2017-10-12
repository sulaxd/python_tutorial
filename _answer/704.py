num = set()
print("Enter numbers (end with -9999):")

while True:
    inp = eval(input())
    if inp == -9999: break
    num.add(inp)

print(num)
print("Length: ", len(num))
print("Max: ", max(num))
print("Min: ", min(num))
print("Sum: ", sum(num))
