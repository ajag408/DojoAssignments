info = {}
info['name'] = 'Akash'
info['age'] = 25
info['birth_country'] = 'USA'
info['language'] = 'Creole English'

def dictJuicer(dict):
    for key, val in dict.iteritems():
        if key == 'name':
            print "My name is " + val
        elif key == 'age':
            print "My age is " + str(val)
        elif key == 'birth_country':
            print "My country of birth is " + val
        elif key == 'language':
            print "My favorite language is " + val

dictJuicer(info)
