
def score_calculate():
    score = int(input("Please enter your score: "))
    if score >= 90 and score <= 100:
        print("Your grade is A")
    elif score >= 70 and score <= 89:
        print("Your grade is B")
    elif score >= 60 and score <= 69:
        print("Your grade is C")
    elif score >= 0 and score <= 59:
        print("Your grade is D")
    else:
        print("Invalid Score")

try:
    score_calculate()
except:
    print("invalid input")








