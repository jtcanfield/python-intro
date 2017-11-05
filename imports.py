# importing
from datetime import date
print(date.today())

# to import from a class from an unspecific directory
import classes
en_greeter = classes.Greeter()
en_greeter.greet("class")

# Import: from {filename} import {classname}
from classes import Greeter
fr_greeter = Greeter("Bonjour")
fr_greeter.greet("Jon")

# Import: from {filename} import {variable}
from classes import french_greeter
french_greeter.greet("Remy")
