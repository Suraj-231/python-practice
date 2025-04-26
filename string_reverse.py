string= input('enter a string: ')
reversed_string= ''
for i in range(len(string) -1,-1,-1):
    reversed_string += string[i]
print('reversed string: ',reversed_string)