#this was made by Akash Jagannathan and Leila Adel
def draw_stars(a):

    for index in a:
        c = None
        emptystring = ""
        output = ""
        num = 0
        if type(index) == type(emptystring):
            first_letter = index[0]
            indexlength = len(index)
            output = first_letter * indexlength
        print output
        if type(index) == type(num):
            for count in range(1, index+1):
                c = "*"*count
            print c
x = draw_stars([4, "bob", "joey", "rick", "jerryyyy", 3])
