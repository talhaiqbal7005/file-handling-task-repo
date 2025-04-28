# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    # TODO: Create a new text file and write "Hello, world!" to it.
    pass
    with open("hello.txt", "w") as file:
    file.write("Hello, World!")
def task2_read_file():
    # TODO: Read the contents of a file and print them to the console.
    pass
    with open("hello.txt", "r") as file:
    content = file.read()
    print(content)
def task3_append_file():
    # TODO: Append a new line of text to an existing file.
    pass
    with open("hello.txt", "a") as file:
         file.write("\nYour Name")  # Replace "Your Name" with your actual name
def task4_count_lines():
    # TODO: Count and print the number of lines in a file.
    pass
    with open("hello.txt", "r") as file:
                                      line_count = len(file.readlines())
    print(f"Number of lines: {line_count}")
def task5_find_word():
    # TODO: Find whether a specific word exists in the file and how many times.
    pass
    filename = "example.txt"  # Replace with your file name
    with open(filename, "r") as file:
     content = file.read()                 
    python_count = content.count("Python")
    print(f"The word 'Python' appears {python_count} times.")
def task6_copy_file():
    # TODO: Copy the contents of one file to another.
    pass
    source_file = "source.txt"  
destination_file = "destination.txt"  

with open(source_file, "r") as src, open(destination_file, "w") as dest:
    dest.write(src.read())
def task7_replace_word():
    # TODO: Replace a specific word in the file with another word.
    pass
    filename = "example.txt"  

with open(filename, "r") as file:
    content = file.read()
content = content.replace("Java", "Python")
with open(filename, "w") as file:
    file.write(content)
def task8_read_csv():
    # TODO: Read a CSV file and print each row.
    pass
    import csv

csv_file = "students.csv"  # Replace with your CSV file name

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])  


def task9_write_csv():
    # TODO: Write a list of dictionaries to a CSV file.
    pass
    import csv

students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 92}
]

csv_file = "students.csv"

with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(students)


def task10_json_file():
    # TODO: Create a JSON file from a Python dictionary and read it back.
    pass
import json

data = {
    "students": [
        {"name": "Alice", "score": 90},
        {"name": "Bob", "score": 85},
        {"name": "Charlie", "score": 92}
    ]
}

json_file = "data.json"

# Write data to JSON file
with open(json_file, "w") as file:
    json.dump(data, file, indent=4)

# Read data back
with open(json_file, "r") as file:
    content = json.load(file)
    print(content)

