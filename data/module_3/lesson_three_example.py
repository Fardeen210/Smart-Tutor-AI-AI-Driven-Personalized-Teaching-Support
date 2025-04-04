# -*- coding: utf-8 -*-
"""Lesson_three_example.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oRMvrzwGp8ItGdT7XbD8Dv_Bvn9_LtXH

# 1. Python module and Python package

**Python Modules**
*   A module is a file containing Python definitions and statements.
*   A module can define functions, classes and variables.
*   A module can also include runnable code.
*   Grouping related code into a module makes the code easier to understand and use.

**Python Packages**



*   Packages are namespaces which contain multiple packages and modules themselves.
*   They are simply directories, but with a twist.
*   Each package in Python is a directory which MUST contain a special file called __init__.py.
*   This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.
*   Example: If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. We also must not forget to add the __init__.py file inside the foo directory.

**What is difference between a Python module and Python package?**


*   A module is a single file (or files) that are imported under one import and used. e.g.,
`import my_module`
*   A package is a collection of modules in directories that give a package hierarchy. e.g., `from my_package.timing.danger.internets import function_of_love`


Any Python file is a [module](https://docs.python.org/3/tutorial/modules.html), its name being the file's base name without the .py extension. A [package](https://docs.python.org/3/tutorial/modules.html#packages) is a collection of Python modules: while a module is a single Python file, a package is a directory of Python modules containing an additional __init__.py file, to distinguish a package from a directory that just happens to contain a bunch of Python scripts.

1.1 Python moduels:
https://www.w3schools.com/python/python_modules.asp


1.2 Python Packages

**(1) Find, install and publish Python packages with the Python Package Index**

[Python package index](https://pypi.org/)

**(2) How to install a python package?**

in command:


```
pip install nltk(package name)
```


in Colab:


```
!pip install nltk(package name)
```
"""

pip install bert

# Package pre-installed in colab
!pip freeze

"""(3) **The structure of Python packages ([from python documentation]**(https://docs.python.org/3/tutorial/modules.html#packages)):

Packages can contain nested subpackages to arbitrary depth. For example, let’s make one more modification to the example package directory as follows:

![alt text](https://files.realpython.com/media/pkg4.a830d6e144bf.png)


The four modules (mod1.py, mod2.py, mod3.py and mod4.py) are defined as previously. But now, instead of being lumped together into the pkg directory, they are split out into two subpackage directories, sub_pkg1 and sub_pkg2.

Importing still works the same as shown previously. Syntax is similar, but additional dot notation is used to separate package name from subpackage name:



```
import pkg.sub_pkg1.mod1

from pkg.sub_pkg1 import mod2

from pkg.sub_pkg2.mod3 import function_name

# Rename a function
from pkg.sub_pkg2.mod4 import qux as grault

```

**Remember, the usage of packages and modules are very similar!**

# 2. Python Advanced Recursion

Problems (in life and also in computer science) can often seem big and scary. But if we keep chipping away at them, more often than not we can break them down into smaller chunks trivial enough to solve. This is the essence of thinking recursively!

![alt text](https://files.realpython.com/media/santa_claus_2.ecbf2686f1a1.png)
"""

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)
deliver_presents_iteratively()

"""![alt text](https://files.realpython.com/media/elves_7.8d1af1cd85c8.png)

Assign titles and responsibilities to the elves based on the number of houses for which they are responsible:

*   \> 1 He is a manager and can appoint two elves and divide his work among them
*   = 1 He is a worker and has to deliver the presents to the house assigned to him

"""

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)
deliver_presents_recursively(houses)

"""n! = n x (n−1)!

n! = n x (n−1) x (n−2)!

n! = n x (n−1) x (n−2) x (n−3)!

⋅

⋅

n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3!

n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3 x 2!

n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3 x 2 x 1!

![alt text](https://files.realpython.com/media/stack.9c4ba62929cf.gif)
"""

def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

factorial_recursive(5)

"""![alt text](https://files.realpython.com/media/state_3.3e8a68c4fde5.png)


(1,0)

(2,1)

(3,3)

(4,6)

(5,10)

(6,15)

(7,21)

(8,28)

(9,36)

(10,45)

(11,55)


"""

def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)

sum_recursive(1, 0)

"""## **Recursive Data Structures in Python**

A data structure is recursive if it can be deﬁned in terms of a smaller version of itself.
"""

# Return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, input_list):
    return [element] + input_list

attach_head(1,                                                  # Will return [1, 46, -31, "hello"]
            attach_head(46,                                     # Will return [46, -31, "hello"]
                        attach_head(-31,                        # Will return [-31, "hello"]
                                    attach_head("hello", [])))) # Will return ["hello"]

