package day15;

import utilities.Input;

public class PartOne {
    public static void main(String[] args) {
        String input = Input.readInput("day15/input.txt")[0];
        String[] numbers = input.split(",");

        int solution = 0;
        for (String number : numbers) {
            int currentValue = 0;
            for (char c : number.toCharArray()) {
                currentValue = (currentValue + c) * 17 % 256;
            }
            solution += currentValue;
        }
        System.out.println(solution);
    }
}
