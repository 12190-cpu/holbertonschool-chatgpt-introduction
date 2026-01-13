#!/usr/bin/python3
import random
import os
import sys

def clear_screen():
    """Efface l'écran selon le système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Génère des positions de mines aléatoires
        self.mines = set(random.sample(range(width * height), mines))
        # Plateau de jeu et cases révélées
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """Affiche le plateau du jeu."""
        clear_screen()
        print("   " + " ".join(f"{i:2}" for i in range(self.width)))
        print("  " + "-" * (self.width * 3))
        for y in range(self.height):
            print(f"{y:2}|", end=" ")
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print("*", end="  ")
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else " ", end="  ")
                else:
                    print(".", end="  ")
            print()
        print()

    def count_mines_nearby(self, x, y):
        """Compte le nombre de mines autour d'une case donnée."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # ignore la case centrale
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """Révèle la case (x, y). Retourne False si c'est une mine."""
        # Vérifie les limites du plateau
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # ignore les clics hors grille
        # Ignore les cases déjà révélées
        if self.revealed[y][x]:
            return True

        # Si c’est une mine → partie perdue
        if (y * self.width + x) in self.mines:
            return False

        # Révèle la case actuelle
        self.revealed[y][x] = True

        # Si aucune mine autour → révèle automatiquement les voisines
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)

        return True

    def check_victory(self):
        """Vérifie si toutes les cases sans mine sont révélées."""
        total_cells = self.width * self.height
        return sum(sum(row) for row in self.revealed) == total_cells - len(self.mines)

    def play(self):
        """Boucle principale du jeu."""
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of range! Try again.")
                    input("Press Enter to continue...")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\n💣 Game Over! You hit a mine.")
                    break

                if self.check_victory():
                    self.print_board(reveal=True)
                    print("\n🏆 Congratulations! You cleared all the mines!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    game = Minesweeper(width=8, height=8, mines=10)
    game.play()

