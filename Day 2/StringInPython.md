1. **String Concatenation**: 
   - Use the `+` operator to concatenate two strings.
   - Example: `"Hello" + " " + "World"`

2. **String Length**: 
   - Use the `len()` function to get the length of a string.
   - Example: `len("Python is awesome")`

3. **String Case**: 
   - `lower()`: Converts a string to lowercase.
   - `upper()`: Converts a string to uppercase.
   - `title()`: Capitalizes the first letter of each word.
   - Examples: `"text".lower()`, `"text".upper()`, `"text".title()`

4. **String Slicing**: 
   - Extract substrings using `string[start:end]`, `string[:end]`, or `string[start:]`.
   - Example: `"Hello, World"[7:12]` returns "World".

5. **String Splitting**: 
   - Use `split()` to split a string into a list based on a delimiter.
   - Use `splitlines()` to split a string at line breaks.
   - Example: `"apple,banana,kiwi".split(",")`

6. **String Stripping**: 
   - Use `strip()`, `lstrip()`, or `rstrip()` to remove leading and trailing whitespace.
   - Example: `"   Hello, World   ".strip()`

7. **String Replacement**: 
   - Use `replace()` to replace all occurrences of a substring.
   - Example: `"I like dogs, but dogs are noisy.".replace("dogs", "cats")`

8. **String Searching**: 
   - Use `find()` to find the first occurrence of a substring.
   - Use `index()` for the same purpose but raises an error if not found.
   - Use `count()` to count occurrences.
   - Example: `"Python is awesome and Python is easy".find("Python")`

9. **String Checking**: 
   - Use `startswith()` and `endswith()` to check prefixes and suffixes.
   - Use `isnumeric()`, `isalpha()`, `isdigit()`, `isalnum()`, etc. for character checks.
   - Example: `"Python is great".startswith("Python")`

10. **String Formatting**: 
    - Use `format()` to replace placeholders with values.
    - Use f-strings (Python 3.6+) to embed expressions inside string literals.
    - Example: `"My name is {} and I'm {} years old".format(name, age)`


#ALL STRING FUNCTIONS IN PYTHON3

| Function                  | Description                                               |
|---------------------------|-----------------------------------------------------------|
| **String Concatenation** |                                                           |
| `+`                       | Concatenates two strings.                                |
|                           |                                                           |
| **String Length**        |                                                           |
| `len()`                   | Returns the length of a string.                         |
|                           |                                                           |
| **String Case**          |                                                           |
| `lower()`                 | Converts a string to lowercase.                         |
| `upper()`                 | Converts a string to uppercase.                         |
| `title()`                 | Converts the first character of each word to uppercase. |
|                           |                                                           |
| **String Slicing**       |                                                           |
| `string[start:end]`       | Extracts a substring from `start` to `end`.              |
| `string[:end]`            | Extracts a substring from the beginning up to `end`.     |
| `string[start:]`          | Extracts a substring from `start` to the end.            |
|                           |                                                           |
| **String Splitting**     |                                                           |
| `split()`                 | Splits a string into a list of substrings based on a delimiter. |
| `splitlines()`            | Splits a string at line breaks.                         |
|                           |                                                           |
| **String Stripping**     |                                                           |
| `strip()`                 | Removes leading and trailing whitespace.                |
| `lstrip()`                | Removes leading whitespace.                              |
| `rstrip()`                | Removes trailing whitespace.                             |
|                           |                                                           |
| **String Replacement**   |                                                           |
| `replace()`               | Replaces all occurrences of a substring with another substring. |
|                           |                                                           |
| **String Searching**     |                                                           |
| `find()`                  | Finds the first occurrence of a substring and returns its index. |
| `index()`                 | Finds the first occurrence of a substring and returns its index (raises an error if not found). |
| `count()`                 | Counts the number of occurrences of a substring.       |
|                           |                                                           |
| **String Checking**      |                                                           |
| `startswith()`            | Checks if a string starts with a specified prefix.      |
| `endswith()`              | Checks if a string ends with a specified suffix.        |
| `isnumeric()`             | Checks if the string contains only numeric characters.  |
| `isalpha()`               | Checks if the string contains only alphabetic characters. |
| `isdigit()`               | Checks if the string contains only digit characters.    |
| `isalnum()`               | Checks if the string contains only alphanumeric characters. |
|                           |                                                           |
| **String Formatting**    |                                                           |
| `format()`                | Formats a string by replacing placeholders with values. |
| f-strings (Python 3.6+)   | Allow embedding expressions inside string literals.    |
|                           |                                                           |
| **Character Case Conversion** |                                                       |
| `capitalize()`            | Capitalizes the first character of the string.          |
| `swapcase()`              | Swaps the case of each character.                       |
|                           |                                                           |
| **Character Removal**    |                                                           |
| `strip(char)`             | Removes specified characters from the beginning and end of a string. |
| `replace(old, new)`       | Replaces specified characters with new characters.      |
|                           |                                                           |
| **Character Checking**   |                                                           |
| `islower()`               | Checks if all characters in the string are lowercase.   |
| `isupper()`               | Checks if all characters in the string are uppercase.   |
| `isprintable()`           | Checks if all characters are printable (not control characters). |
|                           |                                                           |
| **Character Finding**    |                                                           |
| `find(char)`              | Finds the first occurrence of a character and returns its index. |
| `index(char)`             | Finds the first occurrence of a character and returns its index (raises an error if not found). |
|                           |                                                           |
| **Character Counting**   |                                                           |
| `count(char)`             | Counts the number of occurrences of a character in the string. |
|                           |                                                           |
| **Joining Strings**      |                                                           |
| `join(iterable)`          | Joins a sequence of strings using the string as a separator. |
|                           |                                                           |
| **String Partitioning**  |                                                           |
| `partition(substring)`    | Splits a string into three parts at the first occurrence of a specified substring. |
| `rpartition(substring)`   | Splits a string into three parts at the last occurrence of a specified substring. |

