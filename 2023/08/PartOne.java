package day8;

import utilities.Input;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class PartOne {
    public static void main(String[] args) {
        String[] input  = Input.readInput("day8/input.txt");
        Map<String, String[]> map = new HashMap<>();
        String instructions = input[0];

        for (int i = 2; i < input.length; i++) {
            String[] split = input[i].replace("(","").replace(")","").split("\\s=\\s|, ");
            map.put(split[0], Arrays.copyOfRange(split, 1, split.length));
        }
        String curr = "AAA";
        int steps = 0;
        while (!curr.equals("ZZZ")) {
            if (instructions.charAt(steps % instructions.length()) == 'R') {
                curr = map.get(curr)[1];
                steps++;
            } else {
                curr = map.get(curr)[0];
                steps++;
            }
        }
        System.out.println(steps);
    }
}
