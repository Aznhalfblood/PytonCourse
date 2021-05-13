import re

def convert(some_tuple_3):
    return some_tuple_3[0] + " " + some_tuple_3[1] + " = " +some_tuple_3[2]

pattern = r"(int|short|byte)\s([\w]+)\s?=\s?[-+]?(\d+)"

f = open("data.txt")   
str = f.read()

print("Text in file:\n\n" + str + '\n\n')

match = re.findall(pattern, str)

print("\n\nFounded:\n\n" )
if match:
    for item in match:
        print(convert(item))





