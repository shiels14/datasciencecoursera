Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> anagrams (['eat', 'ate', 'done', 'tea', 'soup', 'node'])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    anagrams (['eat', 'ate', 'done', 'tea', 'soup', 'node'])
NameError: name 'anagrams' is not defined
>>> [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
      
SyntaxError: invalid syntax
>>> valuesort ({'x': 1, 'y': 2, 'a': 3}) [3, 1, 2]
      
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    valuesort ({'x': 1, 'y': 2, 'a': 3}) [3, 1, 2]
NameError: name 'valuesort' is not defined
>>> globals()
      
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> x = 1
      
>>> globals()
      
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 1}
>>> x = 2
      
>>> globals()
      
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 2}
>>> globals()['x'] = 3
      
>>> 3
      
3
>>> def f(a, b): print locals()
      
SyntaxError: invalid syntax
>>> def f(a, b): print("locals"())

      
>>> f(1, 2)
      
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    f(1, 2)
  File "<pyshell#12>", line 1, in f
    def f(a, b): print("locals"())
TypeError: 'str' object is not callable
>>> {'a': 1, 'b': 2}
      
{'a': 1, 'b': 2}
>>> def f(name):
      return "Hello %(name)s!" % locals()

      
>>> f("Guido")
      
'Hello Guido!'
>>> import time
      
>>> print time.asctime()
      
SyntaxError: invalid syntax
>>> print time.asctime() 'Fri Mar 30 12:59:21 2012'
      
SyntaxError: invalid syntax
>>> def square(x):
      return x ^ x

      
>>> def cube(x):
      return x * x * x

      
>>> import num
      
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    import num
ModuleNotFoundError: No module named 'num'
>>> num.square(3)
      
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    num.square(3)
NameError: name 'num' is not defined
>>> 9
      
9
>>> num.cube(3)
      
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    num.cube(3)
NameError: name 'num' is not defined
>>> 27
      
27
>>> """The num module provides utilities to work on numbers.
Current it provides square and cube.
"""
      
'The num module provides utilities to work on numbers.\nCurrent it provides square and cube.\n'
>>> def square(x):
      """Computes square of a number."""
      return x * x
      def cube(x):
      """Computes cube of a number."""
      
SyntaxError: expected an indented block
>>> return x * x
      
SyntaxError: 'return' outside function
>>> import os
      
>>> print os.getcwd._doc_
      
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(os.getcwd._doc_)?
>>> getcwd() -> path
      
SyntaxError: invalid syntax
>>> 
