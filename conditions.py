#Python Conditions and If statements
#1 if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#2 elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b: # else if
  print("a and b are equal")

#3 else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#4
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#5 short if
if a > b: print("a is greater than b")

#6 short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

#7 and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#8 or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#9 nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#10 The pass statement
a = 33
b = 200

if b > a:
  pass

#exercise 1
a = 50
b = 10
if a >b:
  print("Hello World")
#2
a = 50
b = 10
if a !=b:
  print("Hello World")
#3
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")
#4
a = 50
b = 10
if a == b:
  print("1")
elif a >b:
  print("2")
else:
  print("3")
#5
a = b =c =d =1
if a == b and c == d:
  print("Hello")
#6
if a == b or c == d:
  print("Hello")
#7
if 5 > 2:
 print("Five is greater than two!")
#8
if 5 > 2: print("Five is greater than two!")
#9
print("Yes") if 5 > 2 else print("No")



  