# Day 2: Learning Python Basics
- ### Reading Input from User
- ### Various Keywords in Python
- ### How to Create a Method in Python

## Reading Input from User
- In Python, the `input()` method is used to read input from the user via the command line. It allows you to prompt the user for input and store the entered data as a string. Here's an overview of the `input()` method.

   - `prompt` (optional): This is a string argument that is displayed to the user as a prompt or message. It provides information or instructions to the user on what kind of input is expected. The user enters their response after seeing this prompt.
- Example:
  ```python
        username = input("Enter UserName ")
         print(username)
  ```
## Various Keywords in Python
- Python has various keywords that serve as reserved words, which have special meanings within the language. These keywords are part of Python's syntax and cannot be used as variable names or identifiers. Some common Python keywords include `if`, `else`, `for`, `while`, `class`, and `def`, among others. Understanding and using these keywords correctly is crucial for writing Python code.

| Keyword   | Description                                     |
|-----------|-------------------------------------------------|
| False     | Represents the Boolean value `False`.          |
| None      | Represents a null or undefined value.          |
| True      | Represents the Boolean value `True`.           |
| and       | A logical operator for "and" conjunction.      |
| as        | Used for aliasing when importing modules or working with contexts. |
| assert    | Used for debugging purposes to check if a condition is true. |
| async     | Declares an asynchronous function or context.  |
| await     | Pauses the execution of an asynchronous function until the awaited object is complete. |
| break     | Exits the current loop (for, while).           |
| class     | Defines a class, a blueprint for creating objects. |
| continue  | Skips the current iteration of a loop and continues to the next. |
| def       | Defines a function or method.                  |
| del       | Removes a reference to an object, deleting it if there are no other references. |
| elif      | Stands for "else if" and is used in conditional statements. |
| else      | Defines the block of code to be executed if the condition in an `if` statement is not met. |
| except    | Catches and handles exceptions in a try-except block. |
| finally   | Specifies a block of code that is executed no matter what in a try-except block. |
| for       | Used to create a loop that iterates over a sequence (e.g., list, tuple, string). |
| from      | Imports specific attributes or functions from a module. |
| global    | Declares a global variable within a function.  |
| if        | Defines a conditional statement.               |
| import    | Imports a module.                             |
| in        | Checks for membership within a sequence (e.g., list, tuple). |
| is        | Compares object identity.                     |
| lambda    | Creates anonymous (nameless) functions.       |
| nonlocal  | Declares a variable as non-local, used in nested functions. |
| not       | A logical operator for "not" negation.        |
| or        | A logical operator for "or" disjunction.      |
| pass      | A placeholder statement, does nothing.        |
| raise     | Raises an exception.                          |
| return    | Specifies the return value of a function.     |
| try       | Begins a block of code where exceptions may occur. |
| while     | Defines a loop that continues as long as a specified condition is true. |
| with      | Sets up a context for resource management.    |
| yield     | Returns a generator, used in generator functions. |

## How to Create a Method in Python
- In Python, methods are functions defined within a class or associated with an object. Here's how you can create a method in Python:

```python
    def my_method( parameter1, parameter2):
        # Method code here
```
