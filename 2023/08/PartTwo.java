package day8;

import utilities.Input;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class PartTwo {
    private static long greatestCommonDivisor(long a, long b) {
        while (b > 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    private static long leastCommonMultiple(long a, long b) {
        return a * (b / greatestCommonDivisor(a, b));
    }
    public static void main(String[] args) {
        String[] input  = Input.readInput("day8/input.txt");
        Map<String, String[]> map = new HashMap<>();
        String instructions = input[0];

        for (int i = 2; i < input.length; i++) {
            String[] split = input[i].replace("(","").replace(")","").split("\\s=\\s|, ");
            map.put(split[0], Arrays.copyOfRange(split, 1, split.length));
        }

        String[] starts = Arrays.stream(map.keySet().toArray(new String[0])).filter(s -> s.endsWith("A")).toArray(String[]::new);
        ArrayList<Integer> steps = new ArrayList<>();
        for (int i = 0; i < starts.length; i++) {
            String curr = starts[i];
            int stepsCurr = 0;
            while (!curr.endsWith("Z")) {
                if (instructions.charAt(stepsCurr % instructions.length()) == 'R') {
                    curr = map.get(curr)[1];
                    stepsCurr++;
                } else {
                    curr = map.get(curr)[0];
                    stepsCurr++;
                }
            }
            steps.add(stepsCurr);
        }
        long solution = steps.get(0);
        for (int i = 1; i < steps.size(); i++) {
            solution = leastCommonMultiple(solution, steps.get(i));
        }
        System.out.println(solution);
    }
}
