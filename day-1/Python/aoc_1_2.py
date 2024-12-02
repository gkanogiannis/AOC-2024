from collections import Counter

def read_input(file_path):
    left_list = []
    right_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    right_counts = Counter(right_list)
    
    similarity_score = sum(left * right_counts[left] for left in left_list)
    
    return similarity_score

if __name__ == "__main__":
    file_path = "../1.txt"
    left_list, right_list = read_input(file_path) 
    
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {similarity_score}")