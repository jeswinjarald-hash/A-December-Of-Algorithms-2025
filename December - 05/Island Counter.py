def dfs(grid, i, j, rows, cols):
    # Check boundaries and water
    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
        return

    # Mark land as visited
    grid[i][j] = 0

    # Visit all 4 directions
    dfs(grid, i + 1, j, rows, cols)
    dfs(grid, i - 1, j, rows, cols)
    dfs(grid, i, j + 1, rows, cols)
    dfs(grid, i, j - 1, rows, cols)


def countIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
                dfs(grid, i, j, rows, cols)

    return count


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the grid row by row (0s and 1s separated by space):")
grid = []

for _ in range(rows):
    grid.append(list(map(int, input().split())))

islands = countIslands(grid)
print("Number of islands:", islands)
