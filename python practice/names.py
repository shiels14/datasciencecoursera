Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> _author_ = 'dev'
>>> name = input("Please enter your name: ")
Please enter your name: age = input("How old are you, {0}? ".format(name))
>>> print(age)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(age)
NameError: name 'age' is not defined
>>> print(age)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(age)
NameError: name 'age' is not defined
>>> name = input("Please enter your name: ")
Please enter your name: Stephen
>>> age = input("How old are you, {0}? ".format(name))
How old are you, Stephen? 25
>>> print(age)
25
>>> age = int(input("How old are you, {0}? ".format(name))

if age >= 18:
	      
SyntaxError: invalid syntax
>>> if age >= 18:
	      print("You are old enough to vote")

	      
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    if age >= 18:
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> else:
	      
SyntaxError: invalid syntax
>>> print("Please come back in {0}".format(18 - age))
	      
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("Please come back in {0}".format(18 - age))
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> print("Please put an X in the box")
	      
Please put an X in the box
>>> print("Please guess a number between 1 and 10: ")
	      
Please guess a number between 1 and 10: 
>>> guess = Int(input())
	      
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    guess = Int(input())
NameError: name 'Int' is not defined
>>> if guess < 5:
	      print("Please guess higher")
	      guess = Int(input())
	      if guess == 5:
	      print("Well done, you guessed it")
	      
SyntaxError: expected an indented block
>>> else:
	      
SyntaxError: invalid syntax
>>> print('Sorry, you have not guessed correctly.")
	  
SyntaxError: EOL while scanning string literal
>>> elif guess > 5:
	  
SyntaxError: invalid syntax
>>> print("Please guess lower")
	  
Please guess lower
>>> print("Well done, you guessed it")
	  
Well done, you guessed it
>>> else:
	  
SyntaxError: invalid syntax
>>> print("Sorry, you have not guessed correctly")
	  
Sorry, you have not guessed correctly
>>> else:
	  
SyntaxError: invalid syntax
>>> print("You got it first time")
	  
You got it first time
>>> 5
	  
5
>>> 
