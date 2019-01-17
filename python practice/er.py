Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> names = "a", "b", "c"]
SyntaxError: invalid syntax
>>> names = ["a", "b", "c"]
>>> values = [1, 2, 3]
>>> for name, value in zip(names, values):
	print("name, value")

	
name, value
name, value
name, value
>>> sum([1, 2, 3])
6
>>> sum(["hello", "world"])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sum(["hello", "world"])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum(["aa", "bb", "cc"])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    sum(["aa", "bb", "cc"])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> product([1, 2, 3])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    product([1, 2, 3])
NameError: name 'product' is not defined
>>> factorial(4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    factorial(4)
NameError: name 'factorial' is not defined
>>> reverse([1, 2, 3, 4])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    reverse([1, 2, 3, 4])
NameError: name 'reverse' is not defined
>>> reverse(reverse([1, 2, 3, 4]))
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    reverse(reverse([1, 2, 3, 4]))
NameError: name 'reverse' is not defined
>>> cumulative_sum([1, 2, 3, 4])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    cumulative_sum([1, 2, 3, 4])
NameError: name 'cumulative_sum' is not defined
>>> dups([1, 2, 1, 3, 2, 5])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dups([1, 2, 1, 3, 2, 5])
NameError: name 'dups' is not defined
>>> a = [2, 10, 4, 3, 7]
>>> a.sort()
>>> a
[2, 3, 4, 7, 10]
>>> a = [4, 3, 5, 9, 2]
>>> sorted(a)
[2, 3, 4, 5, 9]
>>> a
[4, 3, 5, 9, 2]
>>> a = ["hello", 1, "world", 45, 2]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> a = [[2, 3], [1, 6]]
>>> a.sort()
>>> a
[[1, 6], [2, 3]]
>>> a = [[2, 3], [4, 6], [6, 1]]
>>> a.sort(key=lambda x: x[1])
>>> a
[[6, 1], [2, 3], [4, 6]]
>>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']) ['c', 'perl', 'java', 'ruby', 'python', 'haskell']
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']) ['c', 'perl', 'java', 'ruby', 'python', 'haskell']
NameError: name 'lensort' is not defined
>>> 
