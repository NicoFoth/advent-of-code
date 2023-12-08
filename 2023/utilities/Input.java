package utilities;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Input {

    public static String[] readInput(String path){
        File file = new File(path);
        try {
            Scanner sc = new Scanner(file);

            ArrayList<String> lines = new ArrayList<>();
            while (sc.hasNextLine()) {
                lines.add(sc.nextLine());
            }
            return lines.toArray(new String[0]);
        } catch (FileNotFoundException e) {
            System.out.println("Input file not found");
        }
        return null;
    }
}
