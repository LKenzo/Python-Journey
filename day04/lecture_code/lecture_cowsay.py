import cowsay
import sys

if len(sys.argv) < 2:
    cowsay.cow("Too few arguments")
    sys.exit("Goodbye!")

message = ""

for arg in sys.argv[1:]:
    message += arg + " "

cowsay.cow("Hello, " + message)