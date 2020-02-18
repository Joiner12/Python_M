# -*- codin:utf-8 -*-
'''
    继承object参数：

    Ref:
    [1]Python 为什么要继承 object 类？https://www.zhihu.com/question/19754936
    [2]self参数用法 https://blog.csdn.net/CLHugh/article/details/75000104\
    [3]super函数 https://www.runoob.com/python/python-func-super.html
'''


class A():
    def foo(self):
        print('Class A function called %s\n' % (foo))


class B(A):
    pass


class C(A):
    def foo(self):
        print('Class C function called %s\n' % (foo))


class D(B, C):
    def foo(self):
        print('d')


class Parent:
    def pprt(self):
        print(self)


class Child(Parent):
    def cprt(self):
        print(self)


if __name__ == "__main__":
    a_1 = D()
    a_1.foo()
    debug_a = 1

    c = Child()
    c.cprt()
    c.pprt()
    p = Parent()
    p.pprt()
