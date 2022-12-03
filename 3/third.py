def letterToNumber (letter: str):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return alphabet.index(letter) + 1

with open("3/input.txt") as f:
  lines = f.readlines()
  priority = 0
  for line in lines:
    half = len(line)//2
    firstHalf = line[0:half]
    secondHalf = line[half:]
    set1 = set(firstHalf)
    set2 = set(secondHalf)
    intersection = set(set1).intersection(set2)
    for letter in intersection:
      letterNumber = letterToNumber(letter)
      priority+=letterNumber
  print(priority)