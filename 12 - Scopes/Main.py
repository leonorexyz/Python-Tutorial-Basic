# Global and local scopes

name = "Leonore"  # Global scope

def display_name():
    print(name)  # Accessing global variable

display_name()

# Accessing global variable inside loop
for i in range(0,5):
    print(f"loop {i}: {name}")

# Branching
if True:
    print(f"if: {name}")


# Local scope
def display_local_name():
    local_name = "Leverie"  # Local scope
    print(local_name)

display_local_name()

# How to change local variable to global variable

name = "Leonore"  # Global variable

def change_name(new_name):
    global name  # Declare that we are using the global variable
    name = new_name  # Modify the global variable

print(f"Before change: {name}")
change_name("Leverie")
print(f"After change: {name}")