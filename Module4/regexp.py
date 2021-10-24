import re

# match

greet = "How are you. How is everything"

# match= re.match("How", greet)
# print(match.span())
# print(match.group())
# print(match.string)

# findall

#matches = re.findall("H[m-p].", greet)
# matches = re.findall("H[a-c].", greet)
# print(matches)


# search

# matches = re.search("How", greet)
# print(matches)
# print(matches.span())
# print(matches.group())
# print(matches.string)

text = "Python is cool, Python is awesome"
replaced_text = re.sub("cool", "good", text)
print(replaced_text)


email_addresses = "sammy priya@google.com, test test2 sam@yahoo.com yahooooo water"

print(re.sub(r'([\w.-]+)@([\w.-]+)', r'\1@edureka.com', email_addresses))

print(re.split('@', email_addresses))