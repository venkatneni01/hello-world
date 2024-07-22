def make_even(num):
    if num % 2 == 1:
        return num + 1
    else:
        return num

# List of numbers to process
x = [552, 551, 543, 45, 33, 22, 448, 339, 229, 44, 39, 49]

# Create an empty list to store the results
y = [] 

# Process each number in the list x using the make_even function
for num in x:
    y.append(make_even(num))

# Print the resulting list
print(y)
