from itertools import permutations
import random
import math
#task1
#A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def to_ounces():
    return 28.3495231 * gramss
gramss=int(input())
print(to_ounces())

#task2
#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def to_centigrade():
    r_fahrenheit=int(input())
    c = (5 / 9) * (r_fahrenheit - 32)
    return c
print(to_centigrade())

#task3
#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(heads, legs):
    num_rabbits = (legs - 2*heads) / 2
    num_chickens = heads - num_rabbits
    return int(num_chickens), int(num_rabbits)
heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print("chickens:", chickens)
print("rabbits:", rabbits)


#task4
#You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def is_prime(n):
    if n<=2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]
numbers=list(map(int,input().split()))
prime_nums=filter_prime(numbers)
print(prime_nums)

#task5
#Write a function that accepts string from user and print all permutations of that string.
def permutationss():
    for permutation in permutations(string):
        print(''.join(permutation))
string = str(input())
permutationss()

#task6
#Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
def reverss():
    return ' '.join(reversed(s.split()))
s=str(input())
print(reverss())

#task7
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
nums=list(map(int,input().split()))
print(has33(nums))

#task8
#Write a function that takes in a list of integers and returns True if it contains 007 in order
#def spy_game(nums):     pass spy_game([1,2,4,0,0,7,5]) --> True spy_game([1,0,2,4,0,5,7]) --> True spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums):
    nums2=[]
    nums3=[0,0,7]
    for i in nums:
        if i==0 or i==7:
            nums2.append(i)
    return nums2==nums3
print(spy_game(list(map(int,input().split()))))

#task9
#Write a function that computes the volume of a sphere given its radius.
def volume():
    v=4/3*math.pi*(r**3)
    return v
r=int(input())
print(volume())

#task10
#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def unique_elements():
    unique_list=[]
    for i in just_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
just_list=list(map(int,input().split()))
print(unique_elements())  

#task11
#Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def ispalindrom():
    s=input()
    return s==s[::-1]
print(ispalindrom())

#task12
#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
def histogram():
    nums=list(map(int,input().split()))
    for i in nums:
        print('*'*i, end=" ")
histogram()
print("\n")

#task13
"""Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal
Hello! What is your name? KBTU Well, KBTU, I am thinking of a number between 1 and 20. Take a guess. 12 Your guess is too low. Take a guess. 16 Your guess is too low. Take a guess. 19 Good job, KBTU! You guessed my number in 3 guesses!"""
def whats_the_number():
    name=input()
    print("Hello! What is your name?")
    print(f"{name} Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number=random.randint(1,20)
    number=0
    while True:
        print("Take a guess")
        number+=1
        guess=int(input())
        if guess<secret_number:
            print("Your guess is too low.")
        elif guess>secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, KBTU!, You guessed my number in {number} guesses!")
            break
whats_the_number()