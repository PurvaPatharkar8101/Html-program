# text=input("enter a string")
# rev_text= text[::-1]
# print(rev_text)




     
     
text = input("Enter the string: ")
print("Reverse of the given string:")

str1 = ""

for ch in text:
    str1 = ch + str1   # Add character in front

print(str1)
