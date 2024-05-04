            #List
thislist = ["apple", "banana", "cherry"]
print(thislist)

#list allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#list lenght
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list can be any datatype
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#list can contain diff datetypes
list1 = ["abc", 34, True, 40, "male"]

#type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#the list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#range index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#[:4] from 1st index until 4th
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#[2:] from 2nd to last
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#neg indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)



            #insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Append Items to end of list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#append list to list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable : (tuples, sets, dictionaries etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



            #Python - remove list items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#remove last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) 

#del
thislist = ["apple", "banana", "cherry"]
del thislist[0] # = list.pop(0)
print(thislist)
#can delate the list completely
thislist = ["apple", "banana", "cherry"]
del thislist

#empty list with no elements
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



                #loop lists
#print all items
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#list comprehansion
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# same but in 1 line
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


    #the syntax
#newlist = [expression for item in iterable if condition == True]

#condition
newlist = [x for x in fruits if x != "apple"]

# witn no if statement
newlist = [x for x in fruits]


   #Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
#same example but with condition
newlist = [x for x in range(10) if x < 5]

#Expression
newlist = [x.upper() for x in fruits] #Set the values in the new list to upper case

newlist = ['hello' for x in fruits] #Set all values in the new list to 'hello'

newlist = [x if x != "banana" else "orange" for x in fruits] #Return "orange" instead of "banana"    #"Return the item if it is not banana, if it is banana return orange"    



                #sort
#sort alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sort decending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


   #customize sort function
def myfunc(n):
  return abs(n - 50) #sort by how close to 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#uppercase before lowercase
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#sort first lowercase
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#Reverse
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


          #       Copy list
#cannot write list2 =list1. changes in list2 will be in list2
#right copy:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


                #Join Lists
#easiest way by +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#one by one
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


                #Exercises
#1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))