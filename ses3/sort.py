# Sort a text
def process_string(input_string):
    vowels = 'aeiouAEIOU'
    
    # Remove vowels
    consonants = [char for char in input_string if char not in vowels]
    
    # Sort the consonants
    sorted_consonants = sorted(consonants)
    
    return sorted_consonants

# Example usage:
input_str = "Hello, World!"
result = process_string(input_str)
print(result)

#sort a list
# List of strings with names
names = ['Claus', 'Ib', 'Per']

# Sort the list alphabetically
sorted_names = sorted(names)
print("Sorted alphabetically:", sorted_names)

# Sort the list in reversed order
reverse_sorted_names = sorted(names, reverse=True)
print("Sorted in reversed order:", reverse_sorted_names)

# Sort the list based on the length of the name
length_sorted_names = sorted(names, key=len)
print("Sorted by length of name:", length_sorted_names)

# Sort the list based on the last letter in the name
last_letter_sorted_names = sorted(names, key=lambda x: x[-1])
print("Sorted by last letter of name:", last_letter_sorted_names)

# Sort the list with names containing 'a' first (alphabetically)
contains_a_sorted_names = sorted(names, key=lambda x: (not 'a' in x.lower(), x.lower()))
print("Sorted with 'a' first (alphabetically):", contains_a_sorted_names)

#Text editoer plugin simulation 
# Given string
s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

# Count the number of characters including blank spaces
total_characters = len(s)
print("Total characters (including blank spaces):", total_characters)

# Count the number of characters excluding blank spaces
characters_excluding_spaces = len(s.replace(' ', '').replace('\n', ''))
print("Total characters (excluding blank spaces):", characters_excluding_spaces)

# Count the number of words
word_count = len(s.split())
print("Total words:", word_count)

#Sort a list of tuples 
# Given list of tuples
data = [(1, 2), (2, 2), (3, 2), (2, 1), (2, 2), (1, 5), (10, 4), (10, 1), (3, 1)]

# Sort the list by the last element, then by the first element in each tuple
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))

# Print the result
print(sorted_data)

# Logic if/else 
# Traditional if/else approach
def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

# One-liner using a ternary operator
calculate_grade_one_liner = lambda score: "Invalid score" if score < 0 or score > 100 else "A" if score >= 90 else "B" if 80 <= score <= 89 else "C" if 70 <= score <= 79 else "D" if 60 <= score <= 69 else "F"

# Example usage
print(calculate_grade(75))  # Output: C
print(calculate_grade_one_liner(85))  # Output: B

#And / or logic
# Straightforward approach
def reserve_room(room_number, guests, room_availability):
    if room_number not in room_availability:
        return False
    if guests <= room_availability[room_number]['capacity'] and not room_availability[room_number]['booked']:
        room_availability[room_number]['booked'] = True
        return True
    return False

# Example usage
rooms = {
    '101': {'capacity': 2, 'booked': False},
    '102': {'capacity': 4, 'booked': True},
    # Add more rooms as needed
}

print(reserve_room('101', 2, rooms))  # Output: True


