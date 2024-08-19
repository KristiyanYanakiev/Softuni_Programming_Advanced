from core import create_fib_seq, locate_number


command = input()
seq = []
while command != "Stop":
    n = int(command.split()[-1])
    if "Create" in command:
        seq = create_fib_seq(n)
        print(*seq)

    else:
        print(locate_number(n, seq))



    command = input()

