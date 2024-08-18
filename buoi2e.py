# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:34:23 2024

@author: nguyenthiphuongvan
"""

import math
print ("giải phương trình bậc 2")
a = float(input("Nhập a ="))
b = float(input("Nhập b ="))
c = float(input("Nhập c ="))
delta = b**2 -(4*a*c)
if delta < 0: 
    print("phương trình vô nghiệm")
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("phương trình có 2 nghiệm phân biệt")
    print("x1=",x1)
    print("x2=",x2)
elif delta == 0:
    print("phương trình có nghiệm kép x1=x2",-b/2*a)
    
    
    
    
    
    

