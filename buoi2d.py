# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:14:40 2024

@author: nguyenthiphuongvan
"""

print ("giải phương trình bậc 1")
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else: 
        print("Phương trình vô nghiệm.")
else:
        x = -b / a
        print("Nghiệm của phương trình là:", x)


