package day5;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class PartTwo {
    private ArrayList<long[]> seeds;
    private long[][][] maps;

    public PartTwo() {
        this.seeds = new ArrayList<>();
        this.maps = new long[7][][];
    }

    private void readSpecificInput() throws FileNotFoundException {
        File file = new File("day5/input.txt");
        Scanner sc = new Scanner(file);
        ArrayList<String> input = new ArrayList<>();
        while (sc.hasNextLine()) {
            input.add(sc.nextLine());
        }
        String[] inputArray = input.toArray(new String[0]);
        int mapCounter = 0;
        String[] seedSplit = inputArray[0].split(": ")[1].split(" ");
        for (int i = 0; i < seedSplit.length; i+=2) {
            seeds.add(new long[]{Long.parseLong(seedSplit[i]), Long.parseLong(seedSplit[i]) + Long.parseLong(seedSplit[i + 1])});
        }
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

    public static void main(String[] args) throws FileNotFoundException {
        PartTwo partTwo = new PartTwo();
        partTwo.readSpecificInput();
        for (int i = 0; i < partTwo.maps.length; i++) {
            ArrayList<long[]> newSeeds = new ArrayList<>();
            while (!partTwo.seeds.isEmpty()) {
                long[] seed = partTwo.seeds.remove(0);
                boolean rangeFound = false;
                for (int j = 0; j < partTwo.maps[i].length; j++) {
                    long[] map = partTwo.maps[i][j];
                    long overlapStart = Math.max(seed[0], map[1]);
                    long overlapEnd = Math.min(seed[1], map[1] + map[2]);
                    if (overlapStart < overlapEnd) {
                        long[] newSeed = new long[2];
                        newSeed[0] = map[0] + (overlapStart - map[1]);
                        newSeed[1] = newSeed[0] + (overlapEnd - overlapStart);
                        newSeeds.add(newSeed);
                        rangeFound = true;
                        if (overlapStart > seed[0]) {
                            newSeeds.add(new long[] {seed[0], overlapStart});
                        }
                        if (seed[1] > overlapEnd) {
                            newSeeds.add(new long[] {overlapEnd, seed[1]});
                        }
                        break;
                    }
                }
                if (!rangeFound) {
                    newSeeds.add(seed);
                }
            }
            partTwo.seeds = newSeeds;
        }
        long minLocation = Long.MAX_VALUE;
        for (int i = 0; i < partTwo.seeds.size(); i++) {
            long[] seed = partTwo.seeds.get(i);
            if (seed[0] < minLocation) {
                minLocation = seed[0];
            }
        }
        System.out.println(minLocation);
    }
}
