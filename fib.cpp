#include <iostream>

using namespace std;

int count_fibonacci_numbers(int a, int b) {
  // Initialize the Fibonacci sequence.
  int fibs[2] = {0, 1};

  // Iterate over the Fibonacci sequence until we find a number greater than b.
  int i = 2;
  while (fibs[i - 1] <= b) {
    fibs[i] = fibs[i - 1] + fibs[i - 2];
    i++;
  }

  // Count the number of Fibonacci numbers in the range [a, b].
  int count = 0;
  for (int j = 0; j < i; j++) {
    if (a <= fibs[j] && fibs[j] <= b) {
      count++;
    }
  }

  return count;
}

int main() {
  int a, b;
  cin >> a >> b;

  cout << count_fibonacci_numbers(a, b) << endl;

  return 0;
}

