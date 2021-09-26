# input() 
print('What is your name?')   # ask for their name
myName = input()
print('It is good to meet you, {}'.format(myName))

# len()
len('hello')

# str() int()
str(29)
int(7.7)

# bool
a = (4 < 5) and (5 < 6)
b = (1 == 2) or (2 == 2)
age = 3

if a is True:
   pass
if a is not False:
   pass
if a:
   pass
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('Hello, stranger.')


# while
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')


# for 
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
print('My name is')
spam = ['cat', 'bat', 'rat', 'elephant']
for i in range(5):
    print('Jimmy Five Times ({})'.format(str(i)))

for i in range(0, 10, 2):
   print(i)

for i in range(5, -1, -1):
    print(i)

for v in spam().values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)


# global Value
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)


# negative Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print(spam[-3])

# lists
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]

[1, 2, 3] + ['A', 'B', 'C'] # concat
['X', 'Y', 'Z'] * 3

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i, supply in enumerate(supplies):
    print('Index {} in supplies is: {}'.format(str(i), supply))

'howdy' in ['hello', 'hi', 'howdy', 'heyas']
'cat' not in spam

# set 
s = {1, 2, 3}
s = set([1, 2, 3])
 # add() update() remove() discard() s1.intesection(a,b,c) union(a,b) s1.difference()   

# iterator combinations() count() cylce() chain() compress() dropwhile() filterfals() groupby() islice() permutations() product() repeat() 

[i - 1 for i in a]
{s.upper() for s in b}
# \'	Single quote
# \"	Double quote
# \t	Tab
# \n	Newline (line break)
# \\	Backslash
# Removing Whitespace with strip()

import re
# Regular Expresion
# Path Files reading and writing json und debugging

add = lambda x, y: x + y
(lambda x, y: x + y)(5, 3)

# spam /= 1 ...
# index() für listen
# append() insert() und remove()
# sort()
# tupel() list()

eggs = ('hello', 42, 0.5)
eggs[0]

# Get has two parameters: key and default value if the key did not existGet has two parameters: key and default value if the key did not exist
#

@dataclass
class Product:
    name: str
    count: int = 0
    price: float = 0.0
obj = Product("Python")
obj.name
obj.count
0
obj.price
0.0
