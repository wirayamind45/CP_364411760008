"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
"""
print("Start")

#divisionทำหน้าที่รับค่าและรีเทินค่าออกไป
def division(a,b):
    try:
        return a/b
    except:
        raise ZeroDivisionError("divide by zero")

try:
    rs = division(10,0)
    print("The result: ",rs)
except Exception as e:
    print("Error log:",e.args)

print("End")