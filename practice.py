Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> michele_age = 22
>>> truth_value = michele_age > 17
>>> if (truth_value):
	print("Michele can see a rated R movie")

	
Michele can see a rated R movie
>>> while True:
	age = input("How old are you? ")
	if age >= 17:
		print("Can see a rated R movie")
		else age < 17 and age > 12:
			
SyntaxError: invalid syntax
>>> print("Can see a Rated PG-13 movie")
Can see a Rated PG-13 movie
>>> else:
	
SyntaxError: invalid syntax
>>> print("Can only see rated PG movies")
Can only see rated PG movies
>>> age = 21
>>> if age == 21:
	print("You are 21!")
	print("You're old.")
	else:
		
SyntaxError: invalid syntax
>>> print("Young one!")
Young one!
>>> password = "unsafepassword"
>>> if password == "unsafepassword":
	print("You may enter.")
	else:
		
SyntaxError: invalid syntax
>>> print("Try again!")
Try again!
>>> password = "unsafepassword"
>>> if password == "unsafepassword":
	print("You may enter.")
	else:
		
SyntaxError: invalid syntax
>>> print("Try again!")
Try again!
>>> real_password = "unsafepassword"
>>> user_password = input("Enter the password: ")
Enter the password: 
>>> while user_password != real_password:
	user_password = input("Enter the password: ")
	print("You may enter!")

	
Enter the password: 
You may enter!
Enter the password: yes
You may enter!
Enter the password: hell yeah
You may enter!
Enter the password: \n
You may enter!
Enter the password: 
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    user_password = input("Enter the password: ")
EOFError: EOF when reading a line
>>> with open('file_to_save.txt', 'w') as open_file:
	open_file.write('A string to write')

	
17
>>> open_file = open('file_tosave.txt' , 'w')
>>> open_file.write('A string to write')
17
>>> open_file.close()
>>> 
>>> with open('file_to_read.txt' , 'r') as open_file:
	line = open_file.readline()
	while line:
		print(line)
		line = open_file.readline()

		
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    with open('file_to_read.txt' , 'r') as open_file:
FileNotFoundError: [Errno 2] No such file or directory: 'file_to_read.txt'
>>> student_scores = {'Adama': 100, 'starbuck': 75, 'Apollo': 80, 'Athena': 85, 'Agathon': 90}
>>> 
>>> adama_score = student_scores['Adama']
>>> adama_score = student_scores['Adama']
>>> adama_score += 100 % adama_score is now 200. This dosn't schange the dictionary value student_scores['Adama'] = adama_score % the score in the dictionary is now updated
SyntaxError: invalid syntax
>>> all_scores = student_scores.keys()
>>> all_names = student_scores.values()
>>> for pair in student_scores.items():
	print(pair)

	
('Adama', 100)
('starbuck', 75)
('Apollo', 80)
('Athena', 85)
('Agathon', 90)
>>> game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]
>>> winner_is_2 = [[2, 2, 0],
		   [2, 1, 0],
		   [2, 1, 1]]
>>> winner_is_1 = [[1, 2, 0],
		   [2, 1, 0],
		   [2, 1, 1]]
>>> winner_is_also_1 = [[0, 1, 0],
			[2, 1, 1]]
>>> no_winner = [[1, 2, 0],
		 [2, 1, 0],
		 [2, 1, 2]]
>>> also_no_winner = [[1, 2, 0],
		      [2, 1, 0],
		      [2, 1, 0]]
>>> my_list = [5, 10, 15]
>>> print(my_list[0])
5
>>> print(my_list[-1])
15
>>> print(len(my_list))
3
>>> print(matrix[0])
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(matrix[0])
NameError: name 'matrix' is not defined
>>> print(matrix[0]) [1, 2]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print(matrix[0]) [1, 2]
NameError: name 'matrix' is not defined
>>> print(matrix[-1])
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(matrix[-1])
NameError: name 'matrix' is not defined
>>> game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]
>>> game = [[0, 0,x],
	    [0, 0, 0],
	    [0, 0, 0]]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    game = [[0, 0,x],
NameError: name 'x' is not defined
>>> 
