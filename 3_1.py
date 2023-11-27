import os

directory = "3_1"
file_list = os.listdir(directory)

file_data = []
for file_name in file_list:
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_data.append((file_name, len(lines), lines))

file_data.sort(key=lambda x: x[1])

result_file_path = 'result.txt'
with open(result_file_path, 'w', encoding='utf-8') as result_file:
    for file_info in file_data:
        file_name, lines_count, lines = file_info

        result_file.write(f"{file_name}\n{lines_count}\n")
        result_file.writelines(lines)
        result_file.write("\n\n")
with open(result_file_path, 'r', encoding='utf-8') as result_file:
    print(result_file.read())

