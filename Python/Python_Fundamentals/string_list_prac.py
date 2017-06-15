
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')

newstr = words.replace(' day', ' month')
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
length = len(a)
half = len(a)/2
b = a[0:half]
c = a[half:length]
c.insert(0,b)
print c
