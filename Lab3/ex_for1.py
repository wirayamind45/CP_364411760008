"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
"""

# for loop

# rang()
for x in range(10):
    print(x,end="-")

#1-10
print("")
for x in range(1,11):
    print(x, end="-")

#แสดงตัวเลขตั้งแต่ 1-100 ที่หารด้วย 5 ลงตัว
print("")
for x in range(5,101,5):
    print(x, end="-")

#แสดงตัวเลขตั้งแต่ 1-100 ที่หารด้วย 3 และ 5 ลงตัว
print("")
for x in range(1,101):
    if x%3==0 and x%5==0:
        print(x, end="-")