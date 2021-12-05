from io import StringIO
import csv
import numpy as np
with open('bingo.txt', 'r') as file:
    # reading each line
    boardList = []
    tmpNumbersList = []
    numbersList = []
    tmpRow = []
    tmpBoard = []
    rowCounter = 0
    colCounter = 0
    for line in file:
        for word in line.split():
            #print(word)

            if len(word)>20:
                f = StringIO(word)
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    tmpNumbersList.append(row)
                    #print('\t'.join(row))
            else:
                tmpRow.append(int(word))
                colCounter += 1
                if colCounter == 5:
                    tmpBoard.append(tmpRow)
                    tmpRow = []
                    colCounter = 0
                    rowCounter += 1
                if rowCounter == 5:
                    boardList.append(tmpBoard)
                    tmpBoard = []
                    rowCounter = 0
                #print(word)
    for j in range(len(tmpNumbersList[0])):
        numbersList.append(int(tmpNumbersList[0][j]))
    #print(np.sum(boardList[0],-1))
drawnNumbers = []
counter = 0
tmpBoard = np.zeros((5,5))
win = False
winningBoardList = []
winCounter = 0
for num in numbersList:
    if win:
        break
    drawnNumbers.append(numbersList[counter])
    if counter>=5:
        for board in boardList:
            for i in range(5):
                if win:
                    break
                c = 0
                r = 0
                winningNumbers = []
                winningNumbers2 = []
                for j in range(5):
                    #print(board[i][j])
                    check = any(item in [board[i][j]] for item in drawnNumbers)
                    check2 = any(item in drawnNumbers for item in [board[j][i]])
                    if check:
                        winningNumbers.append([board[i][j]])
                        r += 1
                    if check2:
                        c += 1
                        winningNumbers2.append([board[j][i]])

                    if r == 5 or c == 5:
                        winningBoard = board
                        if board not in winningBoardList:
                            winningBoardList.append(board)
                            winCounter += 1
                            if winCounter==100:
                                win = True
                                break

    counter += 1
print(winCounter)

print(winningBoardList[-1])
lastNumber = drawnNumbers[counter-1]
print(lastNumber)
#print(winningNumbers2)
#print(drawnNumbers)
winningBoard = np.array(winningBoardList[-1])
#print(winningBoard)
#print(np.sum(winningBoard))
unmarkedSum = 0
for k in range(5):
    for y in range(5):
        for it in drawnNumbers:
            winningBoard[k][y] = np.where(winningBoard[k][y]==it,0,winningBoard[k][y])
print(np.sum(winningBoard)*lastNumber)



