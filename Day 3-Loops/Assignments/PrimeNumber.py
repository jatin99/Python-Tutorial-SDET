'''
Assignment: Find Prime Numbers

Write a Python program that finds all prime numbers within a given range.

Requirements:

The program should take two integers, start and end, as input from the user.
It should then find and print all prime numbers between start and end, inclusive.
If start or end is less than 2, the program should handle this case gracefully 
and provide a message indicating that there are no prime numbers in that range.

Input: 
Enter the start of the range: 10
Enter the end of the range: 20

Output:
Prime numbers between 10 and 20: 11, 13, 17, 19

Instructions:

Define a function is_prime(n) that takes an integer n as input and returns 
True if n is a prime number and False otherwise.

In your main program, prompt the user to enter the start and end values.

Use a for loop to iterate through the range of numbers from start to end.

For each number in the range, check if it is prime using the is_prime function. 
If it is, add it to a list of prime numbers.

After the loop, if the list of prime numbers is not empty, print them. Otherwise,
 print a message indicating that there are no prime numbers in the given range.

Remember to handle edge cases where start or end is less than 2.

'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start >= 2:
    prime_numbers = find_primes_in_range(start, end)
    if prime_numbers:
        print(f"Prime numbers between {start} and {end}: {', '.join(map(str, prime_numbers))}")
    else:
        print(f"There are no prime numbers between {start} and {end}.")
else:
    print(f"There are no prime numbers less than 2.")
