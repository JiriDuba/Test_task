
file_names = ['1.txt', '2.txt', '3.txt']
line_counts = {}

# Count lines in each file and store their content
for file_name in file_names:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]  # Remove trailing newline characters
        line_counts[file_name] = {
            'line_count': len(lines),
            'content': lines
        }

# Sort files based on line counts in ascending order
sorted_files = sorted(line_counts.items(), key=lambda x: x[1]['line_count'])

# Generate output string with the sorted files and their content
output = ''
for file_name, file_info in sorted_files:
    output += file_name + '\n'
    output += str(file_info['line_count']) + '\n'
    output += '\n'.join(file_info['content']) + '\n\n'

# Write the output to a new file
output_file = 'merget_files.txt'
with open(output_file, 'w') as file:
    file.write(output)