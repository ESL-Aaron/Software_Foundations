# Date Created: 04/02/2025
# Description: Assesment code test
# Created by: Aaron Barbizan
# data_processing.py

import sys
from datetime import datetime  

# This function serves to read the data from the input_data file.
# It reads the data line by line and converts it to a float and return a list of numeric value. 
# It also print responses, in case the file is not found or if values are not only numebrs.
def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [float(line.strip()) for line in file.readlines()]
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid data in the file. Ensure all values are numbers.")
        sys.exit(1)

# This function process the calculations of the sums and the average and returns then.
def perform_calculations(data):
    total = sum(data)
    average = total / len(data)
    return total, average

# This function writes the results to the output file.
def write_output(file_path, total, average, data):
    with open(file_path, 'w') as file:
        file.write("\nNumber to Animal Mapping:\n")
        file.write("+--------+-------------+\n")
        file.write("| Number |    Animal   |\n")
        file.write("+--------+-------------+\n")
        for number in data:
            animal = number_to_animal(number)
            file.write(f"| {int(number):<6} | {animal:<11} |\n")
        file.write("+--------+-------------+\n")
        file.write(f"|Total:  | {total}       |\n")
        file.write(f"|Average:| {average}      |\n")
        file.write("+--------+-------------+\n")

def number_to_animal(number):
    # This function process the numbers and returns the corresponding animal.
    # The numbers are divided into ranges and each range is assigned an animal.
    if 1 <= number <= 4:
        return "Ostrich"
    elif 5 <= number <= 8:
        return "Eagle"
    elif 9 <= number <= 12:
        return "Donkey"
    elif 13 <= number <= 16:
        return "Butterfly"
    elif 17 <= number <= 20:
        return "Dog"
    elif 21 <= number <= 24:
        return "Goat"
    elif 25 <= number <= 28:
        return "Ram"
    elif 29 <= number <= 32:
        return "Camel"
    elif 33 <= number <= 36:
        return "Snake"
    elif 37 <= number <= 40:
        return "Rabbit"
    elif 41 <= number <= 44:
        return "Horse"
    elif 45 <= number <= 48:
        return "Elephant"
    elif 49 <= number <= 52:
        return "Rooster"
    elif 53 <= number <= 56:
        return "Cat"
    elif 57 <= number <= 60:
        return "Alligator"
    elif 61 <= number <= 64:
        return "Lion"
    elif 65 <= number <= 68:
        return "Monkey"
    elif 69 <= number <= 72:
        return "Pig"
    elif 73 <= number <= 76:
        return "Peacock"
    elif 77 <= number <= 80:
        return "Turkey"
    elif 81 <= number <= 84:
        return "Bull"
    elif 85 <= number <= 88:
        return "Tiger"
    elif 89 <= number <= 92:
        return "Bear"
    elif 93 <= number <= 96:
        return "Deer"
    elif 97 <= number <= 100:
        return "Cow"
    else:
        return "N/A"  # For numbers outside the range
    
# This function generates a report containing the time the code is executed.
# The name of the input and output files and the calculations performed.
def generate_report(file_path, input_file, output_file, total, average, data):
    """Generate a report summarizing the processing activity."""
    execution_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'w') as file:
        file.write("Data Processing Report\n")
        file.write("======================\n")
        file.write(f"Execution Date: {execution_date}\n")
        file.write(f"Input File: {input_file}\n")
        file.write(f"Output File: {output_file}\n")
        file.write("\nNumber to Animal Mapping:\n")
        file.write("+--------+-------------+\n")
        file.write("| Number |    Animal   |\n")
        file.write("+--------+-------------+\n")
        for number in data:
            animal = number_to_animal(number)
            file.write(f"| {int(number):<6} | {animal:<11} |\n")
        file.write("+--------+-------------+\n")
        file.write(f"\nTotal of Values: {total}\n")
        file.write(f"Average of Values: {average}\n")
        file.write("======================\n")
        file.write("End of Report\n")

# This is the main function that calls all the other functions.
# It also checks if the input file is provided and if not, it prints an error message.
# It also prints a message when the processing is complete.   
def main():
    if len(sys.argv) != 2:
        print("Usage: python data_processing.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "output_data.txt"
    report_file = "report.txt"

    # Read data from input file
    data = read_data(input_file)

    # Perform calculations
    total, average = perform_calculations(data)

    # Write results to output file
    write_output(output_file, total, average, data)

    # Generate report
    generate_report(report_file, input_file, output_file, total, average, data)
    # Print completion message
    print(f"Processing complete. Results written to {output_file} and {report_file}.")
# This is the entry point of the code, where the main function is called.
if __name__ == "__main__":
    main()
               