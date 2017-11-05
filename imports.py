# importing
from datetime import date
print(date.today())

# to import from a class from an unspecific directory
import classes
en_greeter = classes.Greeter()
en_greeter.greet("class")

# from greeter import classes
from classes import Greeter
fr_greeter = Greeter("Bonjour")
fr_greeter.greet("Jon")
