import sys

# why does sys.argv use 1 not 0? Reasoning: The name of the program that we're executing [lecture_name.py]
#print can be changed to sys.exit
if len(sys.argv) < 2:
     sys.exit("Too few arguments")

print("Hello, my name is")
for arg in sys.argv[1:]:
     print(arg)

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError: 
#     print("Too few arguments")