import re

# Define a RegEx pattern to match any character within the brackets [].
pattern = r'[aeiou]'

# Define a sample string to use for pattern matching.
string = "Hey, let's decode Regular Expressions."

# Search for the pattern in the string.
result = re.findall(pattern, string)

# Print the matched substring!
print(result)