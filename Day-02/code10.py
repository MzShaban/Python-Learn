import re

text = "The quick brown fox"
pattern = r"fox"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")