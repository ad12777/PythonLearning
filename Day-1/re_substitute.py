import re

text="The quick brown fox jumps over the lazy dog."
pattern = r"quick"

replacement = "stupid"
new_text = re.sub(pattern, replacement, text)
print("Original text:", text)
print("Modified text:", new_text)
