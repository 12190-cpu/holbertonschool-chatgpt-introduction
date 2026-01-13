#!/usr/bin/python3
def print_board(board):
    """Affiche le plateau du jeu."""
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(f"{i} " + " | ".join(row))
        if i < 2:
            print("  " + "-" * 9)
    print()

def check_winner(board):
    """Vérifie si un joueur a gagné."""
    # Lignes
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Vérifie si le plateau est plein."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Boucle principale du jeu Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]
    play

