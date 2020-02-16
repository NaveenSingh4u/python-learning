f = open('abc.txt', 'w')
f.write('I ')
f.write('am ')
f.write('the best..always ')
f.close()
print('Write Operation completed..')

# The above lines will get printed in the given file.

# Following lines will get printed whenever we will run code.
f = open('a_txt_mode', 'a')
f.write('I ')
f.write('am ')
f.write('the best..always \n')
f.close()
print('Write Operation completed..by appending mode..')


# Writing file from tuples
f = open('abc.txt', 'w')
l = {'Sunnny\n', 'Bunny\n', 'Chinny\n'}
f.writelines(l)
f.close()
print('Write operation completed from tuples..')