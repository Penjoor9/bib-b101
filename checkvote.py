userinput = input("enter your age: ")

userAge = int(userinput)
if userAge >= 18:
  print('You can vote')
else:
  print('You cannot vote')

# 3. Check if user can vote
if userAge > 18:
  print('You can vote')
elif userAge < 18:
  print('You cannot vote')