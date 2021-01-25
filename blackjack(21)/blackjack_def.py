import random
deck = [6,7,8,9,10,2,3,4,11]
score_1 = 0
score_2 = 0
def take_card():
    global deck,score_1
    if score_1 > 21:
        score_1 = 0
    number = random.choice(deck)
    print(number)
    score_1 += number
    print(score_1)
    return number
def diler_take_card():
    global deck,score_2,score_1
    number_2 = 0
    if score_2 > 21:
        score_2 =0
    while score_2 <= score_1:
        number_2 = random.choice(deck)
        score_2 += number_2
        print(score_2)
    return score_2

