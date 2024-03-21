# Labyrinth - Finding Path
def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    rows = len(lab)
    columns = len(lab[0])

    # Prints the top row with column numbers
    top_row = " " + "".join([str(i % 10) for i in range(columns)]) + " "
    print(top_row)

    for i in range(rows):
        row = str(i)
        for j in range(columns):
            if path is not None and (i, j) in path:
                row += "X"  # Replace spaces on the path with "X"
            else:
                row += lab[i][j]
        row += str(i)
        print(row)

    # Prints the bottom row with column numbers
    bottom_row = " " + "".join([str(i % 10) for i in range(columns)]) + " "
    print(bottom_row)


def replace_at_index(s, r, idx):
    return s[:idx] + r + s[idx + len(r):]


labyrinth = [
    "███████",
    "█     █",
    "█   ███",
    "█ ███ █",
    "█     █",
    "███████",
]

print_labyrinth(labyrinth)


def prompt_integer(message: str) -> int:
    while True:
        users_number = input(message)
        if users_number.isdigit():
            return int(users_number)
        else:
            print("Invalid input. Please enter a valid integer.")


def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    row, col = location
    if 0 <= row < len(lab) and 0 <= col < len(lab[0]) and lab[row][col] == ' ':
        return True
    return False


def prompt_user_for_location(name: str, lab: list[str]) -> tuple[int, int]:
    while True:
        row = prompt_integer(f"Row of {name}: ")
        column = prompt_integer(f"Column of {name}: ")
        location = (row, column)
        if is_traversable(lab, location):
            return location
        else:
            print("Invalid input. Please choose a valid location within the labyrinth's boundaries and not '█'.")


start = prompt_user_for_location("start", labyrinth)
end = prompt_user_for_location("end", labyrinth)

print("Start location:", start)
print("End location:", end)


from collections import deque


def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque()
    queue.append([start])  # Start with a path containing only the start location
    visited = set()

    # Define the possible moves (up, down, left, right)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        path = queue.popleft()  # Dequeue the first path
        last = path[-1]  # Get the last location in the path

        if last == end:
            return path  # If we reached the end location, return the path

        if last not in visited:
            visited.add(last)

            for move in moves:
                next_location = (last[0] + move[0], last[1] + move[1])

                if is_traversable(lab, next_location):
                    new_path = path.copy()
                    new_path.append(next_location)
                    queue.append(new_path)

    return []  # If no path is found, return an empty list


path = bfs(labyrinth, start, end)
if path:
    print("Path from start to end:")
    for location in path:
        print(location)
else:
    print("No path found.")


print_labyrinth(labyrinth, path)  # Displays the labyrinth with the path

# TO DO:
# 1 Create restrictions for users input (if it makes sense) (DONE)
# Try new labyrinth (DONE)

"""
labyrinth = [
 "████████",
 "█      █",
 "█   ██ █",
 "█ █ ██ █",
 "█  █   █",
 "████████",
]
"""
