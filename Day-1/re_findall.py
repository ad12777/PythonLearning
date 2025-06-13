import re

text= "The quick brown fox jumps over the lazy dog. The quick brown fox is very quick."
pattern = r"quick"
found = re.findall(pattern, text)
length = len(found)
print("Number of matches found:", length)
if found:
    print("Matches found:", found)
else:
    print("No matches found.")