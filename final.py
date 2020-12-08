import random
from helpers import *

def main():
    playing = True
    gameResults = open("Fortunes.txt", "w")
    count = 0
    while(playing):
        count += 1
        fortunes = []
        fortuneList = fortuneGetter(fortunes)
        finalFortune = fortuneForGame(fortuneList)
        option = fortunePicker(finalFortune)
        userQuestion = input("Ask a yes or no question: ")
        future = finalFortune[int(option)]
        print(future)
        stillPlaying = validateUserString("Quit or Try Again?", ["Quit", "Try Again"], False).lower()

        if(stillPlaying == "quit"):
            playing = False
        
        fortuneWriter(userQuestion, future, gameResults, count)
    gameResults.close()
    gameResults = open("Fortunes.txt", "r")
    fortunePrinter(gameResults)
    gameResults.close()

def fortuneWriter(question, fortune, fortuneFile, count):
    if("." in question):
        question = question.replace(".", "") # Used this URL for assistance - https://stackoverflow.com/questions/14750942/replacing-periods-in-a-string
    if("?" in question):
        fortuneFile.write("Question " + str(count) + ": " + question + "\n")
    else:
        fortuneFile.write("Question " + str(count) + ": " + question + "?" + "\n")

    fortuneFile.write("Fortune: " + fortune + "\n")
    
def fortunePrinter(file):
    for line in file:
        print(line)

def fortuneGetter(fortunes):
    with open("magic8.txt", "r") as magic8:
        for line in magic8:
            fortunes.append(line.strip())
    return fortunes

def fortuneForGame(fortuneList):
    randomFortunes = {}
    count = 9
    for i in range(1, count):
        randoFortune = random.randint(0, len(fortuneList) - 1)
        randomFortunes.update({i: fortuneList[randoFortune]})
        fortuneList.pop(randoFortune)
    return randomFortunes

def fortunePicker(finalFortune):
    oddNo = ["1", "3", "4", "8"]
    evenNo = ["2", "5", "6", "7"]
    userChoice = validateUserString("Pick one.", ["Clover", "Rainbow", "Unicorn", "Star"])
    for letter in userChoice:
        print(letter.upper())
    if(len(userChoice) % 2 == 0):
        userChoice2 = validateUserString("Pick one.", evenNo)
        if(int(userChoice2) == 2):
            for i in range(1, 3):
                print(i)
            userChoice3 = validateUserString("Pick one.", evenNo)
            return userChoice3
        if(int(userChoice2) == 5):
            for i in range(1, 6):
                print(i)
            userChoice3 = validateUserString("Pick one.", oddNo)
            return userChoice3
        if(int(userChoice2) == 6):
            for i in range(1, 7):
                print(i)
            userChoice3 = validateUserString("Pick one.", evenNo)
            return userChoice3
        if(int(userChoice2) == 7):
            for i in range(1, 8):
                print(i)
            userChoice3 = validateUserString("Pick one.", oddNo)
            return userChoice3
    else:
        userChoice2 = validateUserString("Pick one.", oddNo)
        if(int(userChoice2) == 1):
            for i in range(1, 2):
                print(i)
            userChoice3 = validateUserString("Pick one.", evenNo)
            return userChoice3
        if(int(userChoice2) == 3):
            for i in range(1, 4):
                print(i)
            userChoice3 = validateUserString("Pick one.", evenNo)
            return userChoice3
        if(int(userChoice2) == 4):
            for i in range(1, 5):
                print(i)
            userChoice3 = validateUserString("Pick one.", oddNo)
            return userChoice3
        if(int(userChoice2) == 8):
            for i in range(1, 9):
                print(i)
            userChoice3 = validateUserString("Pick one.", oddNo)
            return userChoice3

main()