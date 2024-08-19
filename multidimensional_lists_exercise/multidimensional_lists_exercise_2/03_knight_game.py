n = int(input())

chess_board = []


for _ in range(n):
    chess_board.append(list(input()))

directions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_max_attacks_pos = []

    for row in range(n):
        for col in range(n):
            if chess_board[row][col] == "K":

                current_knight_attacks = 0
                for direction in directions:

                    k_r = row + direction[0]
                    k_c = col + direction[1]

                    if k_r in range(n) and k_c in range(n):

                        if chess_board[k_r][k_c] == "K":
                            current_knight_attacks += 1

                if current_knight_attacks > max_attacks:
                    max_attacks = current_knight_attacks
                    knight_with_max_attacks_pos = [row, col]

    if knight_with_max_attacks_pos:
        r, c = knight_with_max_attacks_pos
        chess_board[r][c] = "0"
        removed_knights += 1

    else:
        break

print(removed_knights)















