from logging import exception


a=10
b=2
try :
    if b>a :
     print(a)
    else :
     print('a is greterthan b')
except exception as f :
    print(f)
finally:
    print('completed')    