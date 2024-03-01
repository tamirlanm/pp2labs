import re
#task1
#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
def rowpy(text):
   if re.search("^a(b*)$",text):
      return "matched"
   else:
      return "not"
print(rowpy("abbb"))
print(rowpy("a"))
print(rowpy("b"))

print()
#task2
#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def rowpy(text):
   if re.search("^a(b{2})$",text) or re.search("^a(b{3})$",text):
      return "matched"
   else:
      return "not"
print(rowpy("abbb"))
print(rowpy("ab"))
print(rowpy("abb"))
print()

#task3
#Write a Python program to find sequences of lowercase letters joined with a underscore.
def rowpy(text):
   if re.search("^[a-z]+_+[a-z]",text):
      return "matched"
   else:
      return "not"
print(rowpy("lowecase_lowercase"))
print(rowpy("lowercase"))
print(rowpy("under_lowercase"))
print()

#task4
#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def rowpy(text):
   if re.search("^[A-Z]{1}+[a-z]+",text):
      return "found"
   else:
      return "not"
print(rowpy("Aandlowercases"))
print(rowpy("lowercases"))
print(rowpy("AAfff"))
print()

#task5
#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def rowpy(text):
   if re.search("^a.*b$",text):
      return "matched"
   else:
      return "not"
print(rowpy("a_to_b"))
print(rowpy("beginb"))
print(rowpy("athisnotworkd"))
print()

#task6
#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def rowpy(text):
   return re.sub("[ ,.]",":",text)
print(rowpy("comma,space dot."))
print()

#task7
#Write a python program to convert snake case string to camel case string.
def rowpy(text):
   t=text.split('_')
   return t[0] + ''.join(x.title() for x in t[1:])
print(rowpy("snake_to_camel"))
print()

#task8
#Write a Python program to split a string at uppercase letters.
def rowpy(text):
   return re.findall("[A-Z][^A-Z]*",text)
print(rowpy("A  to AAAAAA"))
print(rowpy("thisNOtlistT"))
print()

#task9
#Write a Python program to insert spaces between words starting with capital letters.
def rowpy(text):
   return re.sub(r"(\w)([A-Z])",r"\1 \2",text)
print(rowpy("PythonAndLabs"))

#task10
#Write a Python program to convert a given camel case string to snake case.
def rowpy(text):
   return re.sub(r"([a-z0-9])([A-Z])",r"\1_\2",text).lower()
print(rowpy("toSnake"))
print(rowpy("CamelStringBecomeToSnakeString:)"))