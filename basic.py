firstname = "Bola"
lastname = " Winter"
fullname = firstname + lastname
print(fullname)

name = "Bob"
print("My name is " + name)

#Type conversion....changing from one data type to another
print(type(str(100)))
print(type(int("20")))
print(type(int(str(900))))

girl_age = 10
if girl_age < 15:
    print(fullname + " is a teenager")
else:
    print("She is not a teenager")

#Lists []
list1 = ["one","three","four","five","six"]
if "two" in list1:
    print("Two is present in list1")
else: 
    print(list1[3] + " is present in list 1")
list1.append("seven")
list1.insert(1,"two")
print(list1)
# To append elements from another list to the current list, use the extend() method.
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# The remove() method removes the specified item.
# The pop() method removes the specified index.#
# The clear() method empties the list.

#looping through a list
for lista in list1:
    print(lista)
    # the index is gotten
for indexa in range(len(list1)):
    print(indexa)
    # while loop
i = 0
while(i<len(list1)):
    print(list1[i])
    i = i + 2

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default
# To sort descending, use the keyword argument reverse = True:
list1.sort(reverse=True)
print(list1)

#Tuples ()
# You can convert the tuple into a list, change the list, and convert the list back into a tuple since a tuple is unchangeable.
tuplea = ("one","two","three","four")
listb = list(tuplea)
listb[2] = "five"
tuplea = tuple(listb)
print(tuplea)
#Adding a tuple to another tuple

#SETS {}
#A set is a collection which is unordered, unchangeable*, and unindexed.
set1 = {"a","b","c","d","e"}
print(set1)
print(1,000,000)

#Sorting words from longest to shortest
text = 'I love food but I love solid food the most'
words = text.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)



#formatted strings
name = "John"
age = 20
print("hi " + name + ", you are " + str(age) + " years old") #str is used to change to string, but this is cumbersome
print(f"hi {name}, you are {age} years old")
#Escape sequence and string indexes
#use of backslashes... \t for space \n for a new line
print("My Dad says \"welcome\" \nHe is greeting you")




