            #Tuples
mytuple = ("apple", "banana", "cherry")

#create tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#tuple allow duplicate valuse
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#lenght
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#tuple with 1 item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#can be any datatype
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#can contain diff dt
tuple1 = ("abc", 34, True, 40, "male")

#datatype of tuple is tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#tuple() constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



        #Access Tuple Items
#indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])#2nd ellement
#neg indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#from start to n'th
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#fron n'th to last
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#range of neg indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#check if itex exist
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



            #Update Tuples
  #Change Tuple Values
#from tuple yo list then to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#tuple +tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#del tuple completaly
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists



        #Unpack Tuples
#
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits #red is list fromvherry to rasberry

print(green)
print(yellow)
print(red)

#
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)



            #Loop tuples
#for
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#while
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1



            #Join Tuples
#
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiply count of items
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

        #Tuple methods
"""
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
"""


    #Exercises
#1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])