package day17;

import utilities.Input;

import java.util.*;

public class PartOne {
    public static class Visit {
        Coordinate coordinate;
        Coordinate direction;
        public Visit(Coordinate pos, Coordinate dir) {
            this.coordinate = pos;
            this.direction = dir;
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
    public static Map<Coordinate, List<Coordinate>> directions = Map.of(
        new Coordinate(1, 0), List.of(new Coordinate(0, 1), new Coordinate(0, -1)),
        new Coordinate(0, 1), List.of(new Coordinate(1, 0), new Coordinate(-1, 0)),
        new Coordinate(0, 0), List.of(new Coordinate(1, 0), new Coordinate(-1, 0), new Coordinate(0, 1), new Coordinate(0, -1))
    );
    public static List<Visit> getPossibleMoves(Coordinate currentPos, Coordinate prevDirection, int width, int height) {
        List<Visit> possibleMoves = new ArrayList<>();
        for (Coordinate dir : directions.get(new Coordinate(Math.abs(prevDirection.x), Math.abs(prevDirection.y)))) {
            for (int i = 1; i <= 3; i++) {
                Coordinate possibleMove = new Coordinate(
                    currentPos.x + dir.x * i,
                    currentPos.y + dir.y * i
                );
                if (possibleMove.x < 0 || possibleMove.x >= width || possibleMove.y < 0 || possibleMove.y >= height) {
                    continue;
                }
                possibleMoves.add(new Visit(possibleMove, dir));
            }
        }
        return possibleMoves;
    }

    public static void main(String[] args) {
        String[] input = Input.readInput("day17/input.txt");
        Set<Visit> visited = new HashSet<>();
        Map<Coordinate, Integer> heatLosses = new HashMap<>();
        Queue<Visit> queue = new PriorityQueue<>(Comparator.comparingInt(o -> heatLosses.get(o.coordinate)));

        Coordinate startPos = new Coordinate(0, 0);
        for (int i = 1; i <= 3; i++) {
            Coordinate possibleMove = new Coordinate(startPos.x + i, startPos.y);
            Coordinate possibleMove2 = new Coordinate(startPos.x, startPos.y + i);
            heatLosses.put(possibleMove, Integer.parseInt(String.valueOf(input[possibleMove.y].charAt(possibleMove.x))));
            heatLosses.put(possibleMove2, Integer.parseInt(String.valueOf(input[possibleMove2.y].charAt(possibleMove2.x))));
            queue.add(new Visit(possibleMove, new Coordinate(1, 0)));
            queue.add(new Visit(possibleMove2, new Coordinate(0, 1)));
            visited.add(new Visit(possibleMove, new Coordinate(1, 0)));
            visited.add(new Visit(possibleMove2, new Coordinate(0, 1)));

        }

        while (!queue.isEmpty()) {
            Visit current = queue.poll();
            if (current.coordinate.x == input[0].length() - 1 && current.coordinate.y == input.length - 1) {
                System.out.println(heatLosses.get(current.coordinate));
                break;
            }
            List<Visit> possibleMoves = getPossibleMoves(current.coordinate, current.direction, input[0].length(), input.length);
            for (Visit move : possibleMoves) {
                int moveAmount = Math.max(Math.abs(move.coordinate.x - current.coordinate.x), Math.abs(move.coordinate.y - current.coordinate.y));
                int heatLoss = heatLosses.get(current.coordinate);
                for (int i = 1; i <= moveAmount; i++) {
                    heatLoss += Integer.parseInt(String.valueOf(input[current.coordinate.y + move.direction.y * i].charAt(current.coordinate.x + move.direction.x * i)));
                }
                if (!visited.contains(move)) {
                    heatLosses.put(move.coordinate, heatLoss);
                    visited.add(move);
                    queue.add(move);
                    System.out.println("(" + move.coordinate.x + "," + move.coordinate.y + ")" + ": " + heatLoss);
                } else {
                    if (heatLoss < heatLosses.get(move.coordinate)) {
                        heatLosses.put(move.coordinate, heatLoss);
                    }
                }
            }
        }
    }
}
