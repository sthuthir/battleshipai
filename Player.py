import random

def getMoveCount(board):
    moves = 0
    for row in range(0, 10):
        for col in range(0, 10):
            if board[row][col] == 'X' or board[row][col] == '*':
                moves += 1
    return moves

def getNumHits(board):
    hits = 0
    for row in range(0, 10):
        for col in range(0, 10):
            if board[row][col] == 'X':
                hits += 1
    return hits

def check(board, row, col, direction):
    if direction == 'Up':
        return board[max(row - 1, 0)][col]
    if direction == 'Down':
        return board[min(row + 1, 9)][col]
    if direction == 'Left':
        return board[row][max(col - 1, 0)]
    if direction == 'Right':
        return board[row][min(col + 1, 9)]
    
def makeMove(board):
    probabilities = calculateProbabilities(board)
    sorted_positions = sortProbabilities(probabilities)

    # Iterate through sorted positions to find the first valid move
    for position in sorted_positions:
        row, col = position
        if isValid(row, col, board):
            return [row + 1, col + 1]

def calculateProbabilities(board):
    probabilities = [[0] * 10 for _ in range(10)]

    for row in range(10):
        for col in range(10):
            if board[row][col] == 'X' or board[row][col] == '*':
                continue

            # Calculate probability based on neighboring hits
            for i in range(max(0, row - 1), min(10, row + 2)):
                for j in range(max(0, col - 1), min(10, col + 2)):
                    if board[i][j] == 'X':
                        probabilities[row][col] += 1

    return probabilities

def sortProbabilities(probabilities):
    flattened = [(row, col) for row in range(10) for col in range(10)]
    sorted_positions = sorted(flattened, key=lambda pos: probabilities[pos[0]][pos[1]], reverse=True)
    return sorted_positions

def isValid(row, col, board):
    return 0 <= row < 10 and 0 <= col < 10 and board[row][col] not in ('X', '*')

# Example usage:
# move = makeMove(board)
# print("AI Move:", move)

