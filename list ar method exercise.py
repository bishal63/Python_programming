#Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0]='kiwi'
print(fruits)

#Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append('orange')
print(fruits)

#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,'lemon')
print(fruits)

#Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove('banana')
print(fruits)

#Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))