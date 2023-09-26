# run the java file Search with different parameters, and save the results in a file
# the command to run the program is: java Search -Ec -R <number_of_runs> <test_file> <search_pattern> <num_of_tasks>

import os
import subprocess
import time

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
for num_of_tasks in range(2, 20):
    for num_of_threads in range(1, 20):
        output_path = f"results/problem4/{file_name}/ta={num_of_tasks},tr={num_of_threads}.txt"
        os.system(
            "java Search -Ef -R "
            + str(num_of_runs)
            + " -W 2 "
            + " "
            + test_path
            + " "
            + search_pattern
            + " "
            + str(num_of_tasks)
            + " "
            + str(num_of_threads)
            + " > "
            + output_path
        )
