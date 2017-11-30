print("Enter 10 integers:")
tmp = {}
for i in range(10):
    num = input()
    if(num in tmp):
        tmp[num]+=1
    else:
        tmp[num]=1
        
mode = max(tmp, key=tmp.get)
print("Mode of the set: ", mode)
print("Number of occurrence: ", tmp[mode])
