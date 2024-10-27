# 5) Palindrome Checker (3 ქულა)
# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.
# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False

def palindrome (str1):
    normal_str = ""
    for i in str1:
        if ("a" <=i <= "z") or ("A" <=i <= "Z"):
            normal_str += i.lower ()
    reversed_str = ""
    for x in normal_str:
        reversed_str = x + reversed_str
    return normal_str == reversed_str

print (palindrome("A man a plan a canal Panama"))
print (palindrome("Hello"))