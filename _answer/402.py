print("Enter numbers (end with 9999):")
num = eval(input())
min_num = num

while num != 9999:
    num = eval(input())
    if num < min_num:
        min_num = num
		
print("Minimum =", min_num)