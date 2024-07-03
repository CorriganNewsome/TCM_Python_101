#Need to put in full path to file to open. 
f = open('/home/anubis/Desktop/Tech/test.txt', 'rt')
print(f.readlines())

f.seek(0)#changes file position
print('----for loop---')
for line in f:
    print(line.strip())
    
f.close()

#write mode
f = open('/home/anubis/Desktop/Tech/test01.txt', 'w')
f.write('test line\ntest line two\n')
f.close()

# append mode
f = open('/home/anubis/Desktop/Tech/test01.txt', 'w')
f.write('test line\ntest line two\n')
f.close()