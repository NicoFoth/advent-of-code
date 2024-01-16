package day3;
import utilities.Input;

import java.io.FileNotFoundException;

public class PartOne {

    private static boolean isNotDigitOrDot(char c) {
        return (c < 48 || c > 57) && c != 46;
    }

    public static void main(String[] args) throws FileNotFoundException {
        String[] input = Input.readInput("day3/input.txt");
        int solution = 0;

        for (int i = 0; i < input.length; i++) {
            int numberLength = 0;
            int numberStartAt = 0;
            boolean numberFound = false;
            for (int j = 0; j < input[i].length(); j++) {
                if (input[i].charAt(j) >= 48 && input[i].charAt(j) <= 57) {
                    numberLength += 1;
                    if (!numberFound) {
                        numberStartAt = j;
                        numberFound = true;
                    }
                }
                if (!(input[i].charAt(j) >= 48 && input[i].charAt(j) <= 57) || j == input[i].length()-1) {
                    boolean valid = false;
                    if (!numberFound) continue;
                    if (i != 0) {
                        for (int k = Math.max(numberStartAt - 1, 0); k < Math.min(numberStartAt + numberLength + 1, input[i - 1].length()); k++) {
                            if (isNotDigitOrDot(input[i - 1].charAt(k))) {
                                valid = true;
                                break;
                            }
                        }
                    }
                    if (i < input.length - 1) {
                        for (int k = Math.max(numberStartAt - 1, 0); k < Math.min(numberStartAt + numberLength + 1, input[i + 1].length()); k++) {
                            if (isNotDigitOrDot(input[i + 1].charAt(k))) {
                                valid = true;
                                break;
                            }
                        }
                    }
                    if (numberStartAt >= 1) {
                        if (isNotDigitOrDot(input[i].charAt(numberStartAt - 1))) {
                            valid = true;
                        }
                    }
                    if (numberStartAt + numberLength < input[i].length()) {
                        if (isNotDigitOrDot(input[i].charAt(numberStartAt + numberLength))) {
                            valid = true;
                        }
                    }
                    if (valid) {
                        String number = "";
                        for (int a = numberStartAt; a < numberStartAt + numberLength; a++) {
                            number += input[i].charAt(a);
                        }
                        System.out.println(number);
                        solution += Integer.parseInt(number);

                    }
                    numberStartAt = numberLength = 0;
                    numberFound = false;
                }
            }
        }
        System.out.println(solution);
    }
}
