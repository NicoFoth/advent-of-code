package day1;

import java.io.*;
import java.util.*;

public class PartOne {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        int solution = 0;
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            String number = "";
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