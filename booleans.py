#Boolean
#1
print(10 > 9) #TRUE
print(10 == 9) #FALSE
print(10 < 9) #FALSE

#2
a = 200
b = 33

if b > a:
  print("b is greater than a") #won't print 
else:
  print("b is not greater than a") #will print

#3
print(bool("Hello")) #TRUE
print(bool(15)) #FALSE

#4
x = "Hello"
y = 15

print(bool(x)) #TRUE
print(bool(y)) #TRUE

#5 all true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#6 all False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))#False

#8
def myFunction() :
  return True

print(myFunction())#TRUE

#9
def myFunction() :
  return True

if myFunction():
  print("YES!")#will print
else:
  print("NO!")

#10
x = 200
print(isinstance(x, int)) #TRUE