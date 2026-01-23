#!/usr/bin/env python3

if __name__ == "__main__":
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age
    p1 = Plant("Rose:", "25cm,", "30 days old")
    p2 = Plant("Sunflower:", "80cm,", "45 days old")
    p3 = Plant("Cactus:", "15cm,", "120 days old")
    print("=== Day 1 ===")
    print(p1.name, p1.height, p1.age)
    print(p2.name, p2.height, p2.age)
    print(p3.name, p3.height, p3.age)

grow()
age()
get_info() 