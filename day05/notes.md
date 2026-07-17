## Concepts

### Lecture 5 - Unit Test
Assert
Debugging tool that test if a specific condition is true.

pytest (library)
automate simple unit tests to complex functional and integration tests.

### Lecture 6 - File I/O
File I/O
Way of storing data to, or reading data from, an external file.

open
A function that opens a file and returns it as file object

with
Automatically open and close file.

sorted
A function that will sort any iterable ascendingly or descendingly.

split
A string method that can split string into multiple pieces of strings based on targeted character.

lambda
A function that is small, and don't need to be define by a name.

csv (library)
Library used to read and write data in csv format.

PIL (library)
Python Imaging Library that is for opening, manipulating, and saving different images file formats.
---
 


## Built
- Url Sanitizer

## Mistakes

## Note
- It's always better to separate big tests into smaller tests to get more clues if something goes wrong.
- A separate test file is better if there are tons of tests.
- https://docs.pytest.org/en/stable/
- "w" to open up a file is dangerous, because it overwrites the old content of a file. Use Appending.
- Programmers use csv instead of txt to store data in a file
- https://pillow.readthedocs.io/en/stable/

## Question
- I still don't get pytest.raises actually do?
    Answer: Pytest created a shortcut so developer don't need to type try and except all the time for a singular test

- If the code is ready to be launch should the assert be changed?
    Answer: only use assert in your test files to verify the behaviour of code during development.

- Question for raises and other types of error handling methods, do I need to know what error it will produce so I can handle it properly. How do I know the name of the error (Ex: ValueError, AssertionError, etc..)?
    Answer: Yes, I need to know which specific error will be produced. To know the exact error and name is by testing the code, like triggering it on purpose, or read docs.

## Video Link
https://www.youtube.com/watch?v=tIrcxwLqzjQ&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=7

## Reflection
Today I learn why testing is important, it correlates with proper error handeling
File handling is really mindblowing there are lots of functions that helps to make code looks cleaner and more practical