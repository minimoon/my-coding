## Problem 1 ##
# try:
#     for i in ['a','b','c']:
#         print i**2
# except:
#     print 'there is an error!'

## Problem 2 ##
# x = 5
# y = 0

# try:
#     z = x/y
# except:
#     print 'error'
# finally:
#     print "let's try!"


def ask():
    while True:
        try:
            f = int(raw_input('Enter interger: '))
            print f
        except:
            print 'there is an error'
            continue
        else:
            print 'you can do it'
            break
        finally:
            print "that's all"
    print f
    



ask()
