import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;

public class PartTwo {
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
            int red = 0;
            int green = 0;
            int blue = 0;

            for (String draw : draws) {
                String[] cubes = draw.split(",");
                for (String cube : cubes) {
                    cube = cube.trim();
                    switch (cube.split(" ")[1]) {
                        case "red":
                            if (Integer.parseInt(cube.split(" ")[0]) > red) {
                                red = Integer.parseInt(cube.split(" ")[0]);
                                }    
                            break;
                        case "blue":
                            if (Integer.parseInt(cube.split(" ")[0]) > blue) {
                                blue = Integer.parseInt(cube.split(" ")[0]);
                            }    
                            break;
                        case "green":
                            if (Integer.parseInt(cube.split(" ")[0]) > green) {
                                green = Integer.parseInt(cube.split(" ")[0]);
                            }    
                            break;
                        }
                }
            }
            solution += red * green * blue;
        }
        System.out.println(solution);
    }

}
