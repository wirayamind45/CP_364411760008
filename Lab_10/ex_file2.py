"""
Name: Wiraya homdach
ID: 364411760008
Group: MIT421
"""

# create file
import os

try:
    f = open("test3.txt","x")
    f.close()
except:
    print("File already exits.")

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\test2.txt", "x")
    f.close()
except Exception as e:
    print(e)

# write file
# mode "a"
try:
    f = open("test2.txt","w")
    f.write("Wiraya Hpmdach")
except:
    print("Cloud not found a fine name 'test2.txt")
finally:
    f.close()

if os.path.exists("test3.txt")
    os.remove("test3.txt") #ลบไฟล์
else:
    print("File not found.")