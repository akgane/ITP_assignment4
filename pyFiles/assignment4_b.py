from itertools import permutations

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
strings = ["Hello", "my", "NAME", "world", "something", "long string"]
vowels = ['a', 'e', 'i', 'o', 'u']


def task1(numbers):
    squares = list(map(lambda n: n ** 2, numbers))
    print(squares)


def task2(numbers):
    evens = list(filter(lambda n: n % 2 == 0, numbers))
    print(evens)


def task3(strings):
    uppercases = list(map(lambda s: s.upper(), strings))
    print(uppercases)


def task4(strings):
    result = list(filter(lambda s: len(s) > 5, strings))
    print(result)


def task5(fahrenheits):
    celsius = list(map(lambda f: (5 / 9) * (f - 32), fahrenheits))
    print(celsius)


def check_prime(number: int):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def task6(numbers):
    primes = list(filter(lambda n: check_prime(n), numbers))
    print(primes)


def task7(first, second):
    if len(first) != len(second):
        print("Length mismatch")
        return
    result = list(map(lambda f, s: f ** 2 + s ** 2, first, second))
    print(result)


def task8(strings):
    palindromes = list(filter(lambda s: s == s[::-1], strings))
    print(palindromes)


def task9(strings):
    lengths = list(map(lambda s: len(s), strings))
    print(lengths)


def task10(numbers):
    positives = list(filter(lambda n: n > 0, numbers))
    print(positives)


def task11(n):
    fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
    result = list(map(fib, range(n)))
    print(result)


def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


def task12(strings):
    anagrams = list(filter(lambda pair: check_anagram(pair[0], pair[1]), permutations(strings, 2)))
    print(anagrams)


def check_vowels(s):
    for c in s:
        if not c.isalpha() or c.lower() in vowels:
            return False
    return True


def task13():
    strings = ["abba", "bbb", "dfdgcxv", "adsvasdo"]
    consonants = list(filter(lambda s: check_vowels(s), strings))
    print(consonants)


def task15(numbers):
    perfect_squares = list(filter(lambda n: (n ** (1 / 2)) % 1 == 0, numbers))
    print(perfect_squares)


