import re

# Define a RegEx pattern to match the start of a string.
pattern = r'^Hello'

# Define a sample string to use for pattern matching.
string = "Hello, Python world!"

# Search for the pattern in the string.
match = re.search(pattern, string)

# Print the results
print("Match found!" if match else "No match")