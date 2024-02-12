#Create a list of capital letters in the english alphabet
all_capital_letters = [chr(i) for i in range(65, 91)]
print(all_capital_letters)

# Create a list of capital letter from the english aplhabet,
# but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
exclude_code_points = [70, 75, 80, 85]
filtered_capital_letters = [chr(i) for i in range(65, 91) if i not in exclude_code_points]
print(filtered_capital_letters)

#Create a list of capital letter from from the english aplhabet, but exclude every second between F & O
exclude_range_start = ord('F')
exclude_range_end = ord('O')
filtered_range_capital_letters = [chr(i) for i in range(65, 91) if exclude_range_start <= i <= exclude_range_end and (i - exclude_range_start) % 2 != 0 or i < exclude_range_start or i > exclude_range_end]
print(filtered_range_capital_letters)

#Clothes List Comprehension
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
soled_out = [('Black', 'm'), ('White', 's')]

result = [(color, size) for color in colors for size in sizes if (color, size) not in soled_out]
print(result)
