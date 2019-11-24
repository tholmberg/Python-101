#We're going to build a simple word counter using regex (findall())

import re

test_string = "Hello world lets count some words from around the world"

print ("The original string is : " + test_string)

res = len(re.findall(r'\w+', test_string))
print ("The number of words in string are : "+str (res))
       
