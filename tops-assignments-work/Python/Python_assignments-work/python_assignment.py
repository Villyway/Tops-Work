                                            # ------------ MODULE 7 - INTRODUCTION TO PYTHON ------------ #



# 1. What are the types of Applications?
   Applications are of following types:

    * Desktop Applications (Calculator, MS Word)
    * Web Applications (Google, Facebook)
    * Mobile Applications (WhatsApp, Instagram)
    * Embedded Applications (ATM machines, washing machines)

# 2. What is programming?
   Programming means writing instructions for a computer to perform specific tasks using a programming language.

# 3. What is Python?
   Python is a high-level, easy-to-learn programming language. It is used in web development, data analysis, automation, AI, etc.

# 4. Write a Python program to check if a number is positive, negative or zero.

    num = int(input("Enter number: "))

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# 5. Write a Python program to get the factorial number of given numbers.

    num = int(input("Enter number: "))
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial is:", fact)

# 6. Write a Python program to get the Fibonacci series of given range.

    n = int(input("Enter range: "))
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# 7. How memory is managed in Python?
    Python uses automatic memory management. It uses garbage collection to remove unused objects automatically, so the programmer does not need to manage memory manually.

#  8. What is the purpose of continue statement in Python?
    The continue statement is used to skip the current iteration of a loop and move to the next iteration.

    Example

    for i in range(1, 6):
        if i == 3:
            continue
        print(i)


# 9. Write python program that swap two numbers with temp variable and without temp variable.

# With temp variable:

    a = 10
    b = 20

    temp = a
    a = b
    b = temp
    print(a, b)

# Without temp variable:

    a = 10
    b = 20

    a, b = b, a
    print(a, b)


