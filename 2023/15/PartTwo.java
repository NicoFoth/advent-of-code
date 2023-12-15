package day15;

import utilities.Input;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class PartTwo {
    private static int hashFunction(String s) {
        int hash = 0;
        for (char c : s.toCharArray()) {
            hash = (hash + c) * 17 % 256;
        }
        return hash;
    }
    public static void main(String[] args) {
        String[] steps = Input.readInput("day15/input.txt")[0].split(",");
        Map<Integer, List<String>> boxes = new HashMap<>();
        Map<String, Integer> focalLengths = new HashMap<>();
        for (String step : steps) {
            String label = step.split("[=-]")[0];
            int index = hashFunction(label);
            if (!boxes.containsKey(index)) {
                boxes.put(index, new LinkedList<>());
            }
            if (step.contains("=")) {
                int focalLength = Integer.parseInt(step.split("=")[1]);
                if (boxes.get(index).contains(label)) {
                    focalLengths.put(label, focalLength);
                } else {
                    boxes.get(index).add(label);
                    focalLengths.put(label, focalLength);
                }
            } else {
                boxes.get(index).remove(label);
                focalLengths.remove(label);
            }
        }
        int solution = 0;
        for (int boxNumber : boxes.keySet()) {
            for (String lens : boxes.get(boxNumber)) {
                int focusingPower = focalLengths.get(lens)*(boxNumber+1)*(boxes.get(boxNumber).indexOf(lens)+1);
                solution += focusingPower;
            }
        }
        System.out.println(solution);
    }
}
