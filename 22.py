#wap to define a module & import a specific funtion in that module to another program in python

from my_module import greet

def main():
    # Using the greet function from the imported module
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

# Execute the main function
if __name__ == "__main__":
    main()
