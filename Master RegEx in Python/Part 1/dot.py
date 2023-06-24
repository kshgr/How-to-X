import re

# Define a RegEx pattern to match any character followed by 'ox'.
pattern = r'.ox'

# Define a sample string to use for pattern matching.
string = "The quick brown fox jumps over the lazy dog"

# Search for the pattern in the string.
result = re.search(pattern, string)

# Print the matched substring!
print(result.group())
