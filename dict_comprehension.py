'''
@author: Shivam Mishra
@date: 22-12-21 7:53 PM
@desc: practice problems for dictionary comprehension
'''

# Use a dictionary comprehension to count the length of each word in a sentence
string = {"Practice Problems to Drill Dictionary Comprehension in Your Head."}
dict = {k: v for (k,v) in string}
print(dict)


