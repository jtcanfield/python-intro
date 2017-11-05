# Classes
class Greeter:
    # ALL CLASSES HAVE TO HAVE SELF SET
    # This line is required:
    def __init__(self, greeting="Hello", excited=True):
        # "greeting" does not have to be set, but if it is, it will
        # use what it is set as by default if nothing is specified
        self.greeting = greeting
        self.excited = excited
        # Also, any variables in init must be declared like above

    def greet(self, name):
        punct = "."
        if self.excited:
            punct = "!"
        print(self.greeting + " " + name + "!")

# Now, the classes "self" must be set...
english_greeter = Greeter()
spanish_greeter = Greeter("Hola", False)
french_greeter = Greeter(excited=True, greeting="Bonjour")

# ...And Called
english_greeter.greet("Remy")
spanish_greeter.greet("Remy")
french_greeter.greet("Remy")

# Or if you want to take a shortcut
Greeter("Hello").greet("Shorty")
