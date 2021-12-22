'''
@author: Shivam Mishra
@date: 22-12-21 1:17 PM
@decs: practice problems for list comprehension
'''

numbers = range(0,51)
even_numbers = [x for x in numbers if x%2 == 0 ]
print(even_numbers)


rows, cols = [4, 4]
list = [[x for x in range(rows)] for y in range(cols)]
print(list)
list.append([12,45,20])
print(list)

# Find all of the numbers from 1–100 that are divisible by 8
list = [x for x in range(1,101) if x%8 == 0]
print(list)

# Find all of the numbers from 1–100 that have a 6 in them
num = range(1,101)
list = [y for y in num if "6" in str(y)]
print(list)

# Count the number of spaces in a string
str = "Python is very easy programming language"
count = len([x for x in str if x == " "])
print(count)

# Find all of the words in a string that are less than 5 letters
str = "Python is very easy programming language"
words = [x for x in str.split(" ") if x.__len__()<5]
print(words)

# Remove all of the vowels in a string
str = "Python is very easy programming language"
vow = "".join([char for char in str if char not in ["a","e","i","o","u"]])
print(vow)
vowels = [x for x in str if x=="a" or x=="e" or x=="i" or x=="o" or x=="u"]
print(vowels)

#