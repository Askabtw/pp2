                #Sets
myset = {"apple", "banana", "cherry"}
#create set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#do not have duplicatete items
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Lenght
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Any datatype
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#diff data in 1set
set1 = {"abc", 34, True, 40, "male"}

#type of set is set
myset = {"apple", "banana", "cherry"}
print(type(myset))

#set() constractor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



        #Access set items
#acces from loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#check item is present in the set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#can't change its items


    #Add set items
#set.add()
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#another set to our set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# set.update() can work with lists, tuples, dict, etc like set.update(list) 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)



        #Remove set items
#set.remove()  chance of error
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#set.discard()
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#set.pop() - random remove
thisset = {"apple", "banana", "cherry"}

x = thisset.pop() # x is banana

print(x)

print(thisset)

#set.clear() - empty set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#del - delate set
thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset) error


    #Loop set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


        #Join set union()
#old sets on new one
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#old set on old one
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#no duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#set methods same with other ones


    #Exercises
#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")