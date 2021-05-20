fruits = ["apple", "woodapple", "pears", "banana"]

# add a new value named `mango` to the above list
print(fruits)
fruits.append("mango")
print(fruits)

# Pick the value woodapple from it
print(fruits[1])

# Replace woodapple with guava
fruits[1] = 'guava'
print(fruits)

# Remove pears from it
fruits.remove("pears")
print(fruits)

# print the lenght of the list/array
print (len(fruits))

# print each element of the list/array in a separate line
for i in fruits:
    print (i)