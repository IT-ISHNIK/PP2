#Write a python program to convert snake case string to camel case string.
import re
with open('row.txt', 'r', encoding = "utf-8") as f:
    text = f.read()


print('\n\nFOR snake case!')
answer1 = re.sub(r'[\W+]', '_' , text)
print(answer1.lower())


print('\n\nFOR camel case!')

def reveRse(text):
    words = re.findall(r'\b\w+\b' , text)
    string1 = ""
    for word in words:
        pattern = r'\b([a-zA-Z])|\b([а-яА-Я])'
        if re.search(pattern, word):
            ex =""
            s1 = word[0].upper()
            ex += s1
            s2 = word[1:].lower()
            ex += s2
            string1 += ex
        else:
            word = word.lower()
            string1 += word
    return string1

print(reveRse(text))
