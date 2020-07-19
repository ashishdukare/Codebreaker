# GET GUESS
def get_guess():
    return list(str(input("What is your guess?\n")))

# GENERATE COMPUTER CODE 123
import random
def generate_code():
    digits = [str(num) for num in range(10)]

    #subsitute for above line
    #list = []
    #for item in range(10):
        #list.append(item)

    #print(list)

    #Shuffle the digits
    random.shuffle(digits)
    #Then grab the first three
    return digits[:3]

# GENERATE THE CLUES
result = "Code Craccked!\n"
def generate_clues(code, user_guess):
    if user_guess==code:
        return result

    clues = []
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

# RUN GAEME LOGIC
print("Welcome Code Breaker!\n")
secret_code = generate_code()
print("secret_code: ")
print(secret_code)
clue_report = []

while clue_report != result:
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print("here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
