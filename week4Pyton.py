#create file and write
file = open('new file.doc','w')
file.write("Read & Write Challenge.\n" ) 


#read a file
file = open('new file.doc', 'r')
data = file.read()
print(data)

# Appending content
file = open('new file.doc','a')
file.write("Create a program that reads a file and writes a modified version to a new file.")

#•	Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    file = open ('newfile.pdf','r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found! What's the corectly filename?")
finally:
    file.close()





   

