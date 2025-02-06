# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n - 1)
# num = float (input("Enter a number: "))
# print("Factorial of", num, "is", factorial(num))



# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n - 1)

# def input_output():
#   num = int(input("Enter a number: "))
#   result = factorial(num)
#   print("Factorial of", num, "is" , result)

# input_output()


# name = input ("what is your name? ")
# print ("hello," , name ,"!")

def get_user_age():
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
    print (f"Welcome,{name}!")
user_name = input ("what is your name?")
user_age = get_user_age()
display_welcome(user_name)
print(f"you are {user_age} years old.")  

  
# File: my_program.py

def main():
    print("Program is running")

if __name__ == "__main__":
    main()