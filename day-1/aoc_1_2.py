from collections import Counter

def read_input(file_path):
    left_list = []
    right_list = []
    
    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into two numbers and append to respective lists
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    """
    Calculate the similarity score based on the given logic:
    Each number in the left list is multiplied by its occurrence count in the right list.
    """
    # Count occurrences of each number in the right list
    right_counts = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = sum(left * right_counts[left] for left in left_list)
    
    return similarity_score

# Example usage
if __name__ == "__main__":
    # Input lists (example or from file)
    file_path = "1.txt"  # Adjust the path to your input file
    left_list, right_list = read_input(file_path)  # Reuse the function from part 1
    
    # Calculate similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {similarity_score}")