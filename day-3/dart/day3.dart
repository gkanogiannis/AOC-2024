import 'dart:io';

void main(List<String> arguments) async {
  if (arguments.length < 1) {
    print("Usage: dart day3.dart <input_file>");
    exit(1);
  }

  final inputFile = arguments[0];

  try {
    final lines = await File(inputFile).readAsLines();
    final part1Result = calculatePart1(lines);
    final part2Result = calculatePart2(lines);
    print("Part 1 Result: $part1Result");
    print("Part 2 Result: $part2Result");
  } catch (e) {
    print("Error reading file: $e");
    exit(1);
  }
}

/// Part 1: Sum the results of all valid mul(X, Y) commands
int calculatePart1(List<String> lines) {
  final validCommands = findMulCommands(lines);
  return validCommands.map(evalMulCommand).fold(0, (a, b) => a + b);
}
int calculatePart2(List<String> lines) {
  bool isEnabled = true; // Start with mul commands enabled
  int total = 0;

  for (var line in lines) {
    // Debug: Print the current line being processed
    print("Processing line: $line");

    // Handle toggling of the isEnabled flag
    if (line.contains("do()")) {
      isEnabled = true;
      print("Found do(), enabling commands.");
      continue;
    }
    if (line.contains("don't()")) {
      isEnabled = false;
      print("Found don't(), disabling commands.");
      continue;
    }

    // Process commands only if isEnabled is true
    if (isEnabled) {
      final commands = findMulCommands([line]); // Extract mul commands
      print("Extracted Commands: $commands");

      for (var command in commands) {
        final result = evalMulCommand(command); // Evaluate the command
        print("Evaluating command: $command -> Result: $result");
        total += result;
      }
    } else {
      print("Skipping line because commands are disabled.");
    }
  }

  print("Final Part 2 Total: $total");
  return total;
}

List<String> findMulCommands(List<String> lines) {
  List<String> mulCommands = [];
  for (var line in lines) {
    // Debug: Print the current line being parsed
    print("Extracting commands from line: $line");

    // Extract commands using a regex or string parsing
    final matches = RegExp(r"mul\(\d+,\d+\)").allMatches(line);
    for (var match in matches) {
      final command = match.group(0)!;
      mulCommands.add(command);
    }
  }

  print("Commands extracted: $mulCommands");
  return mulCommands;
}

int evalMulCommand(String command) {
  // Debug: Print the command being evaluated
  print("Evaluating command: $command");

  final numbers = RegExp(r"\d+").allMatches(command).map((m) => int.parse(m.group(0)!)).toList();
  if (numbers.length == 2) {
    final result = numbers[0] * numbers[1];
    print("Result of $command: $result");
    return result;
  }

  print("Invalid command: $command");
  return 0; // Return 0 for invalid commands
}