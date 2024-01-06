import re

# Define a RegEx pattern to match any digits.
pattern = r'\d+.\d+'

# Define a sample string to use for pattern matching.
string = "The item costs $25.99"

# Search for the pattern in the string.
match = re.search(pattern, string)

# Print the matched substring!
print(match.group())  # prints 25.99