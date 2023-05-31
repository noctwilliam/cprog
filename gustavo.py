def count_numbers_with_sum(sum_digits, max_digits):
    if max_digits == 0:
        if sum_digits == 0:
            return 1
        else:
            return 0
    count = 0
    for digit in [1, 2, 3, 4]:
        if digit == 4:
            count += count_numbers_with_sum(sum_digits - 1, max_digits - 1)
        else:
            count += count_numbers_with_sum(sum_digits - digit, max_digits - 1)
    return count

# Read input until end of file
while True:
    try:
        n = int(input())
        result = count_numbers_with_sum(n, n)
        print(result)
    except EOFError:
        break
