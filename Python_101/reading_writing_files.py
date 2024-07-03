f = open('/home/anubis/Desktop/Tech/test.txt', 'rt')
print(f.readlines())

f.seek(0)
print('----for loop---')
for line in f:
    print(line.strip())
    
f.close()

f = open('/home/anubis/Desktop/Tech/test01.txt', 'w')
f.write('test line\ntest line two\n')
f.close()