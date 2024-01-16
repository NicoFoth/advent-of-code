package day14;

import utilities.Input;

import java.util.*;

public class PartTwo {

    public record Pair(int x, int y) {
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
    private static Map<Pair, Character> tiltNorth(Map<Pair, Character> map, int width, int height) {
        for (int col = 0; col < width; col++) {
            int spaceCounter = 0;
            for (int row = 0; row < height; row++) {
                char currentChar = map.getOrDefault(new Pair(col, row), '.');
                if (currentChar == 'O') {
                    if (spaceCounter != 0) {
                        map.put(new Pair(col, row - spaceCounter), 'O');
                        map.put(new Pair(col, row), '.');
                    }
                } else if (currentChar == '.') {
                    spaceCounter++;
                } else {
                    spaceCounter = 0;
                }
            }
        }
        return map;
    }

    private static Map<Pair, Character> rotate90Clockwise(Map<Pair, Character> map, int height) {
        Map<Pair, Character> newMap = new HashMap<>();
        for (Pair p : map.keySet()) {
            //newMap.put(new Pair(height - p.y, p.x), map.get(p));
            newMap.put(new Pair(height - 1 - p.y, p.x), map.get(p));
        }
        return newMap;
    }

    private static int calculateLoad(Map<Pair, Character> map, int width) {
        int totalWeight = 0;
        for (int col = 0; col < width; col++) {
            for (int row = 0; row < width; row++) {
                if (map.getOrDefault(new Pair(col, row), '.') == 'O') {
                    totalWeight += width - row;
                }
            }
        }
        return totalWeight;
    }

    private static void printGrid(Map<Pair, Character> map, int width, int height) {
        for (int row = 0; row < height; row++) {
            StringBuilder sb = new StringBuilder();
            for (int col = 0; col < width; col++) {
                sb.append(map.getOrDefault(new Pair(col, row), '.'));
            }
            System.out.println(sb);
        }
    }

    public static void main(String[] args) {
        String[] input = Input.readInput("day14/input.txt");
        Map<Pair, Character> map = new HashMap<>();
        for (int i = 0; i < input.length; i++) {
            for (int j = 0; j < input[0].length(); j++) {
                map.put(new Pair(j, i), input[i].charAt(j));
            }
        }

        Set<Map<Pair, Character>> seen = new HashSet<>();
        List<Map<Pair, Character>> iterations = new ArrayList<>();
        while (true) {
            for (int i = 0; i < 4; i++) {
                Map<Pair, Character> tilted = tiltNorth(map, input[0].length(), input.length);
                map = rotate90Clockwise(tilted, input.length);
            }
            //printGrid(map, input[0].length(), input.length);
            if (seen.contains(map)) {
                break;
            }
            seen.add(map);
            iterations.add(map);
        }
        int cycleBegin = iterations.indexOf(map);
        int cycleLength = iterations.size() - cycleBegin;
        map = iterations.get((1000000000 - cycleBegin) % cycleLength + cycleBegin);
        System.out.println(calculateLoad(map, input[0].length()));
    }
}
