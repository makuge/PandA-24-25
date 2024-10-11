def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):

    def replace_at_index(s: str, r: str, idx: int) -> str:
        return s[:idx] + r + s[idx + len(r):]

    n_columns = len(lab[0])
    numbers = " " + "".join([str(i % 10) for i in range(n_columns)])

    print(numbers)
    for i, row in enumerate(lab):
        if path:
            for item in path:
                if item[0] == i:
                    row = replace_at_index(row, "X", item[1])

        print(f"{i %10}{row}{i % 10}")

    print(numbers)

def prompt_integer(message: str) -> int:
    text = input(message)

    while not text.isdigit():
        print("Only integers accepted!")
        text = input(message)

    return int(text)

def prompt_user_for_location(name: str) -> tuple[int, int]:
    row = prompt_integer(f"Row of {name} location: ")
    column = prompt_integer(f"Column of {name} location: ")
    return row, column

# BFS function to traverse a graph
def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    # ... your implementation here...
    path = [(1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10)]
    return path


# Labyrinth represented as a list of strings
labyrinth = [
    "█████████████",
    "█           █",
    "█ █████ █████",
    "█ █   █     █",
    "█ ███ █ █████",
    "█     █     █",
    "█████████████"
]


print_labyrinth(labyrinth)

start_location = prompt_user_for_location("start")
end_location = prompt_user_for_location("end")

# Find path using breadth-first search between start and end locations
path = bfs(labyrinth, start_location, end_location)

print_labyrinth(labyrinth, path)




