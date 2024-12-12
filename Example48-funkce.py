def print_hello_world():
    print("Hello world from inside the function!")

# Calling print_hello_world()
print_hello_world()
print_hello_world()

# Function definition of greet_by_name (name)
def greet_by_name(name):
    print(f"Hello, {name}")

# Call function greet_by_name (name) with "John" as the name argument
greet_by_name("John")
greet_by_name("Albert")

def print_full_name(name, surname):
    print(f"{name} {surname}")

# Calling a function without specifying thr parameter names
print_full_name("Jon", "Snow")
print_full_name("Stanis", "Baratheon")
