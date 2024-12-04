import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day3MullItOver {
    public static void main(String[] args) throws IOException {
        String input = new String(Files.readAllBytes(new File("../day-3.input.txt").toPath()));

        Pattern pattern = Pattern.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)");
        Matcher matcher = pattern.matcher(input);

        int totalSum = 0;

        while (matcher.find()) {
            int x = Integer.parseInt(matcher.group(1));
            int y = Integer.parseInt(matcher.group(2));
            totalSum += x * y;
        }

        System.out.println("The sum of valid multiplications is: " + totalSum);
    }
}