import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern,text)

if search:
  print("pattern is found")
else:
  print("pattern not found")