import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution4 {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("input2.txt");
        Scanner sc = new Scanner(file);

        Map<Integer, String> games = new HashMap<>();

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
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
