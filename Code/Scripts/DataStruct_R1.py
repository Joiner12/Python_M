# -*- coding:utf-8 -*-
'''
    data struct & algorithm
    https://www.ranxiaolang.com/static/python_algorithm/chapter1/section5.html
'''
import time
start_s = time.time()
for i in range(1000):
    for j in range(100):
        for k in range(1000):
            if i**2 + j**2 == k**2 and i + j + k == 1000:
                print("equal")

end_s = time.time()
print("%.2f\n", end_s-start_s)
