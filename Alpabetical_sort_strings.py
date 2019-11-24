# Parse a string and then apply an alphabetical sort to the words

#Apply a string to the code
# my_str = "Hello world Lets parse some strings!"

#User input a string
my_str = input ("Enter a string: ")

#Break the string into a list
words = my_str.split()

#sort the list
words.sort()

#dsplay the sorted words

print ("The sorted words are: ")
for word in words:
    print(word)
