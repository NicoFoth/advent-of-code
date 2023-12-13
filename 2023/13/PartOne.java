package day13;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PartOne {

    private static boolean checkIfVerticalMirror(int lineLeft, int lineRight, List<String> map) {
        for (String string : map) {
            for (int i = 0; i <= Math.min(lineLeft, string.length() - lineRight - 1); i++) {
                if (string.charAt(lineLeft - i) != string.charAt(lineRight + i)) {
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean checkIfHorizontalMirror(int lineTop, int lineBottom, List<String> map) {
        for (int charIdx = 0; charIdx < map.get(0).length(); charIdx++) {
            for (int i = 0; i <= Math.min(lineTop, map.size() - lineBottom - 1); i++) {
                if (map.get(lineTop - i).charAt(charIdx) != map.get(lineBottom + i).charAt(charIdx)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        List<List<String>> input = new ArrayList<>();
        try {
            File file = new File("day13/input.txt");
            Scanner sc = new Scanner(file);
            List<String> temp = new ArrayList<>();
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                if (line.isEmpty()) {
                    input.add(temp);
                    temp = new ArrayList<>();
                } else {
                    temp.add(line);
                }
            }
            input.add(temp);
        } catch(FileNotFoundException e) {
            System.out.println("File not found");
        }
        int verticalCount = 0;
        int horizontalCount = 0;
        for (List<String> pattern : input) {
            for (int leftPointer = 0, rightPointer = 1; rightPointer < pattern.get(0).length(); leftPointer++, rightPointer++) {
                if (checkIfVerticalMirror(leftPointer, rightPointer, pattern)) {
                    verticalCount += leftPointer + 1;
                    break;
                }
            }
            for (int topPointer = 0, bottomPointer = 1; bottomPointer < pattern.size(); topPointer++, bottomPointer++) {
                if (checkIfHorizontalMirror(topPointer, bottomPointer, pattern)) {
                    horizontalCount += topPointer + 1;
                    break;
                }
            }
        }
        int solution = verticalCount + 100 * horizontalCount;
        System.out.println(solution);
    }
}
