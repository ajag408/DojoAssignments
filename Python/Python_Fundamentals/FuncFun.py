def odd_even():                                 #code block of odd/even
    for int in range(1, 2001):
        if(int%2!=0):
            print "Number is " + str(int) + ".  This is an odd number."
        if(int%2 == 0):
            print "Number is " + str(int)+ ".  This is an even number."

odd_even()


def multiply(list, x):          #multiply
    newlist = []
    for element in list:
        element = element*x
        newlist.append(element)
    return newlist

a = multiply([2,4,10,16], 5)
print a

def layered_multiples(arr):             #Hacker Challenge
    wtf = []
    for val in arr:
        wtf2 = []
        for rawnummult in range(1, val+1):
            wtf2.append(1)
        wtf.append(wtf2)
    return wtf

pmf = layered_multiples(multiply([2,4,5],2))
print pmf
