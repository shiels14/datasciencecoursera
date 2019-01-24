Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> _author_ = 'dev'
>>> for i in range(1, 12):
	print("No {} squared is {} and cubed is {1:4}".format(i, i**2, i**4))

	
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    print("No {} squared is {} and cubed is {1:4}".format(i, i**2, i**4))
ValueError: cannot switch from automatic field numbering to manual field specification
>>> for i in range(1, 12):
	print("No {} squared is {} and cubed is {:4}".format(i, i**2, i**4))

	
No 1 squared is 1 and cubed is    1
No 2 squared is 4 and cubed is   16
No 3 squared is 9 and cubed is   81
No 4 squared is 16 and cubed is  256
No 5 squared is 25 and cubed is  625
No 6 squared is 36 and cubed is 1296
No 7 squared is 49 and cubed is 2401
No 8 squared is 64 and cubed is 4096
No 9 squared is 81 and cubed is 6561
No 10 squared is 100 and cubed is 10000
No 11 squared is 121 and cubed is 14641
>>> if(something) {
	
SyntaxError: invalid syntax
>>> print('Calculation complete")
	  
SyntaxError: EOL while scanning string literal
>>> print("Try again")
	  
Try again
>>> 
