"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
"""

# function with default parameter ค่าตั้งต้น
def myfunc(msg = "MIT"):
    print("Hello",msg)

# calling function with keyword paraemter
myfunc()
myfunc("Thungsong")

#function with keyword parameter
def myfunc2(num1,num2,num3):
    print(num1,num2,num3)
# calling function with keyword paraemter
myfunc2(num3=30,num1=10,num2=20)

# #function with mlutiples keyword parameter
def myfunc3(**data): # **data --> dictionary
    print(data)
    print(data.keys())
    print(data.values())

# key=value
myfunc3(name="mind",major="MIT")

















