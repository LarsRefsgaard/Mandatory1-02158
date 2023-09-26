# run the java file Search with different parameters, and save the results in a file
# the command to run the program is: java Search -Ec -R <number_of_runs> <test_file> <search_pattern> <num_of_tasks>

import os

os.system("javac Search.java")

# the path of the java file
path = "Search.java"

# the file name
file_name = "shakespeare"
search_pattern = '"Something is rotten in the state of Denmark"'

# the path of the test files
test_path = f"test_files/{file_name}.txt"

# the path of the output file, where the quatations marks are not present in the search pattern and only the first 8 characters of the search pattern are used
# also replace the %d with the number of tasks

# the number of times to run the program
num_of_runs = 10

# run the program
for num_of_tasks in range(1, 160):
    output_path = f"results/problem3/{file_name}/tasks={num_of_tasks}.txt"
    os.system(
        "java Search -Ec -R "
        + str(num_of_runs)
        + " -W 2 "
        + " "
        + test_path
        + " "
        + search_pattern
        + " "
        + str(num_of_tasks)
        + " > "
        + output_path
    )
