# Classes
class Greeter:
    # ALL CLASSES HAVE TO HAVE "SELF" SET
    # This line is required:
    def __init__(self, greeting="Hello", excited=True):
        # "greeting" does not have to be set, but if it is, it will
        # use what it is set as by default if nothing is specified
        self.greeting = greeting # Sets greeting to use
        self.excited = excited # boolean for punctuation
        # Also, any variables in init must be declared like above

        # ALWAYS REMEMBER to use self below, or else you will get a "this takes two arguments" error
    def greet(self, name):
        punct = "."
        if self.excited:
            punct = "!"
        # Normal string
        # print(self.greeting + " " + name + punct)
        # String Interpolation
        # print("%s %s%s" % (self.greeting, name, punct))
        message = "%s %s%s" % (self.greeting, name, punct)
        print(message)

# Now, the classes "self" must be set...
english_greeter = Greeter()
spanish_greeter = Greeter("Hola", False) # You can call it in order of the init...
french_greeter = Greeter(excited=False, greeting="Bonjour") # ...or set them manually

# ...And Called
# english_greeter.greet("Remy")
# spanish_greeter.greet("Remy")
# french_greeter.greet("Remy")

# Or if you want to take a shortcut
# Greeter("Hello").greet("Shorty")


# Multi-line String
multi_line_string = """
Hello!
"""
# print(multi_line_string)
