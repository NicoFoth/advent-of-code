package day10;

import utilities.Input;

import java.util.*;

public class PartOne {
    private static final Map<Character, int[][]> pipeMappings = Map.of(
        '|', new int[][]{{0, 1}, {0, -1}},
        '-', new int[][]{{1, 0}, {-1, 0}},
        'L', new int[][]{{0, -1}, {1, 0}},
        'J', new int[][]{{0, -1}, {-1, 0}},
        '7', new int[][]{{0, 1}, {-1, 0}},
        'F', new int[][]{{0, 1}, {1, 0}},
        'S', new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}},
        '.', new int[][]{}
    );
    private static List<List<Integer>> possibleMoves(int x, int y, char[][] grid) {
        List<List<Integer>> moves = new ArrayList<>();
        for (int[] move : pipeMappings.get(grid[y][x])) {
            int myMoveX = x + move[0];
            int myMoveY = y + move[1];
            int[][] otherMoves = pipeMappings.get(grid[myMoveY][myMoveX]);
            for (int[] otherMove : otherMoves) {
                if (otherMove[0] == -move[0] && otherMove[1] == -move[1]) {
                    moves.add(new ArrayList<>(Arrays.asList(myMoveX, myMoveY)));
                }
            }
        }
        return moves;
    }

    private static int bfs(char[][] grid, int startX, int startY) {
        Queue<int[]> queue = new LinkedList<>();
        Set<List<Integer>> visited = new HashSet<>();
        queue.add(new int[]{startX, startY, 0});
        visited.add(new ArrayList<>(Arrays.asList(startX, startY)));

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            List<List<Integer>> possibleMoves = possibleMoves(current[0], current[1], grid);
            if (possibleMoves.isEmpty()) {
                System.out.println("Empty");
            }
            for (List<Integer> move : possibleMoves) {
                if (!visited.contains(move)) {
                    int[] newMove = new int[]{move.get(0), move.get(1), current[2] + 1};
                    queue.add(newMove);
                    visited.add(new ArrayList<>(Arrays.asList(move.get(0), move.get(1))));
                }
            }
            if (queue.isEmpty()) {
                return current[2];
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String[] input = Input.readInput("day10/input.txt");
        char[][] grid = new char[input.length][input[0].length()];
        int startX = 0, startY = 0;
        for (int i = 0; i < input.length; i++) {
            if (input[i].contains("S")) {
                startX = input[i].indexOf("S");
                startY = i;
            }
            grid[i] = input[i].toCharArray();
        }
        System.out.println(bfs(grid, startX, startY));
    }
}
