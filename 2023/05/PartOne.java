package day5;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class PartOne {
    private long[] seeds;
    private long[][][] maps;

    private void readSpecificInput() throws FileNotFoundException {
        File file = new File("day5/input.txt");
        Scanner sc = new Scanner(file);
        ArrayList<String> input = new ArrayList<>();
        while (sc.hasNextLine()) {
            input.add(sc.nextLine());
        }
        String[] inputArray = input.toArray(new String[0]);
        this.maps = new long[7][][];
        int mapCounter = 0;
        this.seeds = Arrays.stream(inputArray[0].split(": ")[1].split(" ")).map(Long::parseLong).mapToLong(i -> i).toArray();
        for (int i = 2; i < inputArray.length; i++) {
            if (inputArray[i].contains("map:")) {
                ArrayList<long[]> map = new ArrayList<>();
                for (int j = i + 1; j < inputArray.length; j++) {
                    if (inputArray[j].isEmpty()) {
                        i = j;
                        break;
                    }
                    String[] line_split = inputArray[j].split(" ");
                    long[] x = new long[3];
                    x[0] = Long.parseLong(line_split[0]);
                    x[1] = Long.parseLong(line_split[1]);
                    x[2] = Long.parseLong(line_split[2]);
                    map.add(x);
                }
                this.maps[mapCounter] = map.toArray(new long[0][0]);
                mapCounter++;
            }
        }
    }

    private long convertMap(long[][] map, long value) {
        for (int i = 0; i < map.length; i++) {
            if (value >= map[i][1] && value < map[i][2]+map[i][1]) {
                return map[i][0]+(value-map[i][1]);
            }
        }
        return value;
    }

    public static void main(String[] args) throws FileNotFoundException{
        PartOne partOne = new PartOne();
        partOne.readSpecificInput();
        long minLocation = Long.MAX_VALUE;

        for (int i = 0; i < partOne.seeds.length; i++) {
            long curr = partOne.seeds[i];
            for (int j = 0; j < partOne.maps.length; j++) {
                curr = partOne.convertMap(partOne.maps[j], curr);
            }
            if (curr < minLocation) {
                minLocation = curr;
            }
        }
        System.out.println(minLocation);
    }
}
