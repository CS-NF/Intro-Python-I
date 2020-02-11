"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

import os

# need to find the file path
path = os.path.dirname(os.path.realpath(__file__))

f = open(f"{path}/foo.txt", "r")
read_the_data = f.read()
print(read_the_data)





# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar_f = open(f"{path}/bar.txt", "w") 
bar_f.write(str("To infinity and beyond\n Galaxy far far away\n Live long and prosper"))

bar_f.close()