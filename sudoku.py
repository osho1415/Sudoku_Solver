from pprint import pprint 

def is_valid(puzzle,guess,row,col): 

    # checks if the guess made present in the row.
    if guess in puzzle[row]: 
        return False 
    
    # checks if the guess made present in the column.
    for rows in range(9): 
        if guess == puzzle[rows][col]: 
            return False 

    # checks if the guess made present in the box.

    
    row_start = (row // 3) * 3 
    col_start = (col// 3) * 3 

    for b_row in range(row_start, row_start + 3): 
        for b_col in range(col_start, col_start + 3): 
            if guess == puzzle[b_row][b_col]: 
                return False
 
    return True # false if guess in there, else true.

def find_empty(puzzle):
    # checks the puzzle for an empty square (contains -1)
    # returns tuple row, col if an empty square found else returns (None, None)

    for row in range(9): 
        for col in range(9):
            if puzzle[row][col] == -1: 
                return row,col

    return None, None  # if no empty spaces.

def solve_sudoku(puzzle): 
    # solves sudoku puzzle by going through all the spaces
    # and filling them up with entries that don't violate the rules. 

    row, col = find_empty(puzzle)
    # if no empty spaces left, we have solved the puzzle.  
    if row is None :
        return True
    
    # if empty space left, we try and fill it with a guess (1,9)
    for guess in range(1,10): 

        if is_valid(puzzle, guess, row, col): 
            # updating the valid guess in the puzzle.
            puzzle[row][col] = guess

            if solve_sudoku(puzzle): 
                return True 

            # the previous guess doesn't lead to a solution and hence we will choose another guess.   
        puzzle[row][col] = -1

    return False 

def main(): 
    board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],
        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],
        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
     ]

    solve_sudoku(board)
    pprint(board)

if __name__ == "__main__": 
    main() 