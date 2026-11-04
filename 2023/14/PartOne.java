import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class PartOne {
    public static void main(String[] args) throws IOException {
        String[] input = Files.readAllLines(Path.of("input.txt")).toArray(String[]::new);
        int totalWeight = 0;
        for (int col = 0; col < input[0].length(); col++) {
            int spaceCounter = 0;
            for (int row = 0; row < input.length; row++) {
                if (input[row].charAt(col) == 'O') {
                    if (spaceCounter == 0) totalWeight += input.length - row;
                    else totalWeight += input.length - row + spaceCounter;
                } else if (input[row].charAt(col) == '.') {
                    spaceCounter++;
                }
                else {
                    spaceCounter = 0;
                }
            }
        }
        System.out.println(totalWeight);
    }
}
