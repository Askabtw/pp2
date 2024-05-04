#strings
print("Hello")
print('Hello')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" #or '''  ''' instead of """  """
print(a)

a = "Hello, World!"
print(a[1]) # a[1] = e

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

#check
txt = "The best things in life are free!"
print("free" in txt) #true

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#Slicing strings
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2]) #-1 = d, -2 = l, ...


#Modify strings
a = "Hello, World!"
print(a.upper())#HELLO, WORLD!

a = "Hello, World!"
print(a.lower())#hello, world

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


a = "Hello, World!"
print(a.replace("H", "J"))#Jello, World!


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#string Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)


#String format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



#Escape Characters
txt = "We are the so-called \"Vikings\" from the north."

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	"""