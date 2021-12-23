'''
@author: Shivam Mishra
@date: 22-12-21 7:53 PM
@desc: practice problems for dictionary comprehension
'''

# Use a dictionary comprehension to count the length of each word in a sentence
string = "Practice Problems to Drill Dictionary Comprehension in Your Head."
dict = {word:len(word) for word in string.split(" ")}
print(dict)

# flipping key value pair
a = {"a":10, "b":20, "c":30}
dict = {a[i]:i for i in a}
print(dict)

# manipulating both key and value
a = {"a":10, "b":20, "c":30}
dict = {"Letter "+i:a[i]+1000 for i in a}
print(dict)

# Use a nested list comprehension to find
# all of the numbers from 1–100 that are divisible by any single digit besides 1 (2–9)
nums = [i for i in range(1,101)]
answer = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
print(answer)


