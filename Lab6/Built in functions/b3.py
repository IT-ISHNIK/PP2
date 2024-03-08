#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
string = input("Enter a string: ")
string1 = ''.join(reversed(string))
if (string == string1):
    print("It is polindrome")
else:
    print("It is not polindrome")