import 'dart:io';
import 'dart:math';

void main() async {
  final file = File('../1.txt');
  if (!await file.exists()) {
    print('File not found: 1.txt');
    return;
  }

  final lines = await file.readAsLines();
  List<int> leftList = [];
  List<int> rightList = [];

  for (var line in lines) {
    final parts = line.split(RegExp(r"\s+")).map(int.parse).toList();
    if (parts.length == 2) {
      leftList.add(parts[0]);
      rightList.add(parts[1]);
    }
  }

  if (leftList.isEmpty || rightList.isEmpty) {
    print('No valid data found in 1.txt.');
    return;
  }

  leftList.sort();
  rightList.sort();

  int totalDistance = 0;
  for (int i = 0; i < leftList.length; i++) {
    totalDistance += (leftList[i] - rightList[i]).abs();
  }

  print('Total Distance: $totalDistance');

  Map<int, int> leftCounts = {};
  Map<int, int> rightCounts = {};

  for (var num in leftList) {
    leftCounts[num] = (leftCounts[num] ?? 0) + 1;
  }
  for (var num in rightList) {
    rightCounts[num] = (rightCounts[num] ?? 0) + 1;
  }

  int similarityScore = 0;
  for (var entry in leftCounts.entries) {
    final num = entry.key;
    final leftCount = entry.value;
    final rightCount = rightCounts[num] ?? 0;
    similarityScore += num * leftCount * rightCount;
  }

  print('Similarity Score: $similarityScore');
}