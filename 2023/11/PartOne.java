package day11;

import utilities.Input;

import java.util.*;


public class PartOne {
    public static class Point {
        int x;
        int y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) {
        String[] input = Input.readInput("day11/input.txt");
        ArrayList<Point> galaxies = new ArrayList<>();

        int yModifier = 0;
        for (int y = 0; y < input.length; y++) {
            String line = input[y];
            if (!line.contains("#")) {
                yModifier++;
            }
            for (int j = 0; j < line.length(); j++) {
                if (line.charAt(j) == '#') {
                    galaxies.add(new Point(j, y + yModifier));
                }
            }
        }
        int xModifier = 0;
        for (int x = 0; x < input[0].length(); x++) {
            boolean galaxyInRow = false;
            for (String s : input) {
                if (s.charAt(x) == '#') {
                    galaxyInRow = true;
                    break;
                }
            }
            if (!galaxyInRow) {
                ArrayList<Point> updatedGalaxies = new ArrayList<>();
                for (Point p : galaxies) {
                    if (p.x > x+xModifier) {
                        updatedGalaxies.add(new Point(p.x + 1, p.y));
                    } else {
                        updatedGalaxies.add(p);
                    }
                }
                xModifier++;
                galaxies = updatedGalaxies;
            }
        }
        int solution = 0;
        for (int i = 0; i < galaxies.size(); i++) {
            for (int j = i + 1; j < galaxies.size(); j++) {
                Point p = galaxies.get(i);
                Point q = galaxies.get(j);
                solution += Math.abs(p.x - q.x) + Math.abs(p.y - q.y);
            }
        }
        System.out.println(solution);
    }
}
