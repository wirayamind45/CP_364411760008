"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
"""

# tuple
num = (10,20,30,40,50)
print(num,type(num))

# display first item in tuple num
print(num[4],num[-1])
# display last item in tuple num
print(num[0],num[-5])
#rang index (20,30,40)
print(num[1:4])
#rang negative index (20,30,40)
print(num[-4:-1])

# loop
for x in num:
    print(x)

for i in range(len(num)):
    print(num[i])

i = 0
while i < len(num):
    print(num[i])
    i+=1

#edit data in tuple
# 1.change tuple to list#
# num = (10,20,30,40,50)
numlist = list(num)
numlist[0] = 100 # 10-->100
num = tuple(numlist)
print(num)

# add 1000 at index 2 of tuple num #เพิ่มข้อมูลเข้าไป
# num = (100,20,30,40,50)
numlist = list(num)
numlist.insert(2,"1000")
num = tuple(numlist)
print(num)

# delete 30 from tuple num #คำสั่งลบข้อมูล
# num = (20,30,40,50)
numlist = list(num)
numlist.remove(30)
num = tuple(numlist)
print(num)

num2 = ("apple","banana","cherry")

num3 = num + num2
print(num3)

num3 = num3*2
print(num3)

a,b,c = num2
print(a,b,c)

a,*b = num2
print(a,b)




