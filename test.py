import requests

response = requests.get("https://baconipsum.com/api/?type=meat-and-filler.\n")

paragraphs = response.json()
paragraphs.reverse()
breaks = '\n'.join(paragraphs)
print(breaks)
print()

str_pancetta = str(paragraphs)
str_pancetta.lower()
pancetta = str_pancetta.count("pancetta")
print(f"How many pancettas are here?: {pancetta}\n")


print(f"This silly program is made by Yevhen Sirenko at 3:36 a.m.\n")