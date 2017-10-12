
print("File content:")

f = open("C:\ANS.csf\PY09\Sum.txt",'r')
data = f.read()
print(data)
f.close()

num = data.split(' ')
total = 0
for i in range(0, len(num)):
    total += eval(num[i])

print('Sum of data =', total)