"""

1.   Starting with an empty list, you can generate any list by recursively applying the attach_head function.
2.   Recursion can also be seen as self-referential function composition. We apply a function to an argument, then pass that result on as an argument to a second application of the same function, and so on. Repeatedly composing attach_head with itself is the same as attach_head calling itself repeatedly.

![alt text](https://files.realpython.com/media/list.3df62a89243d.gif)

"""

def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)

list_sum_recursive([1, 2, 3])

def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", " "\n")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

fibonacci_recursive(5)

"""# 3. Python File I/O

**3.1 Glossary**


**File:**

A named location on disk to store related information. It is used to permanently store data in a non-volatile memory (e.g. hard disk).


**Format operator:**

An operator, %, that takes a format string and a tuple and generates a string that includes the elements of the tuple formatted as specified by the format string.


**Format string:**

A string, used with the format operator, that contains format sequences.


**Format sequence:**

A sequence of characters in a format string, like %d, that specifies how a value should be formatted.


**Text file:**

A sequence of characters stored in permanent storage like a hard drive.


**Directory:**

A named collection of files, also called a folder.


**Path:**

A string that identifies a file.


**Relative path:**

A path that starts from the current directory.


**Absolute path:**

A path that starts from the topmost directory in the file system.


**Catch:**


To prevent an exception from terminating a program using the try and except statements.
database:


A file whose contents are organized like a dictionary with keys that correspond to values.

**Python File Modes**

>Mode | Description
>--- | ---
>'r'| Open a file for reading. (default)
>'w'| Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
>'x'|Open a file for exclusive creation. If the file already exists, the operation fails.
>'a'|Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
> 't'|Open in text mode. (default)
>'b'|Open in binary mode.
>'+'|Open a file for updating (reading and writing)

**3.2** **Reading and writing**

A text file is a sequence of characters stored on a permanent medium like a hard drive, flash memory, or CD-ROM.

**Examples in the second edition**:

To **write** a file, you have to open it with mode 'w' as a second parameter:
"""

fout = open('output.txt', 'w')
print(fout)

"""The write() method puts data into the file.

f.write(string) writes the contents of string to the file, returning the number of characters written.

"""

line1 = "This here's the wattle,\n"
fout.write(line1)

"""Again, the file object keeps track of where it is, so if you call write again, it adds the new data to the end."""

# Again, the file object keeps track of where it is, so if you call write again, it adds the new data to the end.

line2 = "the emblem of our lands.\n"
fout.write(line2)

"""When you are done writing, you have to close the file.

To **read** a file in Python, we must open the file in reading mode.
"""

f = open("output.txt",'r',encoding = 'utf-8')

# read the entire file

print(f.read())

f1 = open("output.txt",'r',encoding = 'utf-8')

# read the first 9 data
print(f1.read(9))

# We can read a file line-by-line using a for loop. This is both efficient and fast.

f2 = open("output.txt",'r',encoding = 'utf-8')

for line in f2:
  print(line, end = '')

# The readlines() method returns a list of remaining lines of the entire file
f3 = open("output.txt",'r',encoding = 'utf-8')

print(f3.readlines())

"""**Examples in the third edition: **"""

# Writing our first file

with open("test.txt", "w") as myfile:
  myfile.write("My first file written from Python\n")
  myfile.write("# I like Python\n")
  myfile.write("---------------------------------\n")
  myfile.write("Hello, world!\n")
  myfile.write("## Python is really interesting\n")
  myfile.write("---------------------------------\n")
  myfile.write("# Python is easy\n")

# Reading a file line-at-a-time

with open("test.txt", "r") as my_new_handle:
  for the_line in my_new_handle:
  # Do something with the line we just read.
  # Here we just print it.
    print(the_line, end="")

# If we try to open a file that doesn’t exist, we get an error:
mynewhandle = open("wharrah.txt", "r")

# Turning a file into a list of lines

with open("original_papers.txt", "r") as input_file:
   all_lines = input_file.readlines()
   print(all_lines)
all_lines.sort()
with open("sorted_papers.txt", "w") as output_file:
  for line in all_lines:
    output_file.write(line)
print(all_lines)

# Reading the whole file at once
with open("original_papers.txt") as f:
  content = f.read()
  words = content.split()
  print("There are {0} words in the file.".format(len(words)))

# An example

def filter(oldfile, newfile):
  with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
    for line in infile:
    # Put any processing logic here
      if not line.startswith('#'):
        outfile.write(line)

oldfile = "test.txt"
newfile = "update_text.txt"
filter(oldfile, newfile)

"""**3.3 Format operator**

(1) The argument of write has to be a string, so if we want to put other values in a file, we have to convert them to strings. The easiest way to do that is with str:
"""

x = 52
fout.write(str(x))

