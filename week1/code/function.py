#!/usr/bin/env python3
"""Week 1 - 函数练习"""

def greet(name="朋友"):
    """问候函数"""
    return f"你好，{name}！"

def calculate_area(radius):
    """计算圆面积"""
    import math
    return math.pi * radius ** 2

def main():
    print(greet())
    print(greet("小明"))
    print(f"半径5的圆面积: {calculate_area(5):.2f}")

if __name__ == "__main__":
    main()