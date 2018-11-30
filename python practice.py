Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> try:
	raise ValueError
print('Raising an exception.")
      
SyntaxError: invalid syntax
>>> except ValueError:
      
SyntaxError: invalid syntax
>>> print('ValueError:
	  
SyntaxError: EOL while scanning string literal
>>> print('ValueError Exception!")
	  
SyntaxError: EOL while scanning string literal
>>> sys.exit()
	  
>>> finally:
	  
SyntaxError: invalid syntax
>>> print("Taking care of last minute details.")
	  
Taking care of last minute details.
>>> print("This code will never execute.")
	  
This code will never execute.
>>> ##raise ValueError
	  
>>> def SayHello(Name):
	  print('Hello ", Name)
		
SyntaxError: EOL while scanning string literal
>>> return
		
SyntaxError: 'return' outside function
>>> def SayGoodbye ", Name)
		
SyntaxError: EOL while scanning string literal
>>> return
		
SyntaxError: 'return' outside function
>>> print('Hello There (Single Quote)!')
		
Hello There (Single Quote)!
>>> print("Hello There 9Double Quote)!")
		
Hello There 9Double Quote)!
>>> print("""This is a multiple line string using double quotes. You can also use triple single quotes.""")
	  
This is a multiple line string using double quotes. You can also use triple single quotes.
>>> \
	  \\
	  
SyntaxError: unexpected character after line continuation character
>>> \'
	  
SyntaxError: unexpected character after line continuation character
>>> \"
	  
SyntaxError: unexpected character after line continuation character
>>> print("Part of this text\r\nis on the next line.")
	  
Part of this text
is on the next line.
>>> print("This is an A with a grave accent: \xC0.")
	  
This is an A with a grave accent: À.
>>> print("This is a drawing character: \u2562.")
	  
This is a drawing character: ╢.
>>> print('This is a pillcrow: \266.")
	  
SyntaxError: EOL while scanning string literal
>>> print("This is a pilcrow: \266.")
	  
This is a pilcrow: ¶.
>>> print("This is a division sign: \xF7.")
	  
This is a division sign: ÷.
>>> MyString = "Hello World"
	  
>>> print(MyString[0])
	  
H
>>> print(String1[0])
	  
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(String1[0])
NameError: name 'String1' is not defined
>>> print(String1[0])
	  
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(String1[0])
NameError: name 'String1' is not defined
>>> print(String2[0])
	  
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(String2[0])
NameError: name 'String2' is not defined
>>> print(String1[:5})
	  
SyntaxError: invalid syntax
>>> print(String1[6:])
	  
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(String1[6:])
NameError: name 'String1' is not defined
>>> String3 = String1[:6] + String2[:6]
	  
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    String3 = String1[:6] + String2[:6]
NameError: name 'String1' is not defined
>>> print9String3)
	  
SyntaxError: invalid syntax
>>> print(String2[:7]*5)
	  
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(String2[:7]*5)
NameError: name 'String2' is not defined
>>> MyString = " Hello World "
	  
>>> print(MyString.upper())
	  
 HELLO WORLD 
>>> print(MyString.strip())
	  
Hello World
>>> print(MyString.center(21, "*"))
	  
**** Hello World ****
>>> print(MyString.strip().center(21, "*"))
	  
*****Hello World*****
>>> print(MyString.isdigit())
	  
False
>>> print(max(MyString))
	  
r
>>> print(MyString.split())
	  
['Hello', 'World']
>>> print(MyString.split() [0])
	  
Hello
>>> SearchMe = "The apple is red and the berry is blue!"
	  
>>> print(SearchMe.find("is"))
	  
10
>>> print(SearchMe.rfind("is"))
	  
31
>>> print(SearchMe.count("is"))
	  
2
>>> print(SearchMe.startswith('The"))
			      
SyntaxError: EOL while scanning string literal
>>> print(SearchMe.startswith("The"))
			      
True
>>> print(SearchMe.endswith("The"))
			      
False
]
>>> print(SearchMe.replace("apple", "car").replace("berry", "truck"))
	  
The car is red and the truck is blue!
>>> Formatted = "{:d}"
	  
>>> print(Formatted.format(7000))
	  
7000
>>> Formatted = "{:,d}"
	  
>>> print(Formatted.format(7000))
	  
7,000
>>> Formatted = "{:^15,d}"
	  
>>> print(Formatted.format(7000))
	  
     7,000     
>>> Formatted = "{:*^15,d}"
	  
>>> print(Formatted.format(7000))
	  
*****7,000*****
>>> Formatted = "{:*^15.2f}"
	  
>>> print(Formatted.format(7000))
	  
****7000.00****
>>> Formatted = "{:*>15X}"
	  
>>> print(Formatted.format(7000))
	  
***********1B58
>>> Formatted = "{:*<#15x}"
	  
>>> print(Formatted.format(7000))
	  
0x1b58*********
>>> Formatted = "A {0} {1} and a {0} [2}."
	  
>>> print(Formatted.format("blue", "car", "truck"))
	  
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(Formatted.format("blue", "car", "truck"))
ValueError: Single '}' encountered in format string
>>> print(Formatted.format("blue", "car", "truck"))
	  
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print(Formatted.format("blue", "car", "truck"))
ValueError: Single '}' encountered in format string
>>> append()
	  
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    append()
NameError: name 'append' is not defined
>>> append():
	  
SyntaxError: invalid syntax
>>> Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
	  
>>> ColorSelect = " "
	  
>>> while str.upper(ColorSelect) != "Quit":
	  ColorSelect = input("Please type a color name: ")
	  if (Colors.count(ColorSelect) >= 1):
	  print("The color exists is the list!")
	  
SyntaxError: expected an indented block
>>> elif (str.upper(ColorSelect) != "QUIT"):
	  
SyntaxError: invalid syntax
>>> print("The list doesn't contain the color.")
	  
The list doesn't contain the color.
>>> 
