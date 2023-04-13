# This is a sample Python script.
import math

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import random
import string

def listToMx(keyboardList):
    keyboardMx = []
    for i in range (0,4):
        keyboardMx.append(keyboardList[i*10:((i+1)*10)])
    return keyboardMx

def mxToList(keyboardMx):
    keyboardList = []
    for y in range(0,4):
        for x in range(0,10):
            keyboardList.append(keyboardMx[y][x])
    return keyboardList

def breedKeyboards(keyboard1,keyboard2):
    keyboard1Mx = listToMx(keyboard1)
    keyboard2Mx = listToMx(keyboard2)
    print(keyboard1Mx)
    keyBoardRMx = []
    line = []
    for y in range(0,4):
        for x in range(0,10):
            if(x<5):
                line.append(keyboard1Mx[y][x])
            else:
                line.append("#")
        keyBoardRMx.append(line.copy())
        line.clear()
    print(keyBoardRMx)
    currentX = 5
    currentY = 0
    x = 5
    y = 0
    nbUnderscore = list.count(mxToList(keyBoardRMx),'_')
    print('#' in mxToList(keyBoardRMx))
    while('#' in mxToList(keyBoardRMx)):
        if((not((keyboard2Mx[y][x]) in (mxToList(keyBoardRMx))))or((keyboard2Mx[y][x])=='_')and(nbUnderscore<=14)):
            if((keyboard2Mx[y][x])=='_'):
                nbUnderscore+=1
            keyBoardRMx[currentY][currentX] = keyboard2Mx[y][x]
            currentY+=1
            if(currentY>=4):
                currentX+=1
                currentY=0
            printKeyBoard(mxToList(keyBoardRMx))
            print(nbUnderscore)
        y+=1
        if(y>=4):
            y=0
            x+=1
        if(x>=10):
            x=0
    return keyBoardRMx







def find_letter_pos(keyboard,letter):
    return keyboard.index(letter)

def distanceBetweenLetters(keyboard, letter1, letter2):
    pos1 = find_letter_pos(keyboard,letter1)
    pos2 = find_letter_pos(keyboard,letter2)
    verticalDiff = abs(pos1//10 - pos2//10)
    horizontalDiff = abs(pos1%10 - pos2%10)
    return math.sqrt(verticalDiff*verticalDiff + horizontalDiff*horizontalDiff)

def getCorrespondance(correspondanceMx,letter1, letter2):
    return correspondanceMx[ord(letter1)-65][ord(letter2)-65]

#Optimisation potentielle en ne faisant que la moitié
def calculateFitScore(correspondanceMx, keyboard):
    keyboardFitScore = 0
    for key in keyboard:
        if(key!="_"):
            for letter in string.ascii_uppercase:
                distance = distanceBetweenLetters(keyboard,key,letter)
                correspondance = getCorrespondance(correspondanceMx,key,letter)
                letterFitScore = (11-distance)*correspondance
                keyboardFitScore += letterFitScore
    return (round(keyboardFitScore/100))

def printKeyBoard(keyboard):
    if(len(keyboard)<40):
        for letter in keyboard:
            print(letter, end = '')
        print("")
    for x in range(0,4):
        for y in range(0,10):
            print(keyboard[x*10+y],end = '')
        print("")

def generateRandoKeyboard():
    listeLetters = list(string.ascii_uppercase)
    print(listeLetters)
    random.shuffle(listeLetters)
    print(listeLetters)
    for i in range(0,14):
        pos = random.randint(0,len(listeLetters))
        listeLetters.insert(pos,"_")
    return listeLetters



def print_hi(name):
    np.set_printoptions(suppress=True)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    CSVData = open("correspondance.csv")
    crspsLetersMx = np.loadtxt(CSVData, delimiter=",")
    keyboard = generateRandoKeyboard()
    #keyboard = list("AZERTYUIOPQSDFGHJKLMWXCVBN______________")
    #keyboard = list("___PYFGCRLAOEUIDHTNSQJKXBMWVZ___________")
    printKeyBoard(keyboard)
    print(calculateFitScore(crspsLetersMx, keyboard))
    #keyboard = list("___ANBRCEDVFOGUHYITJZKLMPQSWX___________")
    printKeyBoard(keyboard)
    print(calculateFitScore(crspsLetersMx, keyboard))
    printKeyBoard(mxToList(breedKeyboards(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ______________"),keyboard)))
    print("----------------------------------")
    printKeyBoard("ABCDEFGHIJKLMNOPQRSTUVWXYZ______________")
    printKeyBoard(keyboard)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
