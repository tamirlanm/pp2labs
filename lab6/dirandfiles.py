#task1
print("TASK1:")
#Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = 'C:\\Users\\TamirlanM\\Desktop'
print("Only directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([name for name in os.listdir(path)])
print()

#task2
print("TASK2")
#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
print('exist:', os.access('c:\\Users\\TamirlanM\\Desktop\\pp2', os.F_OK))
print('readable:', os.access('c:\\Users\\TamirlanM\\Desktop\\pp2', os.R_OK))
print('writable:', os.access('c:\\Users\\TamirlanM\\Desktop\\pp2', os.W_OK))
print('executable:', os.access('c:\\Users\\TamirlanM\\Dekstop\\pp2', os.X_OK))
print()

#task3
print("TASK3")
#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
print("Test a path exists or not:")
path = r'C:\\Users\\TamirlanM\\Dekstop\\music'
print(os.path.exists(path))
path = r'C:\\Users\\TamirlanM\\Desktop\\music'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
print()

#task4
print("TASK4")
#Write a Python program to count the number of lines in a text file.
f=open("C:\\Users\\TamirlanM\\Desktop\\forpyt.txt","r")
counter=0
c=f.read()
clist=c.split("\n")
for i in clist:
    if i:
        counter+=1
print(f"This is the number of lines in the file {counter}")
f.close()
print()

#task5
print("TASK5")
#Write a Python program to write a list to a file.
alist = ["Python", "C++", "Java", "C#","Javascript", "Unreal Engine"]
alist2 = ['1sem','2sem','3sem','4sem','5sem','6sem']
f5 = "task5.txt"
myfile = open(f5,'w')
for i in range(0,6):
    thetext = alist[i] + '-' +alist2[i]+'\n'
    myfile.write(thetext)
myfile.close()
print('The list written written')
print()

#task6
print("TASK6")
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
a=64
for i in range(0,26):
    i+=a+1
    f = open(chr(i)+'.txt','w')
    f.close()
print()

#task7
print("TASK7")
#Write a Python program to copy the contents of a file to another file
with open('task5.txt','r') as file, open('A.txt','w') as myfile:
    for i in file:
        myfile.write(i)
myfile.close()
myfile = open('A.txt','r')
print(myfile.read())
myfile.close()
print()

#task8
print("TASK8")
#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
if os.access("c:\\Users\\TamirlanM\\Desktop\\f4.txt",os.F_OK)==True:
    os.remove("c:\\Users\\TamirlanM\\Desktop\\f4.txt")
else:
    print("file does not exists")