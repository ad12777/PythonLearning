import re

string= "The quick brown fox jumps over the lazy dog"
pattern = r"The quick"
match = re.match(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")