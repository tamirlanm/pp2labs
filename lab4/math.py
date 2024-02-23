import math
#task1
#Write a Python program to convert degree to radian.
a = int(input("Input degree: "))
print("Output radian: ",math.radians(a))

#task2
#Write a Python program to calculate the area of a trapezoid.
h=int(input("Height: "))
a=int(input("Base, first value: "))
b=int(input("Base, second value: "))
print("Expected Output:",((a+b)*h)/2 )

#task3
#Write a Python program to calculate the area of regular polygon.
a=int(input("Input number of sides: "))
b=int(input("Input the length of a side: "))
print("The area of the polygon:", (b**2*a)//(4*math.tan(math.pi/a)))

#task4
#Write a Python program to calculate the area of a parallelogram.
h=int(input("length of base: "))
b=int(input("height of parallelogram: "))
print("expected output:", h*b)