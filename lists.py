# Lists

shark = ['great white', 'mako','duck', 'ur mom', 'pineapple']
numbers = [1,2,3,4, "how many niggers are in my store"]

print(shark)
print(numbers)

fruit = ['apple', 'pear', 'peach', 'banana', 'pineapple']

for x in range(0, len(fruit), 1):
  print(fruit[x])

for i in range(0, len(fruit), 1):
  fruit[i] = fruit[i] + "'s are great!"

print(fruit)

word = 'What do?'
letters = list(word)

print(letters)