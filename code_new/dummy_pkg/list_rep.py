def demonstrate_lists():
    # Creating lists
    fruits = ['apple', 'banana', 'orange']
    numbers = [1, 2, 3, 4, 5]
    
    # Adding elements
    fruits.append('grape')
    print("After append:", fruits)
    
     # Inserting at specific position
    fruits.insert(1, 'mango')
    print("After insert:", fruits)
    
    # Accessing elements
    print("Fi# rst fruit:", fruits[0])
    print("Last fruit:", fruits[-1])
    
     # Slicing
    print("First three fruits:", fruits[:3])
    
    # Removing elements
    removed_fruit = fruits.pop()
    print("Removed fruit:", removed_fruit)
    print("After pop:", fruits)
    
    # List length
    print("Number of fruits:", len(fruits)) 
    
    # Checking if element exists
    print("Is apple in fruits?", 'apple' in fruits)
    
    # Sorting
    fruits.sort()
    print("Sorted fruits:", fruits)
    
    # Reversing
    fruits.reverse()
    print("Reversed fruits:", fruits)                                                                                                                                                                                                                                                                                                                                   
    
    # Run the demonstration
demonstrate_lists() 
