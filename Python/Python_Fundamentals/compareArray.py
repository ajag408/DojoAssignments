list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
ditto = False
if len(list_one) == len(list_two):
    for idx, val in enumerate(list_one):
        if val == list_two[idx]:
            ditto = True
            continue
        else:
            ditto = False
            break

if ditto == True:
    print "The lists are the same"
else:
    print "The lists are not the same"
