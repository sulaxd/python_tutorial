a = eval(input("a = "))
b = eval(input("b = "))
opr = input("operator = ")
ans = 0

if opr == '+':   ans = a + b
elif opr == '-': ans = a - b
elif opr == '*': ans = a * b
elif opr == '/': ans = a / b
elif opr == '//':ans = a // b
elif opr == '%': ans = a % b

print("The result is:", ans)