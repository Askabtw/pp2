#while
#
i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#ex
i =1
while i<6:
    print(i)
    i+=1

#ex2
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")