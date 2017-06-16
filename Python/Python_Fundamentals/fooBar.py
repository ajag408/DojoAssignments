for i in range(100, 100001):
    prime = True
    perfect = False
    for j in range(2, i/2 + 1):
        if i%j == 0:
            prime = False
        if j*j == i:
            perfect = True
    if prime == True:
        print "foo"
    if perfect == True:
        print "bar"
    if prime == False and perfect == False:
        print "FooBar"
