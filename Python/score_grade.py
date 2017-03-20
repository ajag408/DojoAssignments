import random
import math
def scoregenerator():
    scores = []
    while len(scores)<10:
        random_num = math.floor(random.random() * 100)
        if random_num>=60:
            scores.append(random_num)
    return scores


x = scoregenerator()
print x

def grade_machine(scores):
    output = "Scores and Grades"
    for score in scores:
        if score<50:
           output += "\nScore: " + str(score) +"; Your grade is F"
        elif score>=60 and score <70:
           output += "\nScore: " + str(score) +"; Your grade is D"
        elif score>=70 and score<80:
            output += "\nScore: " + str(score) +"; Your grade is C"
        elif score>=80 and score<90:
            output += "\nScore: " + str(score) +"; Your grade is B"
        elif score>=90 and score<=100:
            output += "\nScore: " + str(score) +"; Your grade is A"
    output+= "\nEnd of the program. Bye!"
    return output

y = grade_machine(x)
print y
