#1
numlist = list((1, 2, 3, 4, 5, 6))
multiply = 1
for i in numlist: multiply*=i

#print(multiply)


import re
#2
"""
word = "AZXSDfwef42A 4654 sdfwedc "
patA = r'[A-Z]'
Amath = re.findall(patA, word)
pata = r'[a-z]'
amath = re.findall(pata, word)

print("Uppercase: ", len(Amath))
print("Lowercase: ", len(amath))
"""


#3
"""
def polindrome(word):
    l = len(word)
    for i in range(l):
        if word[i] != word[l-i-1]: return False
        if l/2 > i: return True

word = "madam"
print(polindrome(word))
print(polindrome("miss"))
print(polindrome("mm"))
"""



import time
import math
#4
"""
num = int(input("Number: "))
ms = int(input("Number of milliseconds: "))
sec = ms / 1000
time.sleep(sec)
sqms = math.sqrt(num)
print(f"Square root of {num} after {ms} milliseconds is {sqms}")
"""


#5
mytuple1 = tuple((True, True, True, True))
mytuple2 = tuple((True, True, False, True))
mytuple3 = tuple(("", 12, "esdf"))

res = all(mytuple3)
if res:
    print(res)
else:
    print(res)