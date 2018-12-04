Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Welcome to Hangman!
SyntaxError: invalid syntax
>>> Guess your letter: S
SyntaxError: invalid syntax
>>> Incorrect!
SyntaxError: invalid syntax
>>> Guess your letter: E
SyntaxError: invalid syntax
>>> my_list = [1, 1, 2, 2, 3, 3, 5, 5, 8]
>>> print(my_list)
[1, 1, 2, 2, 3, 3, 5, 5, 8]
>>> my_set = {1, 1, 2, 2, 3, 3, 5, 5, 8}
>>> print(my_set)
{1, 2, 3, 5, 8}
>>> my_set = set()
>>> my_set.add(5)
>>> print(my_set)
{5}
>>> my_set.add("Michele")
>>> print(my_set)
{5, 'Michele'}
>>> {5, "Michele"}
{5, 'Michele'}
>>> print(my_set)
{5, 'Michele'}
>>> my_set = [1, 2, 3, 5}
SyntaxError: invalid syntax
>>> my_set = {1, 2, 3, 5}
>>> 1 in my_set
True
>>> 4 in my_set
False
>>> price_dictionary = {
	"banana": 1.50,
	"avocado": 0.99
	"heirloom tomata": 0.89,
	
SyntaxError: invalid syntax
>>> "cherry tomato pack": 3.00
	
SyntaxError: illegal target for annotation
>>> }
SyntaxError: invalid syntax
>>> price_dictionary = {
	"banana": 1.50, "avocado": 0.99, "heirloom tomato": 0.89, "cherry tomato pack": 3.00}
>>> print(price_dictionary["banana"])
1.5
>>> print(price_dictionary.keys())
dict_keys(['banana', 'avocado', 'heirloom tomato', 'cherry tomato pack'])
>>> ["banana", "avocado", "heirloom tomato", "cherry tomato pack"]
['banana', 'avocado', 'heirloom tomato', 'cherry tomato pack']
>>> price_dictionary["granny smith apple"] = 0.49
>>> price_dictionary["red delicious apple"] = 0.35
>>> print(price_dictionary["granny smith apple"])
0.49
>>> price_dictionary["dog food"] = "only at Petco"
>>> print(price_dictionary["dog food"])
only at Petco
>>> print(price_dictionary["dog food"])
only at Petco
>>> price_dictionary["dog food"] = 10.99
>>> print(price_dictionary["dog food"])
10.99
>>> price_dictionary["lemon"]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    price_dictionary["lemon"]
KeyError: 'lemon'
>>> print(price_dictionary.get("banana", "no food like this"))
1.5
>>> print(price_dictionary.get("lemon", "no food like this"))
no food like this
>>> price_dictionary[[1, 2, 3]] = "new food"
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    price_dictionary[[1, 2, 3]] = "new food"
TypeError: unhashable type: 'list'
>>> price_dictionary["lettuce"] = [1.50, 3.50]
>>> print(price_dictionary["lettuce"])
[1.5, 3.5]
>>> "lemon" in price_dictionary
False
>>> "banana" in price_dictionary
True
>>> a = 1
>>> b = 10
>>> print("my number is " + str(a) + " and his number is " + str(b))
my number is 1 and his number is 10
>>> a = 1
>>> b = 10
>>> print("my number is {} and his number is {}".format(a, b))
my number is 1 and his number is 10
>>> {
	"name": "Michele",
	"shirt_color": "blue",
	"laptops": [
		{
			"brand": "Lenovo",
			"operating_system": "Ubuntu"
			}
		{
			
SyntaxError: invalid syntax
>>> },
		
SyntaxError: invalid syntax
>>> {
	"brand":"Apple"
	"operating_system": "OSX"
	
SyntaxError: invalid syntax
>>> }
		
SyntaxError: invalid syntax
>>> ]
	
SyntaxError: invalid syntax
>>> "has_a_dog": false,
	
SyntaxError: invalid syntax
>>> "items_on_desk": ["mug",  "pen", "monitor"]
	
SyntaxError: illegal target for annotation
>>> }
SyntaxError: invalid syntax
>>> import json
>>> info_about_me = {
	"name": "Michele",
	"has_a_dog": False
	}
>>> with open("info.json", "w") as f:
	json.dump(info_about_me, f)
	{
		"name": "Michele",
		"has_a_dog": false
		}

	
Traceback (most recent call last):
  File "<pyshell#81>", line 5, in <module>
    "has_a_dog": false
NameError: name 'false' is not defined
>>> import json
>>> with open("info.json", "r") as f:
	info = json.load(f)

	
>>> if info["has_a-dog"]:
	print("{} has a dog".format(info["name"]))
	else:
		
SyntaxError: invalid syntax
>>> print("{} does not have a dog".format(info["name"]))
Michele does not have a dog
>>> 
