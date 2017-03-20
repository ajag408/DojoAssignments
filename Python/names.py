students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def nameSorter(arr):
    count = 0
    for item in students:
        for key in item:
            count = count + 1
            if count%2 == 0:
                print item.get('first_name') + " " + item.get('last_name')


nameSorter(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def haiku(marrian):
    for key,data in users.iteritems():
        print key
        count = 0
        for item in data:
            for pros, cons in item.iteritems():
                count = count + 1
                index = count/2
                if count%2 == 0:
                    conman = len(item.get('first_name')) + len(item.get('last_name'))
                    print str(index) + " - " + item.get('first_name').upper() + " " + item.get('last_name').upper() + " - " + str(conman)

haiku(users)
