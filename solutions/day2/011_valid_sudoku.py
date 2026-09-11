"""
36 Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Time Complexity: O(1) - Fixed 9x9 board size
Space Complexity: O(1) - Fixed size arrays (9 sets each for rows, cols, boxes)
"""

def isValidSudoku(board):
    """
    Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated 
    according to the following rules:
    
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    
    Args:
        board: List[List[str]] - 9x9 Sudoku board represented as list of lists
        
    Returns:
        bool - True if the board is valid, False otherwise
        
    Note:
        - The input board may be partially filled, where empty cells are filled with '.'
        - A valid Sudoku board (partially filled) is not necessarily solvable
        - Only the filled cells need to be validated
    """
    # Initialize sets to track seen numbers in each row, column, and 3x3 box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            
            # Check if num already exists in current row
            if num in rows[i]:
                return False
            rows[i].add(num)
            
            # Check if num already exists in current column
            if num in cols[j]:
                return False
            cols[j].add(num)
            
            # Calculate which 3x3 box this cell belongs to
            # Box index: (row // 3) * 3 + (col // 3)
            box_index = (i // 3) * 3 + j // 3
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)
    
    return True

# Test the solution
if __name__ == "__main__":
    # Test case 1: Valid Sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print("Test 1 - Valid Sudoku:", isValidSudoku(board1))  # Expected: True
    
    # Test case 2: Invalid Sudoku (duplicate in first row)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print("\nTest 2 - Invalid Sudoku:", isValidSudoku(board2))  # Expected: False
    
    # Test case 3: Empty board
    board3 = [["." for _ in range(9)] for _ in range(9)]
    print("\nTest 3 - Empty board:", isValidSudoku(board3))  # Expected: True