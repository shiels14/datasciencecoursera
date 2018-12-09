Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mymodule as mx
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import mymodule as mx
ModuleNotFoundError: No module named 'mymodule'
>>> a = mx.person1["age"]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = mx.person1["age"]
NameError: name 'mx' is not defined
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> import platform
>>> x = platform.system()
>>> print(x)
Darwin
>>> import platform
>>> x = dir(platform)
>>> print(x)
['DEV_NULL', '_UNIXCONFDIR', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture', '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_parse_release_file', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_release_filename', '_release_version', '_supported_dists', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'warnings', 'win32_ver']
>>> def greeting(name):
	print("Hello, " + name")
	      
SyntaxError: EOL while scanning string literal
>>> print('Hello, " + name)
	  
SyntaxError: EOL while scanning string literal
>>> person1 = {
	"name": "John",
	"age": 36,
	"country": "Norway"
	}
	  
>>> from mymodule import personal
	  
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    from mymodule import personal
ModuleNotFoundError: No module named 'mymodule'
>>> print (person1["age"])
	  
36
>>> import datetime
	  
>>> x = datetime.datetime.now()
	  
>>> print(x)
	  
2018-12-09 16:12:35.313563
>>> import datetime
	  
>>> x = datetime.datetime.now()
	  
>>> print(x.year)
	  
2018
>>> print(x.strftime("%A"))
	  
Sunday
>>> import datetime
	  
>>> x = datetime.datetime(2020, 5, 17)
	  
>>> print(x)
	  
2020-05-17 00:00:00
>>> import datetime
	  
>>> x = datetime.datetime(2018,6 1)
	  
SyntaxError: invalid syntax
>>> x = datetime.datetime(2018, 6, 1)
	  
>>> print(x.strftime("%B"))
	  
June
>>> import json
	  
>>> import json
	  
>>> x = '{"name":"John", "age":30, "city":"New York"}'
	  
>>> y = json.loads(x)
	  
>>> print(y{"age"})
	  
SyntaxError: invalid syntax
>>> print(y["age"])
	  
30
>>> 
