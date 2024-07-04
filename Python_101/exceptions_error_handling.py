try:
    f = open('aal;ksdsal;dk')
except FileNotFoundError:
    print('file does not exist')
except Exception as e:
    print(e)
finally:
    print('this message')
    
    n = 100
    if n == 0:
        raise Exception ("n can't be 0!")
    if type(n) is not int:
        raise Exception("n must be an int!")
    
print(1/n)

n = 0
assert(n != 0)
print(1/n)