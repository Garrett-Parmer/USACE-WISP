testArray = []


text_file = open("romeo.txt")
str = text_file.read()

testArray = str.split()

testArray.sort()
print(testArray)
