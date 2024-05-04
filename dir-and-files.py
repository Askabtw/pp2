import os

#1
def dirs(dname):
    dirss = list()
    for i in os.listdir(dname):
        if not os.path.isfile(i):
            dirss.append(i)
    print(dirss)
    pass

def files(fname):
    filess = list()
    for i in os.listdir(fname):
        if os.path.isfile(i):
            filess.append(i)
    print(filess)
    pass

def fileanddir(fdname):
    print(os.listdir(fdname))

"""
name = input("input what do you wanna to see? \nFiles - 1 \nDirectories - 2\nFile and Dir - 3\n")
TF = True
if(name in '123'):
    paths = input("in wich path?\n")
    if not os.path.exists(paths):
        print('Path not exist')
        TF = False        
else:
    print('not correct input')
    TF = False
    
if TF:
    if name == '1':
        files(paths)
    elif name == '2':
        dirs(paths)
    elif name == '3':
        fileanddir(paths)
"""


#2
"""
pname = input('What is your path?\n')

#Existence
if os.path.exists(pname):
    print('Path is exist')
else:
    print('Path is not exist')

#Readability
if os.access(pname, os.R_OK):
    print('Path is readiable')
else:
    print('Path is not readiable')

#Writability
if os.access(pname, os.W_OK):
    print('Path is writiable')
else:
    print('Path is not writiable')

#Exacuatibility
if os.access(pname, os.X_OK):
    print('Path is exacutable')
else:
    print('Path is not exacutable')
"""


#3
"""
pname = input('What is your path?\n')

if os.path.exists(pname):
    print('Path is exist')
    TF = True
else:
    print('Path is not exist')
    TF = False

if TF:
    if os.path.isfile(pname): #Directory name neadable? if yes we can delete that line
        print(os.path.basename(pname))
    print('Directory:\n' + os.path.dirname(pname))
"""


#4
"""
fname = input()
path =open(fname)
lines =path.readlines()
print(len(lines))
"""


#5
"""
fname = input("FIle name is: ")
if os.path.exists(fname):
    fw = open(fname, mode = 'w')
    ls = [1, 2, 3, 4] #input("list is: ")
    if type(ls) == type(list()):
        fw.write(str(ls))
        fw.close()
    else:
        print(ls, "is not list")
else:
    print(fname, "is not exist")
"""

#6
"""
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in alphabet:
    fopen = open(i +".txt", mode = 'x')
    fopen.close()
"""

#7
"""
fname =open("dir-and-files.py", mode = 'r')
content = fname.read()
fname1 = open("dir-and-files1.py", mode = 'w')
fname1.write(str(content))
fname.close()
fname1.close()
"""


#8
path = input("Path: ")
if os.path.exists(path):
    if os.access(path, os.X_OK):
        os.remove(path)
    else:
        print('no access for deleding')
else:
    print("path is not exist")