#Create a list of even numbers from 0 to 20.
even_numbers = [num for num in range(0, 21) if num % 2 == 0]
print(even_numbers)

#Create a list of squares of numbers from 1 to 10.
squares = [num**2 for num in range(1, 11)]
print(squares)

#Create a list of all the vowels in a given string.
input_string = "Hello, World!"
vowels = [char.lower() for char in input_string if char.lower() in 'aeiou']
print(vowels)

#Create a list of common elements in two given lists. (could this be done with the use of another datastructure?)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [element for element in list1 if element in list2]
print(common_elements)

#Create a list of words from a given string that have more than 4 and less than 8 letters.
random_string = "heeeej hej heeeeej hej hej hej jjjjjjjj"
more_or_less = [word for word in random_string.split() if 4 < len(word) < 8]
print(more_or_less)

#Flatten list 

list_of_lists = [
    [1, 2, 3],
    [4, 5],
    [6],
    [7, 8, 9],
]
flattened_list = [element for sublist in list_of_lists for element in sublist]
print(flattened_list)