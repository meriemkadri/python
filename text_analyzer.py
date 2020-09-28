import re # on importe re pour inclure plusieurs symboles dans les arguments de split
filename = input("Enter a filename: ")
with open(filename, encoding="utf8") as f:
  text = f.read()

def count_char(text):
  count = 0
  words = re.split(", |;| |\\.",text) # deux barres inversées et point \\. pour inlure le point, separer avec | pour inclure plusieurs symboles
  word = str(input("enter a word : "))
  for i in words:
      if i == word:
          count += 1
          word = i

  return count

print("le mot a été cité", count_char(text), "fois")