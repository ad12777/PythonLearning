import re
text="The quick brown fox jumps over the lazy dog. The quick brown fox is very quick."
pattern = r" "

new_text = re.split(pattern, text)[1:]
print(new_text)