import re

# Define a RegEx pattern to match one or more occurances of character preceeded by +.
pattern = r'ab+c'

# Define a sample string to use for pattern matching.
string = "ac, abc, abbbbc"

# Search for the pattern in the string.
result = re.findall(pattern, string)

# Print the matched substring!
print(result)