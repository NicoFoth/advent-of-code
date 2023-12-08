package day1;

import java.io.*;
import java.util.*;

public class PartTwo {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int solution = 0;

        Map<String, String> numbers = new HashMap<>();
        numbers.put("one", "o1e");
        numbers.put("two", "t2o");
        numbers.put("three", "t3e");
        numbers.put("four", "f4r");
        numbers.put("five", "f5e");
        numbers.put("six", "s6x");
        numbers.put("seven", "s7n");
        numbers.put("eight", "e8t");
        numbers.put("nine", "n9e");
        numbers.put("zero", "z0o");

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            String number = "";

            for (String key : numbers.keySet()) {
                line = line.replaceAll(key, numbers.get(key));
            }
            for (int i = 0; i < line.length(); i++) {
                if (line.charAt(i) >= 47 && line.charAt(i) <= 57) {
                    number += line.charAt(i);
                    break;
                }
            }
            for (int i = line.length()-1; i >= 0; i--) {
                if (line.charAt(i) >= 47 && line.charAt(i) <= 57) {
                    number += line.charAt(i);
                    break;
                }
            }
            solution += Integer.parseInt(number);
        }
        sc.close();
        System.out.println(solution);
    }
}
