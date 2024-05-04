            #For loop
#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
  print(x)

#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#range() - ranage(6) = [0 - 5]
for x in range(2, 6):  #The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
  print(x)
#Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
  print(x)


#Else
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#else won't work
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#Nested loops - loop in loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass Statement
for x in [0, 1, 2]:
  pass
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.


#exercises
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":    
    continue
  print(x)
#3
for x in range(6):
    print(x)
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":    
    break
  print(x)