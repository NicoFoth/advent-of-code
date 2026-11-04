import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import java.util.HashMap;
import java.util.Map;

public class PartTwo {
    public static void main(String[] args) throws IOException {
        String[] input = Files.readAllLines(Path.of("input.txt")).toArray(String[]::new);
        String pattern = "\\s+";
        long time = Long.parseLong(input[0].split(":")[1].replaceAll(pattern, ""));
        long distance = Long.parseLong(input[1].split(":")[1].replaceAll(pattern, ""));
        int solution = 0;
        for (int j = 0; j <= time; j++) {
            long curr_distance = (time-j)*j;
            if (curr_distance > distance) {
                solution++;
            }
        }
    System.out.println(solution);
    }
}
