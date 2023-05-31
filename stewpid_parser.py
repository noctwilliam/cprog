'''
Children are taught to add multi-digit numbers from right to left, one digit at a time.
Many find the “carry” operation, where a 1 is carried from one digit position to the
next, to be a significant challenge. Your job is to count the number of carry operations
for each of a set of addition problems so that educators may assess their difficulty.

This code counts the number of carry operations needed to add two numbers.
Example: 123 + 456 = 579, 1 + 4 = 5, 2 + 5 = 7, 3 + 6 = 9. No carry operations.
Example: 555 + 555 = 1110, 5 + 5 = 10 (1 carry operation), 5 + 5 + 1 (from previous operation) = 11 (1 carry operation).

Input
Each line of input contains two unsigned integers less than 10 digits. The last line of
input contains “0 0”.

123 456
555 555
123 594
0 0

Output
For each line of input except the last, compute the number of carry operations that
result from adding the two numbers and print them in the format shown below.

No carry operation.
3 carry operations.
1 carry operation.

'''

def count_carry_operations(num1, num2):
    carry = 0
    carry_count = 0

    # Loop through each digit of num1 and num2
    while num1 > 0 or num2 > 0:
        # Get the rightmost digit of num1 and num2
        digit1 = num1 % 10
        digit2 = num2 % 10

        # Add the digits and the carry
        sum_digits = digit1 + digit2 + carry
        if sum_digits >= 10:
            # If the sum is greater than or equal to 10, there is a carry
            carry = 1
            carry_count += 1
        else:
            # If the sum is less than 10, there is no carry
            carry = 0

        # Remove the rightmost digit from num1 and num2
        num1 //= 10
        num2 //= 10

    return carry_count

carry_count_output = []

print(1//10)

# Read input until "0 0" is encountered
while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break #break the loop if "0 0" is encountered

    carry_count = count_carry_operations(num1, num2)
    if carry_count == 0:
        carry_count_output.append("No carry operation.")
    elif carry_count == 1:
        carry_count_output.append("1 carry operation.")
    else:
        carry_count_output.append(f"{carry_count} carry operations.")

for i in carry_count_output:
    print(i)