Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MyClass:
	def_init_(self, Name="Sam",Age=32):
		
SyntaxError: invalid syntax
>>> self.Name = Name
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    self.Name = Name
NameError: name 'Name' is not defined
>>> self.Age = Age
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    self.Age = Age
NameError: name 'Age' is not defined
>>> def GetName(self) :
	return self.Name
def SetName(self, Name) :
	
SyntaxError: invalid syntax
>>> self.Name = Name
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    self.Name = Name
NameError: name 'Name' is not defined
>>> x = 12
>>> x = 10
>>> x = 13
>>> x = 15
>>> x = 16
>>> x = 18
>>> x = 19
>>> x = 20
>>> x = 234
>>> x ** = 12
SyntaxError: invalid syntax
>>> name = input("Give me your name: ")
Give me your name: Stephen Shiels
>>> print("Your name is " + Stephen Shiels)
SyntaxError: invalid syntax
>>> print("Your name is " + Stephen Shiels")
	  
SyntaxError: invalid syntax
>>> print("My name is Stephen Shiels")
	  
My name is Stephen Shiels
>>> Give me your name: Stephen Shiels
	  
SyntaxError: invalid syntax
>>> age = input("25")
	  
25
>>> age = int(age)
	  
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    age = int(age)
ValueError: invalid literal for int() with base 10: ''
>>> age = int(input("25:"))
	  
25:
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    age = int(input("25:"))
ValueError: invalid literal for int() with base 10: ''
>>> print("were = wolf")
	  
were = wolf
>>> print "Were" + "wolf")
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Were" + "wolf"))?
>>> print("Were" + "wolf")
Werewolf
>>> print("Door" + "man")
Doorman
>>> print("4" + "chan")
4chan
>>> print(str(4) + "chan")
4chan
>>> print(4 * "test")
testtesttesttest
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
>>> if age > 17:
	print("can see a rated R movie")
	elif age < 17 and age > 12:
		
SyntaxError: invalid syntax
>>> print("can see a rated PG-13 movie")
can see a rated PG-13 movie
>>> else:
	
SyntaxError: invalid syntax
>>> print("can only see rated PG movies")
can only see rated PG movies
>>> if a == 3:
	print("the variable has the value 3")
	elif a != 3:
		
SyntaxError: invalid syntax
>>> print("the variable does not have the value 3")
the variable does not have the value 3
>>> if a == 3:
	print("the variable has the value 3")
	else:
		
SyntaxError: invalid syntax
>>> print("the variable does not have the value 3")
the variable does not have the value 3
>>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> x = []
>>> x = []
>>> x.append(3)
>>> my_list = [1, 3, "Stephen Shiels", [5,6,7]]
>>> for element in my_list:
	print(element)

	
1
3
Stephen Shiels
[5, 6, 7]
>>> grade = input("90:")
90:
>>> if grade >= 90:
	print("A")
	elif grade >= 80:
		
SyntaxError: invalid syntax
>>> print("B")
B
>>> elif grade >= 70:
	
SyntaxError: invalid syntax
>>> print("C")
C
>>> elif grade >= 65:
	
SyntaxError: invalid syntax
>>> print("D")
D
>>> else:
	
SyntaxError: invalid syntax
>>> print("F")
F
>>> x = range(2, 11)
>>> [2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for elem in x:
	print elem
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(elem)?
>>> for elem in x:
	print("elem")

	
elem
elem
elem
elem
elem
elem
elem
elem
elem
>>> for elem in x:
	print("2, 3, 4, 5, 6, 7, 8, 9, 10")

	
2, 3, 4, 5, 6, 7, 8, 9, 10
2, 3, 4, 5, 6, 7, 8, 9, 10
2, 3, 4, 5, 6, 7, 8, 9, 10
2, 3, 4, 5, 6, 7, 8, 9, 10
2, 3, 4, 5, 6, 7, 8, 9, 10
2, 3, 4, 5, 6, 7, 8, 9, 10
2, 3, 4, 5, 6, 7, 8, 9, 10
2, 3, 4, 5, 6, 7, 8, 9, 10
2, 3, 4, 5, 6, 7, 8, 9, 10
>>> a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 113]
>>> a = [5, 10, 15, 20]
>>> 10 in a
True
>>> 3 in a
False
>>> list_of_students = ["Stephen" ,"Shiels", "Joeseph"]
>>> name = input("Type name to check: ")
Type name to check: 
>>> if name in list_of_students:
	print("This student is enrolled.")

	
>>> a = [5, 10, 15, 20, 25]
>>> a[3]
20
>>> a[0]
5
>>> a = [5, 10, 15, 20, 25, 30, 35, 40]
>>> a[1:4]
[10, 15, 20]
>>> a[6:]
[35, 40]
>>> a[:-1]
[5, 10, 15, 20, 25, 30, 35]
>>> a = [5, 10, 15, 20, 25, 30, 35, 40]
>>> a[1:5:2]
[10, 20]
>>> a[3:0:-1]
[20, 15, 10]
>>> string = "example"
>>> for c in string:
	print("one letter: " + c")
	      
SyntaxError: EOL while scanning string literal
>>> string = "example"
	      
>>> for c in string:
	      print "one letter: " + c
	      
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("one letter: " + c)?
>>> string = "example"
	      
>>> s = string[0:5]
	      
>>> print s
	      
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(s)?
>>> examp
	      
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    examp
NameError: name 'examp' is not defined
>>> a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	      
>>> years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
	      
>>> ages = []
	      
>>> for year in years_of_birth:
	      ages.append(2014 - year)

	      
>>> a = 5
	      
>>> while (a > 0):
	      print(a)
	      a-=1

	      
5
4
3
2
1
>>> quit = input('Type "enter" to quit:' )
	      
Type "enter" to quit:
>>> while quit != "enter":
	      quit = input('Type "enter" to quit:' )

	      
Type "enter" to quit:
Type "enter" to quit:enter
>>> i = 5
	      
>>> while i > 0:
	      print("Inside the loop")

	      
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
TInside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Inside the loop
Traceback (most recent call last):
  File "<pyshell#127>", line 2, in <module>
    print("Inside the loop")
KeyboardInterrupt
>>> while True:
	      usr_command = input("Enter your command: ")
	      if usr_command == "quit":
	      break
	      
SyntaxError: expected an indented block
>>> else:
	      
SyntaxError: invalid syntax
>>> print("You typed " + usr_command)
	      
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    print("You typed " + usr_command)
NameError: name 'usr_command' is not defined
>>> 
