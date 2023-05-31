#include <iostream>
using namespace std;

/*
Gustavo knows how to count, but he is just now learning how to write numbers.
He has already learned the digits 1, 2, 3, and 4. But he does not yet realize that 4 is different than 1, so he thinks that 4 is just another way to write 1. He is having fun with a little game he created: he makes numbers with the four digits that he knows and sums their values.

For example:
132 = 1 + 3 + 2 = 6
112314=1+1+2+3+1+1=9 (remember that Gustavo thinks that 4=1)

Gustavo now wants to know how many such numbers he can create whose sum is a
number n. For n = 2, he can make 5 numbers: 11, 14, 41, 44, and 2. (He knows how to count up beyond five, just not how to write it.) However, he can’t figure out this sum for n greater than 2, and asks for your help.

Input
Input will consist of an arbitrary number of integers n such that 1 ≤ n ≤ 1,000.
You must read until you reach the end of file.

Output
For each integer read, output an single integer on a line stating how many numbers. Gustavo can make such that the sum of their digits is equal to n.

Sample Input
2
3

Sample Output
5
13

*/
