# A String is a data structure in Python that represents a sequence of characters.
# It is an immutable data type, meaning that once you have created a string, you cannot change it.
# Strings are used widely in many different applications, such as storing and manipulating text data,
# representing names, addresses, and other types of data that can be represented as text.

# String Concatenation
# String concatenation involves combining multiple strings into a single string using the + operator.
string1 = "Python"
string2 = "Data Science"
concatenated_string = string2 + " " + string1
print(concatenated_string)  # Output: Data Science Python

# String Replication
# String replication is achieved by using '*' operator to create repeated copies of a string.
original_string = "Python"
replicated_string = original_string * 3
print(replicated_string)  # Output: PythonPythonPython

# String Length
# The len() function returns the length (number of characters) of a string.
string = "Python is powerful!"
length = len(string)
print(length)  # Output: 20

# String Slicing
# In Python, the String Slicing method is used to access a range of characters in the String.
# Slicing in a String is done by using a colon (:). It includes the start index but excludes the end index.
String1 = "GeeksForGeeks"
print("Slicing characters from 5-12: ", String1[5:12])  # Output: ForGeek
print("Slicing characters between 3rd and 3rd last character: ", String1[3:-3])  # Output: ksForGe

# String Case Conversion
# Strings can be converted to uppercase or lowercase using upper() and lower() methods.
string = "Hello, Python!"
uppercase_string = string.upper()
lowercase_string = string.lower()
print(uppercase_string)  # Output: HELLO, PYTHON!
print(lowercase_string)  # Output: hello, python!

# String Stripping
# Stripping removes leading and trailing whitespace from a string using strip(), lstrip(), or rstrip().
whitespace_string = "   Python   "
stripped_string = whitespace_string.strip()
print(stripped_string)  # Output: Python
l_stripped_string = whitespace_string.lstrip()
print(l_stripped_string)  # Output: Python   
r_stripped_string = whitespace_string.rstrip()
print(r_stripped_string)  # Output:    Python

# String Replacing
# The replace() method replaces occurrences of a substring with another substring.
string = "I am beginner in Python"
new_string = string.replace("beginner", "experienced")
print(new_string)  # Output: I am experienced in Python

# String Count
# The count() method counts the number of occurrences of a substring in a string.
string = "python program run on python IDLE, in pythonic way."
count = string.count("python")
print(count)  # Output: 3

# String Find
# The find() method returns the index of the first occurrence of a substring. If not found, it returns -1.
string = "Python is powerful and Pythonic."
index = string.find("Python")
print(index)  # Output: 0
index = string.find("python")
print(index)  # Output: -1

# String Formatting
# Strings in Python can be formatted using the format() method, which contains curly braces {} as placeholders.
# These placeholders can hold arguments according to position or keyword to specify the order.
String1 = "{} {} {}".format('Beginner', 'in', 'Python')
print("Print String in default order: ", String1)  # Output: Beginner in Python
String1 = "{1} {0} {2}".format('Beginner', 'in', 'Python')
print("Print String in Positional order: ", String1)  # Output: in Beginner Python
String1 = "{l} {f} {g}".format(g='Beginner', f='in', l='Python')
print("Print String in order of Keywords: ", String1)  # Output: Python in Beginner

# Challenge Galore
# Problem Statement - Analyzing User-Generated Text Data for Keyword Frequency
from collections import Counter
import re

def analyze_text_data(text_data):
    combined_text = ' '.join(text_data)

    # Convert to lowercase to make the analysis case-insensitive
    combined_text = combined_text.lower()

    # Find all words in the text
    words = re.findall(r'\b\w+\b', combined_text)

    # List of keywords to analyze
    keywords = ['keyword1', 'keyword2', 'keyword3']

    # Count the frequency of each keyword in the text
    keyword_counts = Counter(words)

    # Display the frequency of each keyword
    for keyword in keywords:
        print(f'The keyword "{keyword}" appears {keyword_counts[keyword]} times.')

# Example usage:
text_data = [
    "User-generated text data for keyword frequency analysis.",
    "Analyzing text data helps to understand user preferences.",
    "This is an example of analyzing keyword frequency in Python."
]
analyze_text_data(text_data)
