#task1
#Write a Python program with built in function to multiply all the numbers in a list
import math, time
def llist(list1):
    return math.prod(list1)
print(llist([1,2,3,4,5]))
print()

#task2
#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def strins(strs):
    upperc=sum(1 for ch in strs if ch.isupper())
    lowerc=sum(1 for ch in strs if ch.islower())
    return upperc,lowerc
strs="This is NOT AvAible"
upperc,lowerc=strins(strs)
print("This is UPPERCASES:>",upperc)
print("This is lowercases:>",lowerc)
print()

#task3
#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def stringgs(strs):
    return "True" if strs==strs[::-1] else "False"
print(stringgs("abba"))
print(stringgs("abbd"))
print()

#task4
#Write a Python program that invoke square root function after specific milliseconds.
def root_after_ms(num, ms):
    time.sleep(ms / 1000)
    return math.sqrt(num)
num = 25100
ms = 2123
print(f"Square root of {num} after {ms} miliseconds is {root_after_ms(num, ms)}")
print()

#task5
#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def thisistuple(tupl):
    x=all(tupl)
    return x
print(thisistuple((1,2,3,4)))
print(thisistuple((False,True)))
print(thisistuple(("thisisstring",1234)))