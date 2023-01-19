
with open('fruits.txt', 'r') as fruits:
   for word in fruits:
      if word[0] == 'a':
         print(word, end=''),
