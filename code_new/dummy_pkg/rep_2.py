def get_user_age():
  """Gets the user's age as an integer."""
  while True:
    try:
      age = int(input("Enter your age: "))
      if age > 0:
        return age
      else:
        print("Age must be a positive number. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")
def display_welcome(name):
  """Displays a welcome message with the user's name."""
  print(f"Welcome, {name}!")
user_name = input("What is your name? ")
user_age = get_user_age()
display_welcome(user_name)
print(f"You are {user_age} years old.")