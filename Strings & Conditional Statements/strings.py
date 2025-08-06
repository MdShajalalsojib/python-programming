str1 = "this is a string."
str2 = 'This is a string.'
str3 = """This is a String."""
print(str1)
print(str2)
print(str3)

#String array
name =  "shajalal"
print(name[3])

#1. for loop দিয়ে স্ট্রিং এর উপর লুপ চালানো

name = "Nazmul"
for char in name:
    print(char)

# 2. স্ট্রিং এর ইনডেক্স সহ লুপ (index সহ character access)

name = "Shajalal"
for i in range(len(name)):
    print(f"Index {i}= {name[i]}")

#3. while loop দিয়ে স্ট্রিং এর উপর লুপ চালানো

name = "String"
i = 0

while i < len(name):
    print(name[i])
    i += 1
   
#4. স্ট্রিং এর অক্ষর গুলো উল্টো (reverse) করে প্রিন্ট করা

name = "Sojib"

for char in reversed(name):
    print(char)

# কতগুলো 'a' আছে একটা স্ট্রিং-এ?

message = "banana is a fruit"
count = 0

for char in message:
    if char == 'a':
        count += 1

print("Total 'a':", count)

#len(string)

name = "Sojib"
print(len(name))    




