/**
 * Solution to the ProMed 2010 UiTM National Level by ChatGPT
 */
import java.util.Scanner;

public class PasswordChecker {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int numTestCases = scanner.nextInt();
		scanner.nextLine(); // Read the newline character after the integer

		for (int i = 0; i < numTestCases; i++) {
			String password = scanner.nextLine();
			if (isPasswordAcceptable(password)) {
				System.out.println(password + " is acceptable");
			} else {
				System.out.println(password + " is unacceptable");
			}
		}
		scanner.close();
	}

	private static boolean isPasswordAcceptable(String password) {
		int consecutiveVowels = 0;
		int consecutiveConsonants = 0;
		char prevChar = '\0';
		boolean containsVowel = false;
		boolean containsNumeric = false;

		for (char c : password.toCharArray()) {
			if (Character.isLetter(c)) {
				c = Character.toLowerCase(c);
				if (isVowel(c)) {
					consecutiveVowels++;
					consecutiveConsonants = 0;
					containsVowel = true;
				} else {
					consecutiveConsonants++;
					consecutiveVowels = 0;
				}

				if (c == prevChar && c != 'e' && c != 'o') {
					return false;
				}
				prevChar = c;
			} else if (Character.isDigit(c)) {
				containsNumeric = true;
			}
		}

		return containsVowel && containsNumeric && consecutiveVowels < 3 && consecutiveConsonants < 3;
	}

	private static boolean isVowel(char c) {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
	}
}