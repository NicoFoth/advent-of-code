package day14;

import utilities.Input;

public class PartOne {
    public static void main(String[] args) {
        String[] input = Input.readInput("day14/input.txt");
        int totalWeight = 0;
        for (int col = 0; col < input[0].length(); col++) {
            int spaceCounter = 0;
            for (int row = 0; row < input.length; row++) {
                if (input[row].charAt(col) == 'O') {
                    if (spaceCounter == 0) totalWeight += input.length - row;
                    else totalWeight += input.length - row + spaceCounter;
                } else if (input[row].charAt(col) == '.') {
                    spaceCounter++;
                }
                else {
                    spaceCounter = 0;
                }
            }
        }
        System.out.println(totalWeight);
    }
}
