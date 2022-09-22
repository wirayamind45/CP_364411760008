"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
"""

# set --> {...}

s = {10,20,30,40,50}

print(s,type(s))
print(len(s))

# access to item in set
print(s)

for x in s:
    print(x,type(x))

# add item into set เพิ่มข้อมูล
# add 60 to s
s.add(60)
print(s)

s2 = {'a','b','c'}
print(s2)

s.update(s2)
print(s)

# delete item in set
# remove
s.remove(10)
print(s)

if 100 in s:
    s.remove(100)
    print(s)
else:
    print("No item in set.")

# pop()
p = s.pop()
print("delete-->",p)
print(s)

#clear
print(s2)
s2.clear()
print(s2)

# del ลบตัวแปลเซตทิ้ง
del s2
#print(s2)

# join set
s1 = {10,20,30,40,50}
s2 = {10,60,80,90,40,70,100}
# update ()
s1.update(s2)
print(s1)
#union () -- create new set
s3 = s1.union(s2)
print(s3)

# intersection
# intersection_update()
s3.intersection_update(s2)
print(s3)
# intersection--> create new set
s1 = {10,20,30,40,50}
s2 = {10,60,80,90,40,70,100}
s4 = s1.intersection(s3)
print(s4)

#
s5 = s1.symmetric_difference(s2)
print(s5)








