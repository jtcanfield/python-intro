a = 1

# Basic If Statement
if a == 1:
    print("A is equal to 1")
# else if
elif a == 2:
    print("A is equal to 2")
# else
else:
    print("A is NOT 1 or 2")


# Basic For Loop
for x in [1, 2, 3]:
    print("x = " + str(x))
    # You have to say X is a string because python is strict on type


# Defining a method
def helloMethod(name):
    print("Hello, " + name)

helloMethod("Jonathan")
helloMethod("Julie")

# Nesting Statements
def print_even_or_odd(num):
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")


print_even_or_odd(0)
print_even_or_odd(1)
print_even_or_odd(2)

print("END PROGRAM")
