def function1():
    return "hello from function 2"

output = function1()
print(output)

def function2 (s1, s2):
    print('{}{}'.format(s1,s2))
    
function2('any','thing')
function2(s1='thing', s2='any')