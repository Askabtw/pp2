#operators
#1
print(10 + 5)

#Arithmetic Operators
"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""

#Assignment Operators
"""
=   	x = 5	  x = 5	
+=	    x += 3	  x = x + 3	
-=  	x -= 3	  x = x - 3	
*=  	x *= 3	  x = x * 3	
/=  	x /= 3	  x = x / 3	
%=  	x %= 3	  x = x % 3	
//= 	x //= 3	  x = x // 3	
**= 	x **= 3	  x = x ** 3	
&=  	x &= 3	  x = x & 3	
|=  	x |= 3	  x = x | 3	
^=  	x ^= 3	  x = x ^ 3	
>>= 	x >>= 3	  x = x >> 3	
<<= 	x <<= 3	  x = x << 3
"""

#Comparison Operators
"""
==	  Equal	                    x == y	
!=	  Not equal	                x != y	
>	  Greater than             	x > y	
<	  Less than	                x < y	
>=	  Greater than or equal to	x >= y	
<=	  Less than or equal to   	x <= y
"""

#Logical Operators
"""
and  	Returns True if both statements are true	x < 5 and  x < 10	
or	    Returns True if one of the statements is true	x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""

#Identity Operators
"""
is      	Returns True if both variables are the same object         	x is y	
is not	    Returns True if both variables are not the same object	 x is not y
"""

#Membership Operators
"""
in     	    Returns True if a sequence with the specified value is present in the object	x in y	
not in  	Returns True if a sequence with the specified value is not present in the object	x not in y
"""

#Bitwise Operators
"""
&    	AND 	Sets each bit to 1 if both bits are 1
|   	OR  	Sets each bit to 1 if one of two bits is 1
^   	XOR  	Sets each bit to 1 if only one of two bits is 1
~   	NOT 	Inverts all the bits
<<  	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>  	Signed right shift  	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""

#
print(10/2)

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

if 5 != 10:
  print("5 and 10 is not equal")

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")