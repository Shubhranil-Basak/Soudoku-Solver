import tkinter as tk

def is_valid(board, row, col, num):
    #for row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    #for 3x3 square
    p_r = 3*(row//3)
    p_c = 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[p_r + i][p_c + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num #assigning the num as it is correct for the time being
                        if solve(board): #trying to solve the entire board using this recursing to check if the 'num' placed is correct or not
                            return True  #if num is corret, we return True
                        board[row][col] = 0 # else, reset it to 0
                return False
    return True

def solve_sudoku(entries, status_label):
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            if value.isdigit():
                board[i][j] = int(value)

    if solve(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
        status_label.config(text="Sudoku solved!")
    else:
        status_label.config(text="No solution exists for this puzzle")

def main():
    root = tk.Tk()
    root.title("Sudoku Solver")

    global entries  # Declare entries as a global variable
    entries = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            entries[i][j] = tk.Entry(root, width=3)
            entries[i][j].grid(row=i, column=j)

    solve_button = tk.Button(root, text="Solve", command=lambda: solve_sudoku(entries, status_label))
    solve_button.grid(row=9, columnspan=9)

    status_label = tk.Label(root, text="")
    status_label.grid(row=10, columnspan=9)

    root.mainloop()

if __name__ == "__main__":
    main()