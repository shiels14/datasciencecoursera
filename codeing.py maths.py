Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> One = int(input("Type a number between 1 and 10: "))
Type a number between 1 and 10: 3
>>> Two = int(input("Type a number between 1 and 10: "))
Type a number between 1 and 10: 5
>>> if (One >= 1) and 9One <= 10):
	
SyntaxError: invalid syntax
>>> if (One >= 1) and (One <= 10):
	if (Two >= 1) and (Two <= 10):
		print('Your secret number is: ", One * Two)
		      
SyntaxError: EOL while scanning string literal
>>> else:
		      
SyntaxError: invalid syntax
>>> print("Incorrect second value!")
		      
Incorrect second value!
>>> else:
		      
SyntaxError: invalid syntax
>>> print("Incorrect first value!')
	  
SyntaxError: EOL while scanning string literal
>>> print("1. Eggs")
	  
1. Eggs
>>> print("2. Pancakes")
	  
2. Pancakes
>>> print("3. Waffles")
	  
3. Waffles
>>> print("4. Oatmeal")
	  
4. Oatmeal
>>> Mainchoice == 2):
		      
SyntaxError: invalid syntax
>>> Mainchoice = int(input('Choose a breakfast item: "))
			   
SyntaxError: EOL while scanning string literal
>>> MainChoice = int(input("Choose a breakfast item: "))
			   
Choose a breakfast item: Oatmeal
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    MainChoice = int(input("Choose a breakfast item: "))
ValueError: invalid literal for int() with base 10: 'Oatmeal'
>>> if 9Mainchoice == 2):
		     
SyntaxError: invalid syntax
>>> if (Mainchoice == 2):
		     Meal = "Pancakes"
		     elif (MainChoice == 3):
		     
SyntaxError: invalid syntax
>>> Meal = "Waffles"
		     
>>> if (MainChoice == 1):
		     print("1. Wheat Toast")
		     print("2. Sour Dough")
		     print("3. Rye Toast")
		     print("4. Pancakes")
		     Bread = int9input('Choose a type of bread: "))
				       
SyntaxError: EOL while scanning string literal
>>> Bread = int(input("Choose a type of bread: "))
				       
Choose a type of bread: Sour Dough
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    Bread = int(input("Choose a type of bread: "))
ValueError: invalid literal for int() with base 10: 'Sour Dough'
>>> if (Bread == 1):
				       print('You chose eggs with wheat toast.")
					     
SyntaxError: EOL while scanning string literal
>>> print("You chose eggs with wheat toast.")
					     
You chose eggs with wheat toast.
>>> elif (Bread == 2):
					     
SyntaxError: invalid syntax
>>> print("You chose eggs with sour dough.")
					     
You chose eggs with sour dough.
>>> elif (Bread == 3):
					     
SyntaxError: invalid syntax
>>> print("You chose eggs with rye toast.")
					     
You chose eggs with rye toast.
>>> elif (Bread == 4):
					     
SyntaxError: invalid syntax
>>> print("You chose eggs with pancakes.")
					     
You chose eggs with pancakes.
>>> else:
					     
SyntaxError: invalid syntax
>>> print("We have eggs, but not that kind of bread.")
					     
We have eggs, but not that kind of bread.
>>> elif (Mainchoice == 2) or (Mainchoice == 3):
					     
SyntaxError: invalid syntax
>>> print("1. Syrup")
					     
1. Syrup
>>> print("2. Strawberries")
					     
2. Strawberries
>>> print("3. Powdered Sugar")
					     
3. Powdered Sugar
>>> Topping = int(input('Choose a topping: "))
			
SyntaxError: EOL while scanning string literal
>>> Topping = int (input('Choose a topping: "))
			 
SyntaxError: EOL while scanning string literal
>>> if (Topping == 1):
			 print ("You chose " + Meal + " with syrup.")
			 elif (Topping == 2):
			 
SyntaxError: invalid syntax
>>> print ("You chose " + Meal + " with strawberries.")
			 
You chose Waffles with strawberries.
>>> elif (Topping == 3):
			 
SyntaxError: invalid syntax
>>> print 9"You chose " + Meal + " with powdered sugar.")
		   
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(9"You chose " + Meal + " with powdered sugar."))?
>>> else:
			
SyntaxError: invalid syntax
>>> print ("We have " + Meal + ", but not that topping.")
			
We have Waffles, but not that topping.
>>> elif (Mainchoice == 4):
			
SyntaxError: invalid syntax
>>> print("You chose oatmeal.")
			
You chose oatmeal.
>>> else:
			
SyntaxError: invalid syntax
>>> print('We don't serve that breakfast item!")
	  
SyntaxError: invalid syntax
>>> Letter 1 is H
	  
SyntaxError: invalid syntax
>>> LetterNum = 1
	  
>>> for Letter in "Howdy!":
	  for Letter in "Howdy!":
	  print("Letter ", LetterNum, " is ", Letter)
	  
SyntaxError: expected an indented block
>>> LetterNum+=1
	  
>>> value = input("Type less than 6 characters: ")
	  
Type less than 6 characters: 
>>> for Letter in value:
	  print("Letter ", LetterNum, " is ", Letter)
	  LetterNum+=1
	  if LetterNum > 6:
	  print("The string is too long!")
	  
SyntaxError: expected an indented block
>>> break
	  
SyntaxError: 'break' outside loop
>>> LetterNum = 1
	  
>>> for Letter in "Howdy!":
	  if Letter == "w":
	  continue
	  
SyntaxError: expected an indented block
>>> print("Encountered w, not processed.")
	  
Encountered w, not processed.
>>> print("Letter ", LetterNum, " is ", Letter)
	  
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print("Letter ", LetterNum, " is ", Letter)
NameError: name 'Letter' is not defined
>>> LetterNum+=1
	  
>>> LetterNum = 1
	  
>>> for Letter in "Howdy!":
	  if Letter == "w":
	  pass
	  
SyntaxError: expected an indented block
>>> print("Encountered w, not processed.")
	  
Encountered w, not processed.
>>> print("Letter ", LetterNum, " is ", Letter)
	  
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print("Letter ", LetterNum, " is ", Letter)
NameError: name 'Letter' is not defined
>>> LetterNum+=1
	  
>>> Value = input("Type less than 6 characters: ")
	  
Type less than 6 characters: 
>>> LetterNum = 1
	  
>>> for Letter in value:
	  print('Letter ", LetterNum, " is ", Letter)
		
SyntaxError: EOL while scanning string literal
>>> LetterNum+=1
		
>>> else:
		
SyntaxError: invalid syntax
>>> print("The string is blank.")
		
The string is blank.
>>> X = 1
		
>>> Y = 1
		
>>> print ('{:>4}'.format(' '), end= ' ')
		
     
>>> for X in range(1, 11):
		print('{:>4}'.format(X), end=' ')
		print()

		
   1 
   2 
   3 
   4 
   5 
   6 
   7 
   8 
   9 
  10 
>>> for X in range(1,11):
		print('{:.4}'.format(X), end=' ')
		while Y <= 10:
		print('{:>4}'.format(X * Y), end=' ')
		
SyntaxError: expected an indented block
>>> Y+=1
		
>>> print()
		

>>> Y=1
		
>>> try:
		Value = int(input("Type a number between 1 and 10:
				  
SyntaxError: EOL while scanning string literal
>>> Value = int(input("Type a number between 1 and 10:"))
				  
Type a number between 1 and 10:3
>>> except ValueError:
				  
SyntaxError: invalid syntax
>>> print("You must type a number between 1 and 10!")
				  
You must type a number between 1 and 10!
>>> else:
				  
SyntaxError: invalid syntax
>>> if (Value > 0) and (Value <= 10):
				  print("You typed: ", Value)
				  else:
				  
SyntaxError: invalid syntax
>>> print("The value you typed is incorrect!")
				  
The value you typed is incorrect!
>>> try:
	Value = int(input("Type a number between 1 and 10:
			  
SyntaxError: EOL while scanning string literal
>>> Value = int(input("Type a number between 1 and 10: "))
			  
Type a number between 1 and 10: 4
>>> except:
			  
SyntaxError: invalid syntax
>>> print("You must type a number between 1 and 10!")
			  
You must type a number between 1 and 10!
>>> else:
			  
SyntaxError: invalid syntax
>>> if (Value > 0) and (Value <= 10):
			  print("You typed: ", Value)
			  else:
			  
SyntaxError: invalid syntax
>>> print('The value you typed is incorrect!")
	  
SyntaxError: EOL while scanning string literal
>>> import sys
	  
>>> try:
	  File = open('myfile.txt')
	  except IOError as e:
	  
SyntaxError: invalid syntax
>>> print('Error opening file!\r\n" +
	  
SyntaxError: EOL while scanning string literal
>>> 'Error Number: {0}\r\n".format(e.errno) +
	  
SyntaxError: EOL while scanning string literal
>>> "Error Number: [0]\r\n".format(e.errno) +
	  
SyntaxError: invalid syntax
>>> "Error Text: {0}".format(e.strerror))
	  
SyntaxError: invalid syntax
>>> else:
	  
SyntaxError: invalid syntax
>>> print("File opened as expected.")
	  
File opened as expected.
>>> File.close();
	  
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    File.close();
NameError: name 'File' is not defined
>>> import sys
	  
>>> try:
	  File = open('myfile.txt')
	  except IOError as e:
	  
SyntaxError: invalid syntax
>>> for Arg in e.args:
	  print(Arg)

	  
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    for Arg in e.args:
NameError: name 'e' is not defined
>>> else:
	  
SyntaxError: invalid syntax
>>> print("File opened as expected.")
	  
File opened as expected.
>>> File.close();
	  
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    File.close();
NameError: name 'File' is not defined
'
>>> except IOError as e:
	  
SyntaxError: invalid syntax
>>> for Entry in dir(e):
	  if (not Entry.startswith("_")):
	  try:
	  
SyntaxError: expected an indented block
>>> print(Entry, " = ", e._getattribute_(Entry))
	  
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    print(Entry, " = ", e._getattribute_(Entry))
NameError: name 'Entry' is not defined
>>> except Attribute ", Entry, " not accessible.")
	  
SyntaxError: invalid syntax
>>> else:
	  
SyntaxError: invalid syntax
>>> print("File opened as expected.")
	  
File opened as expected.
>>> File.close();
	  
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    File.close();
NameError: name 'File' is not defined
>>> try:
	  Value = int(input("Type a number between 1 and 10:"))
	  except (ValueError, KeyboardInterrupt):
	  
SyntaxError: invalid syntax
>>> print("You must type a number between 1 and 10!")
	  
You must type a number between 1 and 10!
>>> else:
	  
SyntaxError: invalid syntax
>>> if (Value > 0) and (Value <= 10):
	  print("You typed: ", Value)
	  else:
	  
SyntaxError: invalid syntax
>>> print("The value you typed is incorrect!")
	  
The value you typed is incorrect!
>>> try:
	Value = int(input("Type a number between 1 and 10:"))
	  except ValueError:
	  
SyntaxError: unexpected indent
>>> print("You must type a number batween 1 and 10!")
	  
You must type a number batween 1 and 10!
>>> except KeyboardInterrupt:
	  
SyntaxError: invalid syntax
>>> print('You pressed Ctrl+C!")
	  
SyntaxError: EOL while scanning string literal
>>> else:
	  
SyntaxError: invalid syntax
>>> if (Value> 0) and (Value <= 10):
	  print('You typed: ", Value)
		
SyntaxError: EOL while scanning string literal
>>> else:
		
SyntaxError: invalid syntax
>>> print("The value you typed is incorrect!")
		
The value you typed is incorrect!
>>> try:
		Value = int(input('Type the first number: "))
				  
SyntaxError: EOL while scanning string literal
>>> Value1 = int(input("Type the first number: "))
				  
Type the first number: 1
>>> Value2 = int(input("Type he second number: "))
				  
Type he second number: 3
>>> Output = Value1 / Value2
				  
>>> except ValueError:
				  
SyntaxError: invalid syntax
>>> print("You must type a whole number!")
				  
You must type a whole number!
>>> except KeyboardInterrupt:
				  
SyntaxError: invalid syntax
>>> print("You pressed Ctrl+C!")
				  
You pressed Ctrl+C!
>>> except ArithmeticError:
				  
SyntaxError: invalid syntax
>>> print("An undefined math error occured.")
				  
An undefined math error occured.
>>> except ZeroDivisionError:
				  
SyntaxError: invalid syntax
>>> print('Attempted to divide by zero!")
	  
SyntaxError: EOL while scanning string literal
>>> else:
	  
SyntaxError: invalid syntax
>>> print(Output)
	  
0.3333333333333333
>>> except ZeroDivisionError:
	  
SyntaxError: invalid syntax
>>> print("Attempted to divide by zero!")
	  
Attempted to divide by zero!
>>> except ArithmeticError:
	  
SyntaxError: invalid syntax
>>> print("An undefined math error occured.")
	  
An undefined math error occured.
>>> TryAgain = True
	  
>>> while TryAgain:
	  try:
	  Value = int(input("Type a whole number. "))
	  
SyntaxError: expected an indented block
>>> except ValueError:
	  
SyntaxError: invalid syntax
>>> print("You must type a whole number!")
	  
You must type a whole number!
>>> try:
	  DoOver = input("Try again (y/n)? ")
	  try:
	  except:
	  
SyntaxError: expected an indented block
>>> print("OK, see you next time!")
	  
OK, see you next time!
>>> TryAgain = False
	  
>>> else:
	  
SyntaxError: invalid syntax
>>> if 9str.upper(DoOver) == "N":
	  
SyntaxError: invalid syntax
>>> TryAgain = False
	  
>>> except KeyboardInterrupt:
	  
SyntaxError: invalid syntax
>>> print("You pressed Ctrl+C!")
	  
You pressed Ctrl+C!
>>> print("See you next time!")
	  
See you next time!
>>> TryAgain = False
	  
>>> else:
	  
SyntaxError: invalid syntax
>>> print(Value)
	  
4
>>> TryAgain = False
	  
>>> try:
	  raise ValueError
	  except ValueError:
	  
SyntaxError: invalid syntax
>>> print("ValueError Exception!")
	  
ValueError Exception!
>>> try:
	  Ex = 'Value must be within 1 and 10.'
	  raise Ex
	  except ValueError as e:
	  
SyntaxError: invalid syntax
>>> print("ValueError Exception!", e.strerror)
	  
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    print("ValueError Exception!", e.strerror)
NameError: name 'e' is not defined
>>> try:
	  raise ValueError
	  except ValueError:
	  
SyntaxError: invalid syntax
>>> class CustomValueError(ValueError):
	  def_init_(self, arg):
	  
SyntaxError: invalid syntax
>>> self.strerror = arg
	  
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    self.strerror = arg
NameError: name 'arg' is not defined
>>> self.args = {arg}
	  
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    self.args = {arg}
NameError: name 'arg' is not defined
>>> try:
	  raise CustomValueError("Value must be within 1 and 10.")
	  except CustomValueError("Value must be within 1 and 10.")
	  
SyntaxError: invalid syntax
>>> except CustomValueError as e:
	  
SyntaxError: invalid syntax
>>> print("CustomValueError Exception!", e.strerror)
	  
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    print("CustomValueError Exception!", e.strerror)
NameError: name 'e' is not defined
>>> 

>>> x + y
	  
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    x + y
NameError: name 'x' is not defined
>>> x = -35
	  
>>> x = abs(x)
	  
>>> print(x)
	  
35
>>> x = 6
	  
>>> y = 4
	  
>>> print( cmp(x,y) )
	  
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    print( cmp(x,y) )
NameError: name 'cmp' is not defined
>>> print(cmp(x,y)
import math x = 6
	  
SyntaxError: invalid syntax
>>> import math
	  
>>> x = 6
	  
>>> print(math.exp(x))
	  
403.4287934927351
>>> import math
	  
>>> x = 6
	  
>>> print(math.log(x))
	  
1.791759469228055
>>> import math
	  
>>> x = 6
	  
>>> print(math.log10(x))
	  
0.7781512503836436
>>> import math
	  
>>> x = 6
	  
>>> print(math.pow(x,2))
	  
36.0
>>> import math
	  
>>> x = 6
	  
>>> print(math.sqrt(x))
	  
2.449489742783178
>>> print(1 + 5)
	  
6
>>> a = 88
	  
>>> b = 103
	  
>>> print(a = b)
	  
Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    print(a = b)
TypeError: 'a' is an invalid keyword argument for print()
>>> print(a + b)
	  
191
>>> c = -36
	  
>>> d = 25
	  
>>> print(c + d)
	  
-11
>>> e = 5.5
	  
>>> f = 2.5
	  
>>> print(e + f)
	  
8.0
>>> g = 75.67
	  
>>> h = 32
	  
>>> print(g - h)
	  
43.67
>>> i = 3.3
	  
>>> print(+i)
	  
3.3
>>> j = -19
	  
>>> print(+j)
	  
-19
>>> i = 3.3
	  
>>> print(-i)
	  
-3.3
>>> j = -19
	  
>>> print(-j)
	  
19
>>> k = 100.1
	  
>>> 1 = 10.1
	  
SyntaxError: can't assign to literal
>>> i = 10.1
	  
>>> print(k * l)
	  
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    print(k * l)
NameError: name 'l' is not defined
>>> print(k * 1)
	  
100.1
>>> k = 100.1
	  
>>> l = 10.1
	  
>>> print(k * l)
	  
1011.0099999999999
>>> m = 80
	  
>>> n = 5
	  
>>> print(m / n)
	  
16.0
>>> o = 85
	  
>>> p = 15
	  
>>> print(o % p)
	  
10
>>> q = 36.0
	  
>>> r = 6.0
	  
>>> print(o % p)
	  
10
>>> s = 52.25
	  
>>> t = 7
	  
>>> print(s ** t)
	  
1063173305051.292
>>> u = 10 + 10 * 5
	  
>>> u = (10 + 10) * 5
	  
>>> print(u)
	  
100
>>> w = 5
	  
>>> w += 1
	  
>>> print(w)
	  
6
>>> for x in range (0, 7):
	  x *= 2
	  print(x)

	  
0
2
4
6
8
10
12
>>> y += 1
	  
>>> y -= 1
	  
>>> y *= 2
	  
>>> y /= 3
	  
>>> y // = 5
	  
SyntaxError: invalid syntax
>>> y //=5
	  
>>> y **= 2
	  
>>> y %= 3
	  
>>> 
