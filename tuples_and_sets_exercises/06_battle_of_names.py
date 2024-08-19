n = int(input())

set_of_even_sums = set()
set_of_odd_sums = set()


for current_row in range(1, n + 1):
    name = input()
    current_sum = sum([ord(ch) for ch in name]) // current_row

    if current_sum % 2 == 0:
        set_of_even_sums.add(current_sum)
    else:
        set_of_odd_sums.add(current_sum)

sum_of_even_sums = sum(set_of_even_sums)
sum_of_odd_sums = sum(set_of_odd_sums)


if sum_of_even_sums == sum_of_odd_sums:
    print(*set_of_even_sums.union(set_of_odd_sums), sep=", ")

elif sum_of_odd_sums > sum_of_even_sums:
    print(*set_of_odd_sums.difference(set_of_even_sums), sep=", ")

else:
    print(*set_of_even_sums.symmetric_difference(set_of_odd_sums), sep=", ")



