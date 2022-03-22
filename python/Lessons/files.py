def file_handling():
    # Python can be used to create, update, delete, or read files. 
    
    sample = 'sample.txt'

    txt = open(sample, 'rt', encoding='utf-8') # rt is the default mode parameter which specifies action = read and type = text
    # utf-8 is specified to force utf-8 encoding which is not done by default.

    # once the file has been opened and placed into the txt variable, we can print it to the screen.
    print(txt.read()) # use the read method to move the content of the file into memory and print to output it to the screen.

    # now that we have read the file, it is best to close it in order to commit changes in memory to disk. 

    txt.close()


    return()

def regex():
    import re # import the regex module to begin searching for regular expressions.

    sample = 'sample.txt'
    txt = open(sample, encoding='utf-8')

    x = txt.read() # read the file to store it in memory.

    y = re.findall('Python', x) # find all instances of Python in sample.txt.
    
    print(len(y)) # provides a count of the instances of Python in sample.txt.

    txt.close()
    return()

def write_files():
    
    test = 'test.txt' # name the file.

    txtCreate = open(test, 'x', encoding='utf-8') # define a function for creating the test file.

    txtCreate.write('This test document has content now!\n') # create and write to test document.

    txtCreate.close() # close to commit changes to disk.

    txtRead = open(test, 'rt',encoding='utf-8') # create a function to read the contents of the test document.

    print(txtRead.read()) # print the contents of the test doc.

    txtRead.close() # close the test document to free it up for more changes.

    txtWrite = open(test, 'a', encoding='utf-8') # create a function to append content to the test document.

    txtWrite.write('This test document has more content now!') # write content to the test document.

    txtWrite.close() # close to commit changes to disk.
    
    txtRead = open(test, 'rt',encoding='utf-8') # call function to open the file and read it. 

    print(txtRead.read()) # read the contents of the test document.
 
    txtRead.close() # close to release from memory.
    return()

def delete_files():

    import os # more advanced os specific functions can be accessed with the os module.
    
    os.remove('test.txt') # remove test.txt from the current directory.

    return()