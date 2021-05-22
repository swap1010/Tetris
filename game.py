import numpy as np

letters = {
    "I": np.array([[4, 14, 24, 34], [3, 4, 5, 6]]),
    "S": np.array([[5, 4, 14, 13], [4, 14, 15, 25]]),
    "Z": np.array([[4, 5, 15, 16], [5, 15, 14, 24]]),
    "L": np.array([[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]),
    "J": np.array([[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]),
    "O": np.array([[4, 14, 15, 5]]),
    "T": np.array([[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]])
}


def check_filled_row():
    indexes = []
    ndgird = new_state.reshape((col, row))
    for n, rows in enumerate(ndgird):
        if all(rows == 0):
            indexes.append(n)
    return indexes


def print_grid(place=None, flagBreak=False):
    if place is None:
        place = []
    global board_state, new_state
    grid = np.array([1] * (row * col))
    np.put(grid, place, [0], mode='clip')
    if any(place) and place.max() < row*col and all(board_state[place]):
        new_state = np.multiply(grid, board_state)
    idxs = check_filled_row()
    if idxs and flagBreak:
        new_state = np.delete(new_state.reshape(col, row), idxs, 0).reshape(1,-1)
        cnt = len(idxs)
        one = [1] * cnt * row
        new_state = np.insert(new_state, 0, one)
    for i in range(0, len(new_state), row):
        print(" ".join(map(lambda x: "-" if x == 1 else '0', new_state[i:i + row])))
    print()
    if any(place) and not place.max() < (row - 1) * col:
        board_state = new_state


row, col = map(int, input().split())
board_state = np.array([1] * (row * col))
new_state = np.array([1] * (row * col))
print_grid()


def checkGameOver():
    ndgird = new_state.reshape((col, row))
    for column in ndgird.T:
        if all(column == 0):
            print("Game Over!")
            exit()
    return False


flag = 0
while True:
    command = input("").lower()
    if flag:
        level = letter[rotation % (len(letter))].max()
    flag = 1
    if command == 'exit':
        exit()
    elif command == 'piece':
        board_state = new_state
        letter = letters[input("").strip().upper()].copy()
        print_grid(letter[0])
        rotation = 0
        continue
    elif command == "break":
        print_grid(flagBreak=True)
        continue
    elif not level < (row - 1) * col:
        print_grid()
        continue
    elif command == 'rotate':
        rotation += 1
    elif command == 'left':
        if all(letter[rotation % (len(letter))] % row > 0):
            letter[rotation % (len(letter))] -= 1
    elif command == 'right':
        if level + 1 % col > 0:
            letter[rotation % (len(letter))] += 1
    letter += row
    print_grid(letter[rotation % (len(letter))])
    level = letter[rotation % (len(letter))].max()
    checkGameOver()
