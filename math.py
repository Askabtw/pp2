import math
#1
deg = int(input("Input degree: "))
rad = round(math.radians(deg), 8)
print(f"Output radian: {rad}")


#2
h = 5
base1 = 5
base2 = 6
area = (base1 + base2) *h/2
print(area)


#3
numside = 4
lenghside = 25
area = area = (numside * lenghside ** 2) / (4 * math.tan(math.pi / numside))
print(round(area, 8))


#4
lenghbase = 5
h = 6
area = lenghbase * h
print(area)