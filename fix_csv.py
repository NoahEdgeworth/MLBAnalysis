import csv

# Open the existing CSV file for reading and a new CSV file for writing
with open('master_batting_stats.csv', 'r', newline='') as input_file, \
        open('fixed_file.csv', 'w', newline='') as output_file:

    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    for row in reader:
        # Shift data in each row to the right
        shifted_row = [None] + row[:-1]

        # Write the shifted row to the new CSV file
        writer.writerow(shifted_row)

print("CSV file fixed successfully.")
