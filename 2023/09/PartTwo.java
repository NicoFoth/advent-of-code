package day9;

import utilities.Input;

import java.util.Arrays;

public class PartTwo {
    private static int differenciate(int[] numbers) {
        int[] differences = new int[numbers.length - 1];
        for (int i = 0; i < numbers.length - 1; i++) {
            differences[i] = numbers[i + 1] - numbers[i];
        }
        if (Arrays.equals(new int[differences.length], differences)) {
            return 0;
        }
        return differences[0] - differenciate(differences);
    }

    public static void main(String[] args) {
        String[] input = Input.readInput("day9/input.txt");
        int solution = 0;
        for (String line : input) {
            int[] numbers = Arrays.stream(line.split(" ")).map(Integer::parseInt).mapToInt(i -> i).toArray();
            int difference = differenciate(numbers);
            solution += numbers[0] - difference;
        }
        System.out.println(solution);
    }
}
