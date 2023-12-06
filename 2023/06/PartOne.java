package day6;

import utilities.Input;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class PartOne {
    public static void main(String[] args) {
        String[] input = Input.readInput("day6/input.txt");
        Map<Integer, Integer> races = new HashMap<>();
        String pattern = "\\s+";
        String[] raceSplit = input[0].split(pattern);
        String[] distanceSplit = input[1].split(pattern);
        for (int i = 1; i < raceSplit.length; i++) {
            races.put(Integer.parseInt(raceSplit[i]), Integer.parseInt(distanceSplit[i]));
        }
        int solution = 1;

        for (Integer time : races.keySet()) {
            int wayCounter = 0;
            for (int j = 0; j <= time; j++) {
                int distance = (time-j)*j;
                if (distance > races.get(time)) {
                    wayCounter++;
                }
            }
            solution *= wayCounter;
        }
        System.out.println(solution);
    }
}
