Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 0
while a < 5:
    a += 1 # Same as a = a + 1 
    print (a)
    
SyntaxError: multiple statements found while compiling a single statement
>>> a = 9
while a < 5:
    a += 9 # Same as a = a + 1 
    print (a)
    
SyntaxError: multiple statements found while compiling a single statement
>>> onetoten = range(1,11)
for count in onetoten:
    print (count)
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
================ RESTART: /Users/stephenshiels/Desktop/run.py ================
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
>>> 
================ RESTART: /Users/stephenshiels/Desktop/run.py ================
1
2
3
4
5
6
7
8
9
>>> 
================ RESTART: /Users/stephenshiels/Desktop/run.py ================
1
2
3
4
5
6
7
8
9
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
>>> 
