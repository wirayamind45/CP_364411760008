"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
"""

# exception
print("Start")

x = "MIT421"

try:
    print(x)
except NameError:
    print("variable name not define.")
except:
    print("Something went wrong.")
else:
    print("No error.")
finally:
    print("Error has been excepted.")

print("End")