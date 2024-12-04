def exist(board, word):
    def backtrack(i, j, idx):
        # Base Case: If all characters are matched
        if idx == len(word):
            return True
        
        # Boundary and constraint check
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        
        # Mark the cell as visited (temporary modification)
        temp = board[i][j]
        board[i][j] = "#"
        
        # Explore all 4 directions
        for di, dj in directions:
            if backtrack(i + di, j + dj, idx + 1):
                return True
        
        # Backtrack: Unmark the cell
        board[i][j] = temp
        return False

    # Direction vectors: Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Start the search from each cell
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and backtrack(i, j, 0):
                return True
    
    return False

# Test
board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))  # Output: True
