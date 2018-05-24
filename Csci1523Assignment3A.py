# Programming Assignment:Programming Project 3 - System Administration
# Course: 1523 Spring 2017
# Meetings: Monday 12:00p to 2:00p
# Student Name: Blaine Jacques  
# Instructor: Sheaffer
# Assignment Description: Network professionals and systems administrators are
# frequently asked to develop statistics from system log files and system
# configuration files. This program will analyze such files and give statistics
# concerning system reliability issues. 


#These 4 lines will open the gettsburg file to read or will tell the
#user that the file can't be read.
try:
    fh = open('passwd.dat','r')
except IOError:
    print('Error opening file, passwd.dat')


#These 4 lines will read the file until  an empty string is returned,
#or return an error made while trying to read the file.
try:
    filestr = fh.read()
except IOError:
    print('Error reading file')



# find and break apart according to newline characters
lines = filestr.split('\n')

print(lines)
print ('Number of lines:', len(lines))

#def 

fields = lines.split(':')
print(fields)
print ('Number of fields:', len(fields))

#take [0] element
#usernames
