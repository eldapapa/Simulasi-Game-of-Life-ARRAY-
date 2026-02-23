import random
import time
import os

# Membersihkan layar terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Membuat grid awal secara acak
def create_grid(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Menampilkan grid
def print_grid(grid):
    for row in grid:
        for cell in row:
            print("■" if cell == 1 else ".", end=" ")
        print()
    print()

# Menghitung jumlah tetangga hidup
def count_neighbors(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    total = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            nx = (x + i) % rows
            ny = (y + j) % cols
            total += grid[nx][ny]

    return total

# Membuat generasi berikutnya
def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1

    return new_grid

# Program utama
def main():
    rows = 20
    cols = 40
    generations = 50

    grid = create_grid(rows, cols)

    for gen in range(generations):
        clear_screen()
        print(f"Generasi: {gen+1}")
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.3)

if __name__ == "__main__":
    main()