"""(2) An alternative is to use the **format operator**, %. When applied to integers, % is the modulus operator. But when the first operand is a string, % is the format operator.

The first operand is the **format string**, which contains one or more **format sequences**, which specify how the second operand is formatted. The result is a string.

For example, the format sequence '%d' means that the second operand should be formatted as an integer (d stands for “decimal”):
"""

camels = 42

print(type(camels))

new_camels = '%d' % camels

print(new_camels)

print(type(new_camels))

"""(3) A format sequence can appear anywhere in the string, so you can embed a value in a sentence:

"""

camels = 42
'I have spotted %d camels.' % camels

"""(4) If there is more than one format sequence in the string, the second argument has to be a tuple. Each format sequence is matched with an element of the tuple, in order.

The following example uses '%d' to format an integer, '%g' to format a floating-point number (don’t ask why), and '%s' to format a string:
"""

'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

"""(5) The number of elements in the tuple has to match the number of format sequences in the string. Also, the types of the elements have to match the format sequences:"""

'%d %d %d' % (1, 2)

'%d' % 'dollars'

"""In the first example, there aren’t enough elements; in the second, the element is the wrong type.

The format operator is powerful, but it can be difficult to use. You can read more about it at: https://docs.python.org/2/library/stdtypes.html#string-formatting

**3.4 Filenames and paths**

Files are organized into **directories** (also called “folders”). Every running program has a “current directory,” which is the default directory for most operations. For example, when you open a file for reading, Python looks for it in the current directory.

The os module provides functions for working with files and directories (“os” stands for “operating system”). os.getcwd returns the name of the current directory:
"""

import os
cwd = os.getcwd()
print (cwd)

"""A string like cwd that identifies a file is called a path. A relative path starts from the current directory; an absolute path starts from the topmost directory in the file system.

The paths we have seen so far are simple filenames, so they are relative to the current directory. To find the absolute path to a file, you can use os.path.abspath:
"""

os.path.abspath('output.txt')

os.path.abspath('mnist_train_small.csv')

"""os.path.exists checks whether a file or directory exists:"""

os.path.exists('output.txt')

"""If it exists, os.path.isdir checks whether it’s a directory:"""

os.path.isdir('output.txt')

os.path.isdir('sample_data')

"""Similarly, os.path.isfile checks whether it’s a file.

os.listdir returns a list of the files (and other directories) in the given directory:
"""

os.listdir(cwd)

"""To demonstrate these functions, the following example “walks” through a directory, prints the names of all the files, and calls itself recursively on all the directories.

**3.5 Catching exceptions**

A lot of things can go wrong when you try to read and write files. If you try to open a file that doesn’t exist, you get an IOError:
"""

fin = open('bad_file')

"""Aif you try to open a directory for reading, you get"""

fout = open('/content', 'w')

"""To avoid these errors, you could use functions like os.path.exists and os.path.isfile, but it would take a lot of time and code to check all the possibilities (if “Errno 21” is any indication, there are at least 21 things that can go wrong).

It is better to go ahead and try—and deal with problems if they happen—which is exactly what the try statement does. The syntax is similar to an if statement:
"""

try:
    fin = open('bad_file')
    for line in fin:
        print (line)
    fin.close()
except:
    print ('Something went wrong.')

"""Python starts by executing the try clause. If all goes well, it skips the except clause and proceeds. If an exception occurs, it jumps out of the try clause and executes the except clause.

Handling an exception with a try statement is called catching an exception. In this example, the except clause prints an error message that is not very helpful. In general, catching an exception gives you a chance to fix the problem, or try again, or at least end the program gracefully.

**3.6 What about fetching something from the web?**

The Python libraries are pretty messy in places. But here is a very simple example that copies the contents at some web URL to a local file.

The urlretrieve function — just one call — could be used to download any kind of content from the Internet.

We’ll need to get a few things right before this works:


*   The resource we’re trying to fetch must exist! Check this using a browser.
*   We’ll need permission to write to the destination filename, and the file will be created in the “current
directory” - i.e. the same folder that the Python program is saved in.
*   If we are behind a proxy server that requires authentication, (as some students are), this may require some
more special handling to work around our proxy. Use a local resource for the purpose of this demonstration!

Here is a slightly different example using the requests module. This module is not part of the standard library distributed with python, however it is easier to use and significantly more potent than the urllib module distributed with
python.
"""

import urllib.request
url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
destination_filename = "rfc793.txt"
urllib.request.urlretrieve(url, destination_filename)

import requests
url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
response = requests.get(url)
print(response.text)

"""Opening the remote URL returns the response from the server. That response contains several types of information, and the requests module allows us to access them in various ways. On line 5, we get the downloaded document as a single string. We could also read it line by line as follows:

"""

import requests
url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
response = requests.get(url)
for line in response:
  print(line)