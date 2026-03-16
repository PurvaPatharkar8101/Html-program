# text="i am good"
# print(text[ ::-1])

text = "i am good"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)