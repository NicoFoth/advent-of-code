package day18;

import utilities.Input;

import java.util.*;

public class PartTwo {
    private static  class Coordinate {
        public int x;
        public int y;
        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Coordinate that = (Coordinate) o;
            return x == that.x && y == that.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
    private static final Map<Character, int[]> directions = Map.of(
            '0', new int[] {1, 0},
            '1', new int[] {0, 1},
            '2', new int[] {-1, 0},
            '3', new int[] {0, -1}
    );
    public static List<Coordinate> getTrench(String[] input) {
        Coordinate digStart = new Coordinate(0, 0);
        List<Coordinate> excavated = new LinkedList<>();
        excavated.add(digStart);
        for (String line : input) {
            int[] direction = directions.get(line.charAt(line.length()-2));
            String dist = line.split("#")[1].replace(")", "").substring(0, 5);
            digStart.x += direction[0] * Integer.parseInt(dist, 16);
            digStart.y += direction[1] * Integer.parseInt(dist, 16);
            excavated.add(new Coordinate(digStart.x, digStart.y));
        }
        return excavated;
    }
    public static int getPerimeterSize(String[] input) {
        int perimeterSize = 0;
        for (String line : input) {
            perimeterSize += Integer.parseInt(line.split("#")[1].replace(")", "").substring(0, 5), 16);
        }
        return perimeterSize;
    }
    public static void main(String[] args) {
        String[] input = Input.readInput("day18/input.txt");
        List<Coordinate> trench = getTrench(input);
        Collections.reverse(trench);

        // Shoelace formula for the area of the polygon
        long areaSum = 0;
        for (int i = 0; i < trench.size() - 1; i++) {
            areaSum += (long) trench.get(i).x * trench.get(i + 1).y;
            areaSum -= (long) trench.get(i + 1).x * trench.get(i).y;
        }
        areaSum = Math.abs(areaSum) / 2;

        // Pick's theorem to the points inside the polygon
        int perimeterSize = getPerimeterSize(input);
        long lavaMass = areaSum + (perimeterSize/2) + 1;
        System.out.println(lavaMass);
    }
}
