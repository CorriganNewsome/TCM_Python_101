try:
    f = open('aal;ksdsal;dk')
except FileNotFoundError:
    print('file does not exist')
except Exception as e:
    print(e)
finally:
    print('this message')