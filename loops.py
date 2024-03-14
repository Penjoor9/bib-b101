# loop over an array
fruits = ['a', 'b', 'c']

# loop through each evelement
# at each stage, if the element is 'a'
# print true
for e in fruits:
  if e == 'a':
    print('True')

# loop through each evelement
# at each stage, if the element is 'c'
# print true
for e in fruits: # 1.e = 'a', 2.e = 'b 3. e = 'c'
  if e == 'c':
   print('True')
  if e == 'b':
   print('True')

# # Iterate over a string
greeting = "Hello"
for char in greeting:
  print(char)
# Exercise: check if the string contains vowel