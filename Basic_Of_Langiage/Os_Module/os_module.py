import os
#----------------FOR NAME----------------
#print(os.name)

#----------------MAKING DIRECTORY---------------- 
if(not os.path.exists("Data")):
    os.mkdir("Data")

for i in range(1,101):
    if not os.path.exists(f"Data/Day{i}"):
        os.mkdir(f"Data/Day{i}")  
        #rename the folder
        #os.rename(f"Data/Day{i}", f"Data/Pratice {i}")  

folder = os.listdir("Data")

#file and folder  #display
for i in folder:
    #print(i) 
    #print(os.listdir(f"Data/{i}"))
    os.rmdir(f"Data/{i}")    
os.rmdir("Data")    

#----------------CHECK THE DIRECTORY----------------
#getcwd()-->It returns the current working directory(CWD) of the file
#print(os.getcwd())

#---------------CHANGE THE DIRECTPRY---------------
#os.chdir()-->The os module provides the chdir() function to change the current working directory.
#os.chdir("E:\Python\In VsCode\Data")

#----------------ERRORS-----------------
"""
try:  
    # If file does not exist,  
    # then it throw an IOError 
    # ------------------------------------------ 
    # filename = 'Python.txt'  
    # f = open(filename, 'r')  
    # text = f.read()  
    # f.close()  
    
    # If file does exist,  
    # then it does not throw an IOError 
    #  # ------------------------------------------  
    filename = 'NewFile.txt'  
    f = open(filename, 'r')  
    text = f.read()  
    f.close() 
    print(text)
# The Control jumps directly to here if  
# any lines throws IOError.  
except IOError:  
  
    # print(os.error) will <class 'OSError'>  
    print('Problem reading: ' , filename)  
    """ 

#--------------------------------------------------------------------------------------------
"""
#os.popen() -->This function opens a file or from the command specified, and it returns a file object which is connected to a pipe.    
fd = "python.txt"      
    
# popen() is similar to open()     
file = open(fd, 'w')     
file.write("This is awesome")     
file.close()     
file = open(fd, 'r')     
text = file.read()     
print(text)     
      
# popen() provides gateway and accesses the file directly     
file = os.popen(fd, 'w')     
file.write("This is awesome")     
# File not closed, shown in next function.           """

#os.close()-->This function closes the associated file with descriptor fr.   
# fr = "Python.txt"    
# file = open(fr, 'r')     
# text = file.read()     
# print(text)     
# os.close(file)