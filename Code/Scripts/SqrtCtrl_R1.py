# -*- coding:utf-8 -*-
'''
    开方控制

    Reference:
    [1] 开方控制 https://zinghd.gitee.io/sqrt_controller-lean_angles_to_accel/
    [2] 多元运算符号 https://blog.csdn.net/lanchunhui/article/details/50248327
    [3] math库 https://blog.csdn.net/IamaIearner/article/details/9381347
    [4] numpy库 https://www.runoob.com/numpy/numpy-tutorial.html
    [5] numpy-linspace函数 https://blog.csdn.net/grey_csdn/article/details/54561796
'''
from math import sqrt
# import numpy as np
from numpy import linspace, sin, pi
import matplotlib.pyplot as plt


def sqrt_controller(error, p, second_ord_lim, dt):
    correction_rate = 0
    if second_ord_lim <= 0:
        correction_rate = error*p
    elif p == 0:
        if error < 0:
            correction_rate = -sqrt(2*second_ord_lim*error)
        elif error > 0:
            correction_rate = sqrt(2*second_ord_lim*error)
        else:
            correction_rate = 0
    else:
        linear_dist = second_ord_lim/sqrt(p)
        if abs(error) > linear_dist:
            dir = 1 if error > 0 else -1
            corection_ratetemp = sqrt(
                abs(2.0*second_ord_lim*(error-(linear_dist/2.0))))
            correction_rate = corection_ratetemp*dir
        else:
            correction_rate = error*p
    if (dt == 0):
        return correction_rate
    else:
        sec_temp = abs(error)/dt
        dir = 1 if correction_rate > 0 else -1
        if abs(correction_rate) > sec_temp:
            return dir*sec_temp
        else:
            return correction_rate

    print('error:', error, 'p:', p, 'second_ord_lim:', second_ord_lim, 'dt:', dt)


if __name__ == "__main__":
    print('sqrt controller')
    t = linspace(0, 5, 100)
    dt_a = 5/len(t)
    error_a = sin(t*pi)
    p_a = 1
    seclim_a = 0.5
    out_a = []
    for i in range(0, 100):
        temp_out = sqrt_controller(error_a[i], p_a, seclim_a, dt_a)
        out_a.append(temp_out)
    # plt.plot(t, error_a)
    plt.plot(t, out_a)
    plt.show()
