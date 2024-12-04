import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day3Part2 {
    public static void main(String[] args) throws IOException {
        String input = new String(Files.readAllBytes(new File("../day-3.input.txt").toPath()));

        Pattern mulPattern = Pattern.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)");
        Pattern doPattern = Pattern.compile("do\\(\\)");
        Pattern dontPattern = Pattern.compile("don't\\(\\)");

        Matcher mulMatcher = mulPattern.matcher(input);
        Matcher doMatcher = doPattern.matcher(input);
        Matcher dontMatcher = dontPattern.matcher(input);

        boolean isEnabled = true;
        int totalSum = 0;

        int index = 0;
        while (index < input.length()) {
            if (mulMatcher.find(index) && mulMatcher.start() == index) {
                if (isEnabled) {
                    int x = Integer.parseInt(mulMatcher.group(1));
                    int y = Integer.parseInt(mulMatcher.group(2));
                    totalSum += x * y;
                }
                index = mulMatcher.end();
            } else if (doMatcher.find(index) && doMatcher.start() == index) {
                isEnabled = true;
                index = doMatcher.end();
            } else if (dontMatcher.find(index) && dontMatcher.start() == index) {
                isEnabled = false;
                index = dontMatcher.end();
            } else {
                index++;
            }
        }

        System.out.println("The sum of valid multiplications is: " + totalSum);
    }
}