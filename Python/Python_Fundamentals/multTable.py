firstRowStr = 'x'
for x in range(1,13):
    firstRowStr = firstRowStr + " " + str(x)
print firstRowStr

for y in range(1, 13):
    mainStr = str(y)
    for i in range(1,13):
        mainStr = mainStr + " " + str(y * i)
    print mainStr
