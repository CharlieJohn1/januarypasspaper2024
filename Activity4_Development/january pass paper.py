def intChecker(integer):
    try:
        int(integer)
    except ValueError:
        return False
    else:
        return True
def validator(integer, high, low):
    try:
        int(integer)
    except ValueError:
        return False
    else:
        if int(integer) > high or int(integer) < low:
            return False
        else:
            return True
totalMinutesPlayed = 0
highScore = 0
playerID = input('Please input the players ID: ')
gamesPlayed = input('Please input the number of games played: ')
gamesPlayedV = validator(gamesPlayed, 10, 5)
while gamesPlayedV == False:
    if intChecker(gamesPlayed) == False:
        print('Error! Please input a number.')
    else:
        if int(gamesPlayed) < 5:
            print('Error! Please input a number above 5. ')
        elif int(gamesPlayed) > 10:
            print('Error! Please input a number below 10. ')
    gamesPlayed = input('Please input the number of games played: ')
    gamesPlayedV = validator(gamesPlayed, 10, 5)
gamesPlayedV = int(gamesPlayed)
for i in range(gamesPlayedV):
    score = input('Please input the score: ')
    scoreV = intChecker(score)
    while scoreV == False:
        print('Error! Pleases input a number.')
        score = input('Please input the score: ')
        scoreV = intChecker(score)
    scoreV = int(score)
    minutesPlayed = input('Please input the amount of minutes played: ')
    minutesPlayedV = validator(minutesPlayed, 60, 5)
    while minutesPlayedV == False:
        if intChecker(minutesPlayed) == False:
            print('Error! Please input a number.')
        else:
            if int(minutesPlayed) < 5:
                print('Error! Please input a number above 5. ')
            elif int(minutesPlayed) > 60:
                print('Error! Please input a number below 60. ')
        minutesPlayed = input('Please input the amount of minutes played: ')
        minutesPlayedV = validator(minutesPlayed, 60, 5)
    minutesPlayedV = int(minutesPlayed)
    if scoreV > highScore:
        highScore = scoreV
    totalMinutesPlayed += minutesPlayedV
    i += 1
averageTime = totalMinutesPlayed / gamesPlayedV
print('Player ID: '+ playerID + '.')
print('High Score: ' + str(highScore) + '.')
print('Average Time: ' + str(averageTime) + '.')
