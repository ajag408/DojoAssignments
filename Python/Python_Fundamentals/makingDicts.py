def make_dict(arr1, arr2):
    if(len(arr1) == len(arr2) or len(arr1)>len(arr2)):
        zippedLists = zip(arr1, arr2)
    else:
        zippedLists = zip(arr2, arr1)
    new_dict = dict(zippedLists)
    return new_dict




# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
#
# test = make_dict(name, favorite_animal)
# print test
