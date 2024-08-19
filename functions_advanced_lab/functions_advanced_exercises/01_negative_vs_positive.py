def find_positive_and_negative_sums(nums):
    positive_sum = sum(num for num in nums if num > 0)
    negative_sum = sum(num for num in nums if num < 0)

    result = ""
    if abs(negative_sum) > positive_sum:
        result = f"{negative_sum}\n{positive_sum}\nThe negatives are stronger than the positives"
    else:
        result = f"{negative_sum}\n{positive_sum}\nThe positives are stronger than the negatives"

    return result

sequence = [int(x) for x in input().split()]

print(find_positive_and_negative_sums(sequence))

