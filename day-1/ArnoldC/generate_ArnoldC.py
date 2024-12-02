def generate_arnoldc_code(file_path, output_path):
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
            
    with open(output_path, 'w') as arnold_file:
        arnold_file.write("IT'S SHOWTIME\n\n")

        for i, value in enumerate(left_list):
            arnold_file.write(f"HEY CHRISTMAS TREE LeftList{i + 1}\n")
            arnold_file.write(f"YOU SET US UP {value}\n")

        for i, value in enumerate(right_list):
            arnold_file.write(f"HEY CHRISTMAS TREE RightList{i + 1}\n")
            arnold_file.write(f"YOU SET US UP {value}\n")

        arnold_file.write("\nHEY CHRISTMAS TREE TotalDistance\n")
        arnold_file.write("YOU SET US UP 0\n")
        arnold_file.write("HEY CHRISTMAS TREE Difference\n")
        arnold_file.write("YOU SET US UP 0\n")

        for i in range(len(left_list)):
            arnold_file.write(f"GET TO THE CHOPPER Difference\n")
            arnold_file.write(f"HERE IS MY INVITATION LeftList{i + 1}\n")
            arnold_file.write(f"GET DOWN RightList{i + 1}\n")
            arnold_file.write("YOU HAVE BEEN TERMINATED\n")

            arnold_file.write("IF IT'S NOT TRUE Difference\n")
            arnold_file.write("    GET TO THE CHOPPER Difference\n")
            arnold_file.write("    HERE IS MY INVITATION Difference\n")
            arnold_file.write("    GET UP Difference\n")
            arnold_file.write("    YOU HAVE BEEN TERMINATED\n")
            arnold_file.write("YOU HAVE BEEN TERMINATED\n")

            arnold_file.write(f"GET TO THE CHOPPER TotalDistance\n")
            arnold_file.write("HERE IS MY INVITATION TotalDistance\n")
            arnold_file.write("GET UP Difference\n")
            arnold_file.write("YOU HAVE BEEN TERMINATED\n")

        arnold_file.write("TALK TO THE HAND TotalDistance\n")

        arnold_file.write("\nYOU HAVE BEEN TERMINATED\n")

    print(f"ArnoldC program generated at {output_path}")


if __name__ == "__main__":
    file_path = "../1.txt"
    output_path = "day1.arnoldc"
    generate_arnoldc_code(file_path, output_path)