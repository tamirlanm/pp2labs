#task1
#Create a generator that generates the squares of numbers up to some number N.
def gen_squares(n):
    for i in range(1,n):
        yield i**2
n=int(input())
squares=gen_squares(n)
for x in squares:
    print(x)

#task2
#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def evennum(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n=int(input())
evenn=evennum(n)
print(*evenn, sep=", ")

#task3
#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def div_by_3_and_4(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
div_by_3_4=div_by_3_and_4(n)
print(*div_by_3_4, sep=", ")

#task4
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def generator(a,b):
    for i in range(a,b+1):
        yield i**2
a,b=map(int,input().split())
squares=generator(a,b)
for x in squares:
    print(x)

#task5
#Implement a generator that returns all numbers from (n) down to 0.
def generator(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
all_numbers=generator(n)
for x in all_numbers:
    print(x)