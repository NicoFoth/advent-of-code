import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import java.io.FileNotFoundException;
import java.util.*;

public class PartOne {
    public static void main(String[] args) throws IOException {
        String[] input = Files.readAllLines(Path.of("input.txt")).toArray(String[]::new);
        Map<Integer, String> games = new HashMap<>();
        for (int i = 0; i < input.length; i++) {
            String line = input[i];
            int id = Integer.parseInt(line.split(":")[0].split(" ")[1]);
            games.put(id, line.split(":")[1]);
        }
        int solution = 0;
        for (Integer gameId : games.keySet()) {
            String[] draws = games.get(gameId).split(";");
            boolean possible = true;
            drawLoop:
            for (String draw : draws) {
                String[] cubes = draw.split(",");
                for (String cube : cubes) {
                    cube = cube.trim();
                    switch (cube.split(" ")[1]) {
                        case "red":
                            if (Integer.parseInt(cube.split(" ")[0]) > 12) {
                                possible = false;
                                System.out.println(gameId + "-r");
                                break drawLoop;
                            }    
                            break;
                        case "blue":
                            if (Integer.parseInt(cube.split(" ")[0]) > 14) {
                                possible = false;
                                System.out.println(gameId + "-b");
                                break drawLoop;
                            }    
                            break;
                        case "green":
                            if (Integer.parseInt(cube.split(" ")[0]) > 13) {
                                possible = false;
                                System.out.println(gameId + "-g");
                                break drawLoop;
                            }    
                            break;
                        }
                }
            }
            if (possible) {
                solution += gameId;
            }
        }
        System.out.println(solution);
    }
}
