#1
import math

def nsquare(n):
    for i in range(n):
        yield pow(i+1, 2)

#for i in nsquare(int(input())):
#    print(i)


#2
def even(n):
    for i in range(1, n):
        if(i%2 == 0):
            yield i

#for i in even(int(input())):
#   print(i, end = ", ")



#3
def div3and4(n):
    i = 12
    while i <n:
        yield i
         
        i += 12

#for i in div3and4(int(input())):
#   print(i)



#4
def squares(a, b):
    for i in range(a, b+1):
        yield pow(i, 2)

#for i in squares(int(input()), int(input())):
#   print(i)



#5
def decending(n):
    for i in range(n):
        yield n - i

#for i in decending(int(input())):
#   print(i)