import re

input_file_path = 'phonebook_raw.csv'
output_file_path = 'phonebook_sorted.csv'

def format_phone_number(digits):
    return f"+3 ({digits[0:3]})-{digits[3:6]}-{digits[6:8]}-{digits[8:10]}"

def create_table(data):
    # Find the maximum length for each column 
    column_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

    # Iterate through each row and pad each cell with extra spaces to match the column widths
    formatted_rows = [
        ' '.join(str(cell).ljust(width) for cell, width in zip(row, column_widths))
        for row in data
    ]

    return formatted_rows

# Read input data from the file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    input_data = input_file.read()

# Process the data and create a table
output_data = []
for line in input_data.splitlines():
    # Count the number of commas in the line
    comma_count = line.count(',')

    # Add extra commas if needed to match the desired count
    if comma_count < 7:  # 7 is the desired number of commas in each row
        line += ',' * (7 - comma_count)

    # Separate names in the beginning
    row = line.split(',')
    if len(row) > 1:
        row[0], row[1] = re.split(r'\s+', row[0], 1) if ' ' in row[0] else (row[0], row[1])
    if len(row) > 2:
        row[1], row[2] = re.split(r'\s+', row[1], 1) if ' ' in row[1] else (row[1], row[2])

    # Format phone number if available
    if len(row) > 5:
        # Check if there is a phone number
        phone_digits = re.sub(r'\D', '', row[5])
        if phone_digits:
            # Use the specified formatting for phone numbers
            row[5] = format_phone_number(phone_digits)
        else:
            # If no phone number, leave the column empty
            row[5] = ''

    # Append the modified line to the output data
    output_data.append(row)

# Merge duplicates based on the first two columns
merged_data = [output_data[0]]

for i in range(1, len(output_data)):
    current_names = output_data[i][:2]
    previous_names = merged_data[-1][:2]

    if current_names == previous_names:
        output_data[i] = [current if current != '' else previous for current, previous in zip(output_data[i], merged_data[-1])]
    else:
        merged_data.append(output_data[i])  # Add the row to merged_data if names are different

# Format the table using the create_table function
formatted_table = create_table(merged_data)

# Join the modified lines and write to the output file
modified_data = "\n".join(formatted_table)
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(modified_data)
