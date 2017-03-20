for count in range(1,1000):        #Multiples part 1
    if(count%2 != 0):
        print count

for var1 in range(5, 1000001):      #Multiples part 2
    if(var1%5==0):
        print var1


a = [1, 2, 5, 10, 255, 3]       #Sum List
sum1=0
for num in a:
    sum1 = sum1 + num
print sum1

a = [1, 2, 5, 10, 255, 3]       #Average List
sum2=0
for bum in a:
    sum2= sum2+bum
avg = sum2/len(a)
print avg
