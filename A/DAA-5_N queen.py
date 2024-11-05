global N 
N = int(input("Enter No. Of Queens : "))

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()  # Add an extra line for better separation between solutions

def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
            
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if i >= 0 and j >= 0 and board[i][j] == 1:
            return False
            
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if i < N and j >= 0 and board[i][j] == 1:
            return False
            
    return True

def solveNQUntil(board, col, solutions):
    if col >= N:
        solutions.append([row[:] for row in board])  # Add a copy of the current board to solutions
        return
    
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place a queen
            solveNQUntil(board, col + 1, solutions)  # Recur to place rest of the queens
            board[i][col] = 0  # Backtrack

def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []  # List to hold all solutions
    
    solveNQUntil(board, 0, solutions)  # Start solving from the first column
    
    if not solutions:
        print("Solution does not exist")
    else:
        for solution in solutions:
            printSolution(solution)  # Print each solution

if __name__ == '__main__':
    solveNQ()
