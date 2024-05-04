#1
def gTOo(a):
    return float(float(a) * 28.3495231)

    a = 1
    print(gTOo(a))


#2
def FtoC(F):
    C = (5 / 9) * (float(F) - 32)
    return C

F = 1
print(FtoC(F))



#3
def solve(numheads, numlegs):
    for i in range(numheads):
        if (2*(i+1) + 4*(numheads-(i+1))) == numlegs:
            return i+1
        if (2*(numheads-(i+1)) + 4*(i+1)) == numlegs:
            return i+1
    return "NOT CORRECT INPUT"

print("count of heads")
numheads = 35
print("count of legs")
numlegs = 94


s = solve(numheads, numlegs)
if type(s) != type("qw"):
    if (2*s + 4*(numheads-s)) == numlegs:
      chi = int(s)
      rab = numheads - chi
      print("Rabbit:", rab, "Chicken:", chi  )
    else:
      rab = int(s)
      chi = numheads - rab
      print("Rabbit:", rab, "Chicken:", chi  )

else:
   print(s)




#4
def primeOnly(a):
    prime = []
    for i in a:
        temp = True
        for j in range(2, int(i)):
            if (int(i) % (j)) == 0:
                temp = False
                break      
        if temp:
          prime.append(i)
    return prime

a = [1, 2, 3, 4, 5, 6]
print(primeOnly(a))




#5
def permute(s, answer):
    if (len(s) == 0):
        print(answer, end="  ")
        return
 
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)
 
 
answer = ""
 
s = "ABCDE"
 
print("All possible strings are : ")
permute(s, answer)




#6
def reverse(s):
    rev = ""
    s = s.split(" ")
    cnt =-1
    for i in s:
        rev += " " +(s[cnt])
        cnt -= 1
    return rev.strip()

s = "We are ready"
print(reverse(s)
)



#7
def has_33(nums):
    for i in range(len(nums)):
        if i == len(nums)-1: continue
        if nums[i] == nums[i+1] == 3 : return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))



#8
def spy_game(nums):
    cnt = 0
    for i in range(len(nums)):
        if (nums[i] == 0):
            cnt += 1
        if nums[i]== 7:
           if cnt >=2: 
            return  True
           else:
            cnt =0
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0])) 



#9
def volumeOFsphere(rad):
    V = 4/3 * 3.1416 * rad**3
    return V 

rad = 3
print(round(volumeOFsphere(rad), 3)) 


#10
def unique(mylist):
    uni =[]
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            if mylist[i] == mylist[j] and i !=j:
                mylist[j] = "De1ete it"
    for i in range(len(mylist)):
        if mylist[i] == "De1ete it": continue
        uni.append(mylist[i])
    return uni

mylist = ['a','s', 'd', 'f', 'a', 'e', 'e']
print(unique(mylist))
    



#11
def polindrome(word):
    l = len(word)
    for i in range(l):
        if word[i] != word[l-i-1]: return False
        if l/2 > i: return True

word = "madam"
print(polindrome(word))
print(polindrome("miss"))
print(polindrome("mm"))


#12
def histogram(mylist):
    for i in mylist:
        for j in range(int(i)):
            print("*", end = "")
        if i != mylist[len(mylist)-1]: print()
    return ""

print(histogram([4, 9, 7]))




#13
def guess(min, max, guessed, num):
    if num < guessed: print("Your guess is too low.")
    if num > guessed: print("Your guess is too high.")
    print("Take a guess")
    return 0
    


print("what is your guessed number")
guessed = int(input())
print("print your lower num")
min = input()
print("print your higer num")
max = int(input())

print("Hello! What is your name?")
name = (input())
qwe = ("Well, {}, I am thinking of a number between {} and {}.")
print(qwe.format(name, min, max))
print("Take a guess")

cnt =0
temp = True
while(temp):
    cnt +=1
    num = int(input())
    if(num == guessed):
        fin = ("Good job, {}! You guessed my number in {} guesses!")
        print(fin.format(name,cnt))
        temp = False
        break
    guess(min, max, guessed, num)