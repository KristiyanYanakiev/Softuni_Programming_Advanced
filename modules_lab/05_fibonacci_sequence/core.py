def  create_fib_seq(num):
    seq = [0, 1]

    for _ in range(num - 2):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)

    return seq


def locate_number(num, sequence:list[int]):
    try:
        return f"The number - {num} is at index {sequence.index(num)}"
    except ValueError:
        return f"The number {num} is not in the sequence"


