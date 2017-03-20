import re
str = "If monkeys like bananas, then I must be a monkey!"
for m in re.finditer('monkey', str):
    print (m.start())

newstr = str.replace("monkey", "alligator")
print newstr

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]
w = []
w.append(y[0])
w.append(y[len(y)-1])
print w

a = [19,2,54,-2,7,12,98,32,10,-3,6]
a.sort()
print a
b = []
b.append(a[:2])
print b
a.remove(-3)
a.remove(-2)
a.insert(0,b)
print a
