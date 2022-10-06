num = []

for x in range(1,101): # 1-100
    num.append(x)

print(num)


newlist = [x for x in num if x%2>=50]
print(newlist)