# 10. Write a Python program to find whether a given number is even or odd.

    num = int(input("Enter number: "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# 11. Write a Python program to test whether a passed letter is a vowel or not.

    ch = input("Enter character: ")

    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Not Vowel")


# 12. Write a Python program to sum of three given integers. If two values are equal, sum will be zero.

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a == b or b == c or a == c:
        print(0)
    else:
        print(a + b + c)


# 13. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a == b or (a + b) == 5 or abs(a - b) == 5:
        print(True)
    else:
        print(False)

# 14. Write a python program to sum of the first n positive integers.

    n = int(input("Enter n: "))
    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum is:", total)

# 15. Write a Python program to calculate the length of a string.

    s = input("Enter string: ")
    print(len(s))

# 16. Write a Python program to count the number of characters (character frequency) in a string.

    s = input("Enter string: ")
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    print(freq)

# 17. What are negative indexes and why are they used?
    Negative indexing means accessing elements from the end of a sequence.
    Example: -1 is last element, -2 is second last. It is used for easy reverse access.

# 18. Write a Python program to count occurrences of a substring in a string.

    s = input("Enter string: ")
    sub = input("Enter substring: ")

    print(s.count(sub))

# 19. Write a Python program to count the occurrences of each word in a given sentence.

    s = input("Enter sentence: ")
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    print(freq)

# 20. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

    a = input("Enter first string: ")
    b = input("Enter second string: ")
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    print(new_a + " " + new_b)

# 21. Write a Python program to add 'in' at the end of a given string. If it already ends with 'ing', add 'ly'. If length < 3, leave unchanged.

    s = input("Enter string: ")

    if len(s) < 3:
        print(s)
    elif s.endswith("ing"):
        print(s + "ly")
    else:
        print(s + "in")

# 22. Write a Python function to reverse a string if its length is a multiple of 4.

    def reverse_string(s):
        if len(s) % 4 == 0:
            return s[::-1]
        return s
    print(reverse_string(input("Enter string: ")))

# 23. Write a Python program to get a string made of first 2 and last 2 characters.

    s = input("Enter string: ")
    if len(s) < 2:
        print("")
    else:
        print(s[:2] + s[-2:])

# 24. Write a Python function to insert a string in the middle of a string.

    def insert_middle(s1, s2):
        mid = len(s1) // 2
        return s1[:mid] + s2 + s1[mid:]

    print(insert_middle("hello", "hi"))

# 25. What is List ? How will you reverse a list? List is an ordered and mutable collection.

    l = [1, 2, 3]
    l.reverse()
    print(l)

# 26. How will you remove last object from a list?

    l = [1, 2, 3]
    l.pop()
    print(l)

# 27. Suppose list1 is [2, 33, 222, 14, 25], what is list1[-1] ?
    Answer: 25

# 28. Differentiate between append() and extend() methods?
    append() adds a single element.
    extend() adds multiple elements.

# 29. Write a Python function to get the largest number, smallest number and sum of all elements from a list.

    def calculate(l):
        return max(l), min(l), sum(l)

    print(calculate([1, 2, 3, 4]))

# 30. How will you compare two lists?

    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    print(l1 == l2)

# 31. Write a Python program to count strings where length >=2 and first and last character are same.

    l = ["abc", "aba", "xyz", "aa"]
    count = 0
    for s in l:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    print(count)


# 32. Write a Python program to remove duplicates from a list.

    l = [1, 2, 2, 3]
    print(list(set(l)))

# 33. Write a Python program to check a list is empty or not.

    l = []
    if not l:
        print("Empty")

# 34. Write a Python function that takes two lists and returns true if they have at least one common member.

    def common(l1, l2):
        for i in l1:
            if i in l2:
                return True
        return False

# 35. Write a Python program to generate list of first and last 5 elements where values are squares of numbers between 1 and 30.

    l = [i * i for i in range(1, 31)]
    print(l[:5])
    print(l[-5:])

# 36. Write a Python function that returns unique elements of a list.

    def unique(l):
        return list(set(l))

# 37. Write a Python program to convert list of characters into a string.

    l = ['h', 'e', 'l', 'l', 'o']
    print("".join(l))

# 38. Write a Python program to select an item randomly from a list.

    import random
    l = [1, 2, 3, 4]
    print(random.choice(l))

# 39. Write a Python program to find second smallest number in a list.

    l = [4, 2, 1, 3]
    l = list(set(l))
    l.sort()
    print(l[1])

# 40. Write a Python program to get unique values from a list.

    l = [1, 2, 2, 3]
    print(list(set(l)))

# 41. Write a Python program to check whether a list contains a sub list.

    l = [1, 2, 3, 4]
    sub = [2, 3]
    for i in range(len(l) - len(sub) + 1):
        if l[i:i + len(sub)] == sub:
            print("Found")

# 42. Write a Python program to split a list into different variables.

    l = [1, 2, 3]
    a, b, c = l
    print(a, b, c)

# 43. What is tuple? Difference between list and tuple.
    Tuple is ordered and immutable collection.
    List is mutable, tuple is immutable.

# 44. Write a Python program to create a tuple with different data types.

    t = (1, "hello", 3.5, True)
    print(t)

# 45. Write a Python program to unzip a list of tuples into individual lists.

    l = [(1, 2), (3, 4), (5, 6)]
    a, b = zip(*l)
    print(list(a))
    print(list(b))


# 46. Write a Python program to convert a list of tuples into a dictionary.


    l = [(1, 'a'), (2, 'b'), (3, 'c')]

    d = dict(l)

    print(d)


# 47. How will you create a dictionary using tuples in python?
    A dictionary can be created by converting a list of tuples using dict() function.


    t = [(1, "one"), (2, "two")]

    d = dict(t)

    print(d)


# 48. Write a Python script to sort (ascending and descending) a dictionary by value.


    d = {'a': 3, 'b': 1, 'c': 2}

    asc = dict(sorted(d.items(), key=lambda x: x[1]))
    desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

    print("Ascending:", asc)
    print("Descending:", desc)


# 49. Write a Python script to concatenate following dictionaries to create a new one.


    d1 = {'a': 1}
    d2 = {'b': 2}

    d = {}
    d.update(d1)
    d.update(d2)

    print(d)


# 50. Write a Python script to check if a given key already exists in a dictionary.


    d = {'a': 1, 'b': 2}

    key = input("Enter key: ")

    if key in d:
        print("Key exists")
    else:
        print("Key not exists")


# 51. How Do You Traverse Through a Dictionary Object in Python?
    We use loop to traverse dictionary.


    d = {'a': 1, 'b': 2}

    for key, value in d.items():
        print(key, value)


# 52. How Do You Check the Presence of a Key in A Dictionary?
    We use "in" keyword.


    d = {'a': 1, 'b': 2}

    print('a' in d)


# 53. Write a Python script to print a dictionary where the keys are numbers between 1 and 15.


    d = {}

    for i in range(1, 16):
        d[i] = i * i

    print(d)


# 54. Write a Python program to check multiple keys exists in a dictionary.


    d = {'a': 1, 'b': 2, 'c': 3}

    keys = ['a', 'c']

    if all(k in d for k in keys):
        print("All keys exist")
    else:
        print("Keys missing")


# 55. Write a Python script to merge two Python dictionaries.


    d1 = {'a': 1}
    d2 = {'b': 2}

    d = {**d1, **d2}

    print(d)


# 56. Write a Python program to map two lists into a dictionary.


    keys = ['a', 'b', 'c', 'd']
    values = [400, 400, 300, 400]

    d = dict(zip(keys, values))

    print(d)


# 57. Write a Python program to find the highest 3 values in a dictionary.


    d = {'a': 10, 'b': 50, 'c': 30, 'd': 40}

    values = sorted(d.values(), reverse=True)

    print(values[:3])


# 58. Write a Python program to combine values in python list of dictionaries.


    from collections import Counter

    data = [
        {'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}
    ]

    result = Counter()

    for d in data:
        result[d['item']] += d['amount']

    print(result)


# 59. Write a Python program to create a dictionary from a string.


    s = input("Enter string: ")
    d = {}

    for ch in s:
        d[ch] = d.get(ch, 0) + 1

    print(d)


# 60. Sample string: 'w3resource' Expected output count of characters.


    s = "w3resource"
    d = {}

    for ch in s:
        d[ch] = d.get(ch, 0) + 1

    print(d)


# 61. Write a Python function to calculate the factorial of a number.


    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    print(factorial(5))


# 62. Write a Python function to check whether a number is in a given range.


    def check_range(n):
        if n in range(1, 11):
            return True
        return False

    print(check_range(5))


# 63. Write a Python function to check whether a number is perfect or not.


    def is_perfect(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n

    print(is_perfect(6))


# 64. Write a Python function that checks whether a passed string is palindrome or not.


    def palindrome(s):
        return s == s[::-1]

    print(palindrome("madam"))


# 65. How Many Basic Types of Functions Are Available in Python?
    There are mainly two types:

    * Built-in functions
    * User-defined functions

# 66. How can you pick a random item from a list or tuple?

    import random
    l = [1, 2, 3, 4]
    print(random.choice(l))

# 67. How can you pick a random item from a range?

    import random
    print(random.randrange(1, 10))

# 68. How can you get a random number in python?

    import random
    print(random.randint(1, 100))

# 69. How will you set the starting value in generating random numbers?

    import random
    random.seed(10)
    print(random.randint(1, 100))

# 70. How will you randomize the items of a list in place?

    import random
    l = [1, 2, 3, 4]
    random.shuffle(l)
    print(l)

# 71. What is File function in python? What are keywords to create and write file.
    
    File handling is used to read and write files.
    Modes:

    * "r" read
    * "w" write
    * "a" append

# 72. Write a Python program to read an entire text file.

    with open("file.txt", "r") as f:
        print(f.read())

# 73. Write a Python program to append text to a file and display the text.

with open("file.txt", "a") as f:
    f.write("Hello\n")

with open("file.txt", "r") as f:
    print(f.read())

# 74. Write a Python program to read first n lines of a file.

n = int(input("Enter n: "))
with open("file.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

# 75. Write a Python program to read last n lines of a file.

n = int(input("Enter n: "))
with open("file.txt", "r") as f:
    lines = f.readlines()

for line in lines[-n:]:
    print(line, end="")

# 76. Write a Python program to read a file line by line and store it into a list.

with open("file.txt", "r") as f:
    lines = f.readlines()
print(lines)

# 77. Write a Python program to read a file line by line store it into a variable.

with open("file.txt", "r") as f:
    data = f.read()
print(data)

# 78. Write a python program to find the longest words.

s = input("Enter sentence: ")
words = s.split()
longest = max(words, key=len)
print(longest)

# 79. Write a Python program to count the number of lines in a text file.

with open("file.txt", "r") as f:
    count = len(f.readlines())

print(count)

# 80. Write a Python program to count the frequency of words in a file.

with open("file.txt", "r") as f:
    words = f.read().split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# 81. Write a Python program to write a list to a file.

l = ["a", "b", "c"]
with open("file.txt", "w") as f:
    for i in l:
        f.write(i + "\n")

# 82. Write a Python program to copy the contents of a file to another file.

with open("file1.txt", "r") as f1:
    with open("file2.txt", "w") as f2:
        f2.write(f1.read())

# 83. Explain Exception handling? What is an Error in Python?
    
    Exception handling is used to handle runtime errors using try-except.
    Error is a problem in program which stops execution.

# 84. How many except statements can a try-except block have? Name some built-in exception classes.
    
    We can have multiple except blocks.
    Examples: ValueError, TypeError, ZeroDivisionError

# 85. When will the else part of try-except-else be executed?
    
    Else block runs when no exception occurs.

# 86. Can one block of except statements handle multiple exception?
    
    Yes, using tuple.

try:
    x = int("abc")
except (ValueError, TypeError):
    print("Error handled")


# 87. When is the finally block executed?
    Finally block always executes whether exception occurs or not.

# 88. What happens when '1' == 1 is executed?
    It returns False because one is string and other is integer.

# 89. How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets.

try:
    x = int(input("Enter number: "))
    y = 10 / x
    print(y)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")


# 90. Write python program that user to enter only odd numbers, else will raise an exception.

num = int(input("Enter number: "))

if num % 2 == 0:
    raise Exception("Even number not allowed")
else:
    print("Valid odd number")