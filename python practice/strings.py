Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> _author_ = 'dev'
>>> age = 24
>>> print("My age is" + age + "years")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("My age is" + age + "years")
TypeError: can only concatenate str (not "int") to str
>>> print("My age is" + str(age) + " years")
My age is24 years
>>> print("My age is {0} years".format(age))
My age is 24 years
>>> print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format, "January", "March", "May", "July", "August", "October", "December"))
SyntaxError: invalid syntax
>>> print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format,(31, "January", "March", "May", "July", "August", "October", "December"))
<built-in method format of str object at 0x109685180> (31, 'January', 'March', 'May', 'July', 'August', 'October', 'December')
>>> print("""January: {2}
Feburay: {0}
March: {2}
April: {1}
May: {2}
June {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))
January: 31
Feburay: 28
March: 31
April: 30
May: 31
June 30
July: 31
August: 31
September: 30
October: 31
November: 30
December: 31
>>> print("My age is %D years" % age)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print("My age is %D years" % age)
ValueError: unsupported format character 'D' (0x44) at index 11
>>> print("My age is %d years" % age)
My age is 24 years
>>> print("My age is %d %s" % (age, "years", 6, "months"))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print("My age is %d %s" % (age, "years", 6, "months"))
TypeError: not all arguments converted during string formatting
>>> print("My age is %d %s, %d %s % (age, "years" , 6, "months"))
	  
SyntaxError: invalid syntax
>>> print("My age is %d years" % age)
	  
My age is 24 years
>>> print("My age is %d %s, %d %s % (age, "24" , 6, "months"))
	  
SyntaxError: invalid syntax
>>> print("My age is %d %s, %d %s % (age, "" , 6, "months"))
	  
SyntaxError: invalid syntax
>>>  print("My age is %d %s, %d %s % (age, "24" , 6, "months"))
	   
SyntaxError: unexpected indent
>>> for i in range(1, 12):
	   print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

	   
No.  1 squared is    1 and cubed is    1
No.  2 squared is    4 and cubed is    8
No.  3 squared is    9 and cubed is   27
No.  4 squared is   16 and cubed is   64
No.  5 squared is   25 and cubed is  125
No.  6 squared is   36 and cubed is  216
No.  7 squared is   49 and cubed is  343
No.  8 squared is   64 and cubed is  512
No.  9 squared is   81 and cubed is  729
No. 10 squared is  100 and cubed is 1000
No. 11 squared is  121 and cubed is 1331
>>> print("Pi is approximately %12f" % ( 22 / 7))
	   
Pi is approximately     3.142857
>>> print("Pi is approximately %12.50f" % ( 22 / 7))
	   
Pi is approximately 3.14285714285714279370154144999105483293533325195312
>>> for i in range(1, 12):
	   print("No. %2d squared is {1:4} and cubed is {2:4}" %(i, i ** 2, i ** 3))

	   
Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    print("No. %2d squared is {1:4} and cubed is {2:4}" %(i, i ** 2, i ** 3))
TypeError: not all arguments converted during string formatting
>>> for i in range(1, 12):
	   print("No. {0:2} squared is {1:4} and cubed is {2:4}" %(i, i ** 2, i ** 3))

	   
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print("No. {0:2} squared is {1:4} and cubed is {2:4}" %(i, i ** 2, i ** 3))
TypeError: not all arguments converted during string formatting
>>> for i in range(1, 12):
	   print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

	   
No.  1 squared is    1 and cubed is    1
No.  2 squared is    4 and cubed is    8
No.  3 squared is    9 and cubed is   27
No.  4 squared is   16 and cubed is   64
No.  5 squared is   25 and cubed is  125
No.  6 squared is   36 and cubed is  216
No.  7 squared is   49 and cubed is  343
No.  8 squared is   64 and cubed is  512
No.  9 squared is   81 and cubed is  729
No. 10 squared is  100 and cubed is 1000
No. 11 squared is  121 and cubed is 1331
>>> for i in range(1, 12):
	   print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

	   
No.  1 squared is 1    and cubed is 1   
No.  2 squared is 4    and cubed is 8   
No.  3 squared is 9    and cubed is 27  
No.  4 squared is 16   and cubed is 64  
No.  5 squared is 25   and cubed is 125 
No.  6 squared is 36   and cubed is 216 
No.  7 squared is 49   and cubed is 343 
No.  8 squared is 64   and cubed is 512 
No.  9 squared is 81   and cubed is 729 
No. 10 squared is 100  and cubed is 1000
No. 11 squared is 121  and cubed is 1331
>>> for i in range(1, 12):
	   print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

	   
No.  1 squared is 1    and cubed is 1   
No.  2 squared is 4    and cubed is 8   
No.  3 squared is 9    and cubed is 27  
No.  4 squared is 16   and cubed is 64  
No.  5 squared is 25   and cubed is 125 
No.  6 squared is 36   and cubed is 216 
No.  7 squared is 49   and cubed is 343 
No.  8 squared is 64   and cubed is 512 
No.  9 squared is 81   and cubed is 729 
No. 10 squared is 100  and cubed is 1000
No. 11 squared is 121  and cubed is 1331
>>> print("Pi is approximately {0:12.50}".format ( 22 / 7))
	   
Pi is approximately 3.1428571428571427937015414499910548329353332519531
>>> 
