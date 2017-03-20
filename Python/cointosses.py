import random
def cointosser():
    headcounter = 0
    tailcounter = 0
    output = "Starting the program..."
    for count in range (1,5001):
        random_num = random.random()
        rounded = round(random_num)
        if rounded == 0:
            outcome = "head"
            headcounter = headcounter + 1
        if rounded == 1:
            outcome = "tail"
            tailcounter = tailcounter + 1
        output += "\nAttempt #" + str(count) + ": Throwing a coin...It's a " + outcome + "!...Got " + str(headcounter) + " head(s) so far and " + str(tailcounter) + " tail(s) so far"
    output += "\nEnding the program, thank you!"
    print output

cointosser()
