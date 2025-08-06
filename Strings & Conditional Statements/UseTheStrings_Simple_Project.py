#Concatenation (দুটি স্ট্রিং জোড়া)
#Length
#Reverse
#Vowel Count
#Palindrome Check

# Step 1: Input from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Step 2: String Concatenation
combined = str1 + str2
print(f"\nConcatenated String: {combined}")

# Step 3: Length of combined string
print(f" Length of combined string: {len(combined)}")

# Step 4: Reverse the combined string
reversed_str = combined[::-1]
print(f"Reversed string: {reversed_str}")

# Step 5: Count vowels in combined string
vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in combined if c in vowels)
print(f" Total vowels: {vowel_count}")

# Step 6: Check if combined string is palindrome
if combined == reversed_str:
    print(" It is a palindrome.")
else:
    print(" It is not a palindrome.")
