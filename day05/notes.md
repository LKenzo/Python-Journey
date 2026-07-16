## Concepts

### Lecture 5 - Unit Test
Assert
Debugging tool that test if a specific condition is true.

pytest (library)
automate simple unit tests to complex functional and integration tests.

---
 


## Built
- Url Sanitizer

## Mistakes

## Note
- It's always better to seperate big tests into smaller tests to get more clues if something goes wrong.
- A seperate test file is better if there are tons of tests.
- https://docs.pytest.org/en/stable/


## Question
- I still don't get pytest.raises actually do?
    Answer: Pytest created a shortcute so developer don't need to type try and except all the time for a singular test

- If the code is ready to be launch should the assert be changed?
    Answer: only use assert in your test files to verify the behaviour of code during development.

- Question for raises and other types of error handling methods, do I need to know what error it will produce so I can handle it properly. How do I know the name of the error (Ex: ValueError, AssertionError, etc..)?
    Answer: Yes, I need to know which specific error will be produced. To know the exact error and name is by testing the code, like triggering it on purpose, or read docs.


## Questions

## Video Link
https://www.youtube.com/watch?v=tIrcxwLqzjQ&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=7

## Reflection
Today I learn why testing is important, it correlates with proper error handeling