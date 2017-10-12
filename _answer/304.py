num = eval(input("Enter a number:"))
ans = 0

for i in range(1, num+1):
    if i % 5 == 0 :
        ans += i
      
print("The sum is: ",ans)