"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
เขียนโปรแกรมเพื่อรับค่าอินพุตจากผู้ใช้ เป็นเลขจำนวนเต็ม
จำนวน 2 ชุดข้อมูล โดยมีข้อมูลชุดละ 10 ตัวเลข
จากนั้นให้แสดงข้อมูลที่ซ้ำกัน และ ไม่ซ้ำกันจากข้อมูล 2 ชุดนี้
"""
s1 = set()
for i in range(5): #0-9
    x = int(input(f"enter an integer {i+1}: "))
    s1.add(x)
print(s1)
s2 = set()
for i in range(5): #0-9
    x = int(input(f"enter an integer {i+1}: "))
    s2.add(x)
print(s2)

print("sam integer betweem s1 and s2:",s1.intersection(s2))
print("difference integer betweem s1 and s2:",s1.symmetric_difference(s2))






