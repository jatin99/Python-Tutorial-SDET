# Loop Concepts in Python

## Difference between for and while loop:

- A `for` loop is used for iterating over a sequence (e.g., a list, tuple, string) or other iterable objects. It iterates a specific number of times.
- A `while` loop is used to repeatedly execute a block of code as long as a condition is true. It may iterate an unknown number of times.

### When to use:

- Use a `for` loop when you know how many times you want to iterate (e.g., when iterating through a known list of items).
- Use a `while` loop when you want to repeat a block of code until a specific condition is met (e.g., when waiting for user input).

## Purpose of range():

- The `range()` function generates a sequence of numbers. It is often used with loops to control the number of iterations. It can take up to three arguments: start, stop, and step.

## Terminating a loop prematurely:

You can use the `break` statement to exit a loop prematurely. It immediately terminates the loop and transfers control to the statement immediately after the loop.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

## Print even numbers from a list:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)
```

## Infinite loop:
- An infinite loop is a loop that never terminates on its own. It continues to execute indefinitely. This can happen if the loop condition is always true or if there is no exit condition.

- To avoid an accidental infinite loop, make sure to provide a condition that will eventually become false, or use control flow statements like break to exit the loop when needed.