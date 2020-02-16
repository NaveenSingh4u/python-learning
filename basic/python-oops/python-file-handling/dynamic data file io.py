# example for creating file and writing on local system

file_name = input('Enter file name: ')
# Here you can change directory name
f = open('/home/naveen'+file_name, 'w')

opinion = input(' Your opinion about python language: ')
f.write(opinion)
f.close()
print('Go and check in your laptop to see written opinion...')

# Note: Permission should be granted for given directory..