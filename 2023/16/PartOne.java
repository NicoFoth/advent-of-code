package day16;

import utilities.Input;

import java.util.*;

public class PartOne {
    private static class Laser {
        public Coordinate coordinate;
        public Coordinate direction;
        public Laser(int x, int y, int[] direction) {
            this. coordinate = new Coordinate(x, y);
            this.direction = new Coordinate(direction[0], direction[1]);
        }
    }
    public static class Coordinate {
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
    public static class Visit {
        public Coordinate coordinate;
        public Coordinate direction;
        public Visit(Coordinate coordinate, Coordinate direction) {
            this.coordinate = coordinate;
            this.direction = direction;
        }
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Visit visit = (Visit) o;
            return Objects.equals(coordinate, visit.coordinate) && Objects.equals(direction, visit.direction);
        }
        @Override
        public int hashCode() {
            return Objects.hash(coordinate, direction);
        }
    }

    public static final Map<Character, Map<Coordinate, int[][]>> newDirections = Map.of(
            '/', Map.of(
                    new Coordinate(0, 1), new int[][]{new int[]{-1, 0}},
                    new Coordinate(0, -1), new int[][]{new int[]{1, 0}},
                    new Coordinate(1, 0), new int[][]{new int[]{0, -1}},
                    new Coordinate(-1, 0), new int[][]{new int[]{0, 1}}
            ),
            '\\', Map.of(
                    new Coordinate(0, 1), new int[][]{new int[]{1, 0}},
                    new Coordinate(0, -1), new int[][]{new int[]{-1, 0}},
                    new Coordinate(1, 0), new int[][]{new int[]{0, 1}},
                    new Coordinate(-1, 0), new int[][]{new int[]{0, -1}}
            ),
            '-', Map.of(
                    new Coordinate(0, 1), new int[][]{new int[]{1, 0}, new int[]{-1, 0}},
                    new Coordinate(0, -1), new int[][]{new int[]{1, 0}, new int[]{-1, 0}}
            ),
            '|', Map.of(
                    new Coordinate(1, 0), new int[][]{new int[]{0, 1}, new int[]{0, -1}},
                    new Coordinate(-1, 0), new int[][]{new int[]{0, 1}, new int[]{0, -1}}
            ),
            '.', Map.of()
    );
    public static void main(String[] args) {
        String[] input = Input.readInput("day16/input.txt");
        Map<Coordinate, Character> map = new HashMap<>();
        for (int i = 0; i < input.length; i++) {
            String line = input[i];
            for (int j = 0; j < line.length(); j++) {
                map.put(new Coordinate(j, i), line.charAt(j));
            }
        }
        Laser startLaser = new Laser(0, 0, new int[]{1, 0});
        Queue<Laser> queue = new LinkedList<>();
        Set<Coordinate> energized = new HashSet<>();
        Set<Visit> visited = new HashSet<>();
        queue.add(startLaser);
        energized.add(startLaser.coordinate);
        visited.add(new Visit(startLaser.coordinate, startLaser.direction));
        while (!queue.isEmpty()) {
            Laser currentLaser = queue.poll();
            Character currentChar = map.get(currentLaser.coordinate);
            int[][] neutralDirection = new int[][]{new int[]{currentLaser.direction.x, currentLaser.direction.y}};
            int[][] directions = newDirections.get(currentChar).getOrDefault(currentLaser.direction, neutralDirection);
            for (int[] dir : directions) {
                Coordinate direction = new Coordinate(dir[0], dir[1]);
                Laser newLaser = new Laser(currentLaser.coordinate.x + direction.x, currentLaser.coordinate.y + direction.y, dir);
                if (newLaser.coordinate.x < 0 || newLaser.coordinate.x >= input[0].length() || newLaser.coordinate.y < 0 || newLaser.coordinate.y >= input.length) {
                    continue;
                }
                if (visited.contains(new Visit(newLaser.coordinate, direction))) {
                    continue;
                }
                visited.add(new Visit(newLaser.coordinate, direction));
                queue.add(newLaser);
                energized.add(newLaser.coordinate);
            }
        }
        System.out.println(energized.size());
    }
}
