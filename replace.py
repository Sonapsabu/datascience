s = input("Enter word:")
f = open("duplicate.py", "r+")
 
# file.txt is an example here,
# it should be replaced with the file name
# r+ mode opens the file in read and write mode
f.truncate(0)
f.write(s)
f.close()
print("Text successfully replaced")
