my_list = ['magical','unicorns']
string = "String:"
runningSum = 0
stringCt = 0
intCt = 0
for el in my_list:
    if isinstance(el, str) == True:
        string = string + " " + el
        stringCt = stringCt + 1
    else:
        runningSum = runningSum + el
        intCt = intCt + 1

if intCt != 0 or stringCt != 0:
    if intCt != 0 and stringCt != 0:
        print string
        print runningSum
        print 'mixed'
    else:
        if intCt == 0:
            print string
            print "string"
        if stringCt == 0:
            print runningSum
            print "int"
else:
    print "No list entered"
