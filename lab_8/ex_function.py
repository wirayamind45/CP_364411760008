"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
"""

# 1.
print("Hello, MIT421")
s = "RUTS"
print(len(s))

#2. create by owner --> using "def" keyword

def myfunction1():
    print("Hello, from fromfunction 1.")

def myfunction2(msg):
    print("Hello, from fromfunction 2.",msg)

def myfunction3(num1,num2):
    print("Hello, from fromfunction 3.")
    #return statement
    return num1+num2

#calling function
myfunction1()

# calling function with parameter
myfunction2("RUTS")

# calling function with parameter and return statement
rs = myfunction3(10,10)
print(rs)

print(myfunction3(20,20))














