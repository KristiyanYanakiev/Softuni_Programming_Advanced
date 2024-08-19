n = int(input())

game_board = []
gamer_pos = []
amount = 100


for row in range(n):
    game_board.append(list(input()))
    if "G" in game_board[row]:
        gamer_pos.extend([row, game_board[row].index("G")])


directions = {
    "left": [0, -1],
    "right": [0, +1],
    "up": [-1, 0],
    "down": [+1, 0]
}


command = input()

r, c = gamer_pos

out_of_range = False
jackpot = False
out_of_money = False

while command != "end" and not out_of_range and not jackpot and not out_of_money:
    game_board[r][c] = "-"

    r += directions[command][0]
    c += directions[command][1]

    if not r in range(n) and not c in range(n):
        out_of_range = True

    if game_board[r][c] == "-":
        game_board[r][c] = "G"

    elif game_board[r][c] == "W":
        amount += 100
        game_board[r][c] = 'G'

    elif game_board[r][c] == "P":
        amount -= 200
        game_board[r][c] = "G"
        if amount <= 0:
            out_of_money = True

    elif game_board[r][c] == "J":
        amount += 100000
        game_board[r][c] = "G"
        jackpot = True

    command = input()

if jackpot:
    print(f"You win the Jackpot!\nEnd of the game. Total amount: {amount}$")

elif not jackpot and not out_of_range and not out_of_money:
    print(f"End of the game. Total amount: {amount}$")

elif out_of_range or out_of_money:
    print("Game over! You lost everything!")

if not out_of_money and not out_of_range:
    [print(*line, sep="") for line in game_board]
