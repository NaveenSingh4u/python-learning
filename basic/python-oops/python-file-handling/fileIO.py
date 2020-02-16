# Store are mainly of two type.
# Temporary and permanent
# Temporary : List, Tuple, Dict.(Storage inside PVM - Python virtual machine)
# Permanent : Files and Database.

# Files : For short amount of data.
# Database : For huge amount and relational data.

# Files : text files and Binary files.
# 1. Text data : name of students or any details.
# 2. Binary Files : image, video files, audio files.

# Read/Write... Opening of that file.
# open(filname, mode)

# to open abc.txt file for write operation
#f = open('abc.txt', 'w')

# The allowed modes in Python
#-----------------------------------------
# 1. r : Read
# Open the existing file for read operation.
# if the specified file not available then we will get FileNotFoundError.
# Note : the default mode is read mode in python
#f = open('abc.txt', 'r')
# f = open('abc.txt') is equivalent to f = open('abc.txt', 'r')


# 2. w : Write
# For write operation
f = open('abc.txt', 'w')
#Note : Open the file abc.txt file for write operation
# If the specified file not found then this line will automatically create that file.
# If the file already contains some data it will perform overwrite operation.

# 3. a : Append
f = open('abc.txt', 'a')
# If the file already contains some data it will not perform overwrite operation, It will just add.

# 4. r+ : Read and write --> To read and then write

# 5. w+ : Write and then read
# To write and then read. It will overwrite existing data.

# 6. a+ : Append and then read
# First append and then read. It will not overwrite existing data.

# 7. x : Exclusive.
# It is for write operation.
# f = open('abc.txt', 'x')
# File may or may not exist.
# Compulsory file should not be available.
# If file is already available then we'll get FileExistError.

# Note : The above modes are available only for text files.

# For binary files .. Total 22 modes are available.

# f = open('abc.txt', 'r')
# ...Performed required read operation
f.close()

# ---------------------------------
# Various properties of File Object.
# attribute
# f.name
# f.mode
# f.close

# Methods
# f.readable()
# f.writable()

f = open('abc.txt', 'r')
print('File name : ', f.name)
print('File mode : ', f.mode)
print('Is file readable ? : ', f.readable())
print('Is file writeable ? : ', f.writable())
print('Is File closed ? : ', f.close())

f = open('w_.txt_mode', 'w')
print('File name : ', f.name)
print('File mode : ', f.mode)
print('Is file readable ? : ', f.readable())
print('Is file writeable ? : ', f.writable())
print('Is File closed ? : ', f.close())

f = open('a_txt_mode', 'a')
print('File name : ', f.name)
print('File mode : ', f.mode)
print('Is file readable ? : ', f.readable())
print('Is file writeable ? : ', f.writable())
print('Is File closed ? : ', f.close())

f = open('abc.txt', 'r+')
print('File name : ', f.name)
print('File mode : ', f.mode)
print('Is file readable ? : ', f.readable())
print('Is file writeable ? : ', f.writable())
print('Is File closed ? : ', f.close())

f = open('w_plus_mode.txt', 'w+')
print('File name : ', f.name)
print('File mode : ', f.mode)
print('Is file readable ? : ', f.readable())
print('Is file writeable ? : ', f.writable())
print('Is File closed ? : ', f.close())

f = open('a_plus_mode.txt', 'w')
print('File name : ', f.name)
print('File mode : ', f.mode)
print('Is file readable ? : ', f.readable())
print('Is file writeable ? : ', f.writable())
print('Is File closed ? : ', f.close())

f = open('x_mode.txt', 'x')
print('File name : ', f.name)
print('File mode : ', f.mode)
print('Is file readable ? : ', f.readable())
print('Is file writeable ? : ', f.writable())
print('Is File closed ? : ', f.close())

