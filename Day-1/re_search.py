import re
text= "The quick brown fox jumps over the lazy dog. The quick brown fox is very quick."
pattern = r"quick"
found = re.search(pattern, text)
if found:
    print("Match found:", found.group())
else:
    print("No match found.")