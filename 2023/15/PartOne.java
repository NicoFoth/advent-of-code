import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class PartOne {
    public static void main(String[] args) throws IOException {
        String input = Files.readAllLines(Path.of("input.txt")).toArray(String[]::new)[0];
        String[] numbers = input.split(",");

        int solution = 0;
        for (String number : numbers) {
            int currentValue = 0;
            for (char c : number.toCharArray()) {
                currentValue = (currentValue + c) * 17 % 256;
            }
            solution += currentValue;
        }
        System.out.println(solution);
    }
}
