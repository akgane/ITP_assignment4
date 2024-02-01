import math
from itertools import permutations

def generate_screen():
    print("-"*39)
    print("|" + (" " * 9) + "Roberto" + (" " * 21) + "|")
    print("|" + (" " * 37) + "|")
    print("|" + (" " * 9) + "5786" + (" " * 24) + "|")
    print("|" + (" " * 37) + "|")
    print("|" + (" " * 9) + "UNIFEI" + (" " * 22) + "|")
    print("-"*39)

def circumference(radius: float):
    if 0 >= radius > 10:
        print("Invalid radius.")
        return
    print(f"Circumference of circle of radius {radius} is {(2 * radius * math.pi):.2f}")


def calculate_total_gdp_fluctuation(f1, f2):
    if -100 > f1 > 100 or -100 > f2 > 100:
        print("Invalid input.")
        return
    print(f'{(((f2 - f1) / f1) * 100):.6f}')


def h_index(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i:
            return i


def bulls_and_cows():
    print("Check \"bulls_and_cows.py\" file")


def num_squares(n):
    if n <= 3:
        return n

    result = n
    for i in range(1, n + 1):
        temp = i * i
        if temp > n:
            break
        else:
            result = min(result, 1 + num_squares(n - temp))

    return result


def permutation(input_string):
    return [''.join(p) for p in permutations(input_string)]

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    perms = permutation(s1)
    for perm in perms:
        if perm in s2:
            return True
    return False

print(check_inclusion("ab", "eidboaoo"))