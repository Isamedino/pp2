import math
import random
import itertools


# 1.A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells
# items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def convert_grams_to_ounces(grams: float) -> float:
    ounces: float = 28.3495231 * grams
    return ounces


# 2.Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following
# formula is used for the conversion: C = (5 / 9) * (F – 32)
def fahrenheit_to_celsius(f: float) -> float:
    c: float = (5 / 9) * (f - 32)
    return c


# 3.Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a
# farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numheads: int, numlegs: int) -> tuple:
    for chickens in range(0, numheads + 1):
        rabbits = numheads - chickens
        if numlegs == (chickens * 2 + rabbits * 4):
            return chickens, rabbits
    return 0, 0


# 4.You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers
# as an agrument and returns only prime numbers from the list.
def filter_prime(numbers: list) -> list:
    if_prime = lambda x: all(x % i != 0 for i in range(2, x))
    result_it = filter(if_prime, numbers)
    result_list = list(result_it)
    return result_list


# 5.Write a function that accepts string from user and print all permutations of that string.
def permutations(string: str) -> None:
    print([x for x in itertools.permutations(string, len(string))])


# 6.Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready
# are We
def reverse_words(sentence: str) -> str:
    reversed_words: list = reversed(sentence.split())
    return " ".join(reversed_words)


# 7.Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
#     def has_33(nums):
#         pass
#
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False
def has_33(nums: list) -> bool:
    for i in range(len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True
    return False


# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order
# def spy_game(nums):
#     pass
#
#     spy_game([1,2,4,0,0,7,5]) --> True
#     spy_game([1,0,2,4,0,5,7]) --> True
#     spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(nums: list) -> bool:
    nums = sorted(nums, key=lambda x: x == 0) # нолики в начало
    return nums[:3] == [0, 0, 7]


# 9. Write a function that computes the volume of a sphere given its radius.
def sphere_volume(radius: float) -> float:
    return (4 / 3) * (math.pi * (radius ** 3))


# 10.Write a Python function that takes a list and returns a new list with unique elements of the first list. Note:
# don't use collection set.
def unique_list(numbers: list) -> list:
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


# 11. Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word,
# phrase, or sequence that reads the same backward as forward, e.g., madam
def is_palindrome(string: str) -> bool:
    return string == string[::-1]


# 12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example,
# histogram([4, 9, 7]) should print the following:
#
# ****
# *********
# *******
def histogram(numbers: list) -> None:
    for num in numbers:
        print('*' * num)


# 13. Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen
# between 1 and 20. This is how it should work when run in a terminal:
#     Hello! What is your name?
#     KBTU
#
#     Well, KBTU, I am thinking of a number between 1 and 20.
#     Take a guess.
#     12
#
#     Your guess is too low.
#     Take a guess.
#     16
#
#     Your guess is too low.
#     Take a guess.
#     19
#
#     14.
#     Good job, KBTU! You guessed my number in 3 guesses!
def guess_the_number() -> None:
    name: str = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number: int = random.randint(1, 20)
    i: int = 1
    while True:
        print("Take a guess.")
        guess: int = int(input())
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break
        i += 1
    print(f"Good job, {name}! You guessed my number in {i} guesses!")
    return

# Create a python file and import some of the functions from the above 13 tasks and try to use them.
# in file try_to_use_functions.py