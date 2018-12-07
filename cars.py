Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist = ["apple", "banana", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist = ["apple","banana", "cherry"]
>>> print(thislist[1])
banana
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist[1] = "blackcurrant"
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> thislist = ["apple", "banana", "cherry"]
>>> for x in thislist:
	print(x)

	
apple
banana
cherry
>>> thislist = ["apple", "banana", "cherry"]
>>> if "apple" in thislist:
	print("yes, 'apple' is in the fruits list")

	
yes, 'apple' is in the fruits list
>>> thislist = ["apple", "banana", "cherry"]
>>> print(len(thislist))
3
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.append("orange")
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.insert(1, "orange")
>>> print(thislist)
['apple', 'orange', 'banana', 'cherry']
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.remove("banana")
>>> print(thislist)
['apple', 'cherry']
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.pop()
'cherry'
>>> print(thislist)
['apple', 'banana']
>>> thislist = ["apple", "banana", "cherry"]
>>> del thislist{0}
SyntaxError: invalid syntax
>>> del thislist[0]
>>> print(thislist)
['banana', 'cherry']
>>> thislist = ["apple", "banana", "cherry"]
>>> del thislist
>>> print(thislist)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(thislist)
NameError: name 'thislist' is not defined
>>> thislist = ["apple", "banana", "cherry"]
>>> thislist.clear()
>>> print(thislist)
[]
>>> thislist = list(("apple", "banana", "cherry"))
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> fruits = ["apple", "banana", "cherry"]
>>> print("banana")
banana
>>> fruits = ["apple", "banana", "cherry"]
>>> print(fruits[1])
banana
>>> thistuple = ("apple", "banana", "cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thistuple = ("apple", "banana", "cherry")
>>> print(thistuple[1])
banana
>>> thistuple = ("apple", "banana", "cherry")
>>> thistuple[1] = "blackcurrant"
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    thistuple[1] = "blackcurrant"
TypeError: 'tuple' object does not support item assignment
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thistuple = ("apple", "bannana", "cherry")
>>> for x in thistuple:
	print(x)

	
apple
bannana
cherry
>>> thistuple = ("apple", "banana", "cherry")
>>> if "apple" in thistuple:
	print("yes, 'apple' is in the fruits tuple")

	
yes, 'apple' is in the fruits tuple
>>> thistuple = ("apple", "banana", "cherry")
>>> print(len(thistuple))
3
>>> thistuple = ("apple", "banana", "cherry")
>>> thistuple[3] = "orange"
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    thistuple[3] = "orange"
TypeError: 'tuple' object does not support item assignment
>>> thistuple[3] = "orange"
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    thistuple[3] = "orange"
TypeError: 'tuple' object does not support item assignment
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thistuple = ("apple", "banana", "cherry")
>>> del thistuple
>>> print(thistuple)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(thistuple)
NameError: name 'thistuple' is not defined
>>> thistuple = tuple(("apple", "banana", "cherry"))
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thisset = {"apple", "banana", "cherry"}
>>> print(thisset)
{'cherry', 'apple', 'banana'}
>>> thisset = {"apple", "banana", "cherry"}
>>> for x in thisset:
	print(x)

	
cherry
apple
banana
>>> thisset = {"apple", "banana","cherry"}
>>> print("banana" in thisset)
True
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.add("orange")
>>> print(thisset)
{'cherry', 'orange', 'apple', 'banana'}
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.update(["orange", "mango", "grapes"])
>>> print(thisset)
{'grapes', 'banana', 'orange', 'apple', 'cherry', 'mango'}
>>> thisset = {"apple", "banana", "cherry"}
>>> print(len(thisset))
3
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.remove("banana")
>>> print(thisset)
{'cherry', 'apple'}
>>> thisset = {"apple", "banana", "cherry"}
>>> x = thisset.pop()
>>> print(x)
cherry
>>> print(thisset)
{'apple', 'banana'}
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.clear()
>>> print(thisset)
set()
>>> thisset = {"apple", "banana", "cherry"}
>>> del thisset
>>> print(thisset)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print(thisset)
NameError: name 'thisset' is not defined
>>> thisset = set(("apple", "banana", "cherry"))
>>> print(thisset)
{'cherry', 'apple', 'banana'}
>>> fruits = {"apple", "banana", "cherry"}
>>> if ("apple" in fruits):
	print("yes, apple is a fruit!")

	
yes, apple is a fruit!
>>> thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
	}
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> x = thisdict["model"]
>>> x = thisdict.get('model")
		     
SyntaxError: EOL while scanning string literal
>>> thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
	}
		     
>>> thisdict["year"] = 2018
		     
>>> "brand": "Ford",
		     
SyntaxError: invalid syntax
>>> "model": "Mustang",
		     
SyntaxError: invalid syntax
>>> "year": 1964
		     
SyntaxError: illegal target for annotation
>>> }
SyntaxError: invalid syntax
>>> thisdict["year"] = 2018
>>> for x in thisdict:
	print(x)

	
brand
model
year
>>> for x in thisdict:
	print(thisdict[x])

	
Ford
Mustang
2018
>>> for x thisdict.value():
	
SyntaxError: invalid syntax
>>> print(x)
year
>>> for x, y in thisdict.items():
	print(x, y)

	
brand Ford
model Mustang
year 2018
>>> thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
	}
>>> if "model" in thisdict:
	print("Yes, 'model' is one of the keys in the thisdict dictionary")

	
Yes, 'model' is one of the keys in the thisdict dictionary
>>> print(len(thisdict))
3
>>> thisdict = {
	"brand": 'Ford"
	
SyntaxError: EOL while scanning string literal
>>> "model": "Mustang",
	
SyntaxError: invalid syntax
>>> "year": 1964
	
SyntaxError: illegal target for annotation
>>> }
SyntaxError: invalid syntax
>>> thisdict["color"] = "red"
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
>>> thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
	}
>>> thisdict.pop("model")
'Mustang'
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964}
>>> thisdict = {
	"brand": :Ford",
	
SyntaxError: invalid syntax
>>> "model": "Mustang",
	
SyntaxError: invalid syntax
>>> "year": 1964
	
SyntaxError: illegal target for annotation
>>> }
SyntaxError: invalid syntax
>>> del thisdict["model"]
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    del thisdict["model"]
KeyError: 'model'
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964}
>>> thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
	}
>>> del thisdict
>>> print(thisdict)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    print(thisdict)
NameError: name 'thisdict' is not defined
>>> thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
	}
>>> thisdict.clear()
>>> print(thisdict)
{}
>>> thisdict = dict(brand="Ford", model="Mustang", year=1964)
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> car = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
	}
>>> print(car.get("model"))
Mustang
>>> 
