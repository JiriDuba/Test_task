import csv
import re

def format_phone_number(digits):
    return f"+3 ({digits[0:3]})-{digits[3:6]}-{digits[6:8]}-{digits[8:10]}"

def process_names_and_numbers(data):
    for i, row in enumerate(data):
        if i > 0:  # Skip the header row
            if len(row) > 1:
                row[0], row[1] = re.split(r'\s+', row[0], 1) if ' ' in row[0] else (row[0], row[1])
            if len(row) > 2:
                row[1], row[2] = re.split(r'\s+', row[1], 1) if ' ' in row[1] else (row[1], row[2])

            if len(row) > 5:
                # Check if there is a phone number
                phone_digits = re.sub(r'\D', '', row[5])
                if phone_digits:
                    # Use the specified formatting for phone numbers
                    row[5] = format_phone_number(phone_digits)
                else:
                    # If no phone number, leave the column empty
                    row[5] = ''

def create_table(data):
    # Transpose the data to get columns as rows
    transposed_data = list(map(list, zip(*data)))

    # Find the maximum length for each column
    column_widths = [max(len(str(cell)) for cell in col) for col in transposed_data]

    # Iterate through each row and pad each cell with extra spaces to match the column widths
    formatted_rows = [
        ' '.join(str(cell).ljust(width) for cell, width in zip(row, column_widths))
        for row in data
    ]

    return formatted_rows

def read_csv(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    return data

def write_csv(file_path, formatted_rows):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        for row in formatted_rows:
            file.write(row + '\n')

def main():
    file_path = 'phonebook_raw.csv'
    raw_data = read_csv(file_path)

    # Process names and format numbers using regex
    process_names_and_numbers(raw_data)

    formatted_rows = create_table(raw_data)

    # Print the table to the console
    for row in formatted_rows:
        print(row)

    # Write the formatted table to output.csv
    write_csv('phonebook_sorted.csv', formatted_rows)

if __name__ == "__main__":
    main()
