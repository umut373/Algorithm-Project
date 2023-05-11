import BruteForce
import datetime

input_file = open("random_input_1m.html", "r")
output_file = open("output.html", "w")

text = input_file.readline()
input_file.close()
pattern = input("Enter a pattern: ")
start_time = datetime.datetime.now()
brute_force_count = BruteForce.brute_force(text, output_file, pattern)
exec_time = datetime.datetime.now() - start_time
print(brute_force_count, "matches found\nExecution time is", exec_time.microseconds, "\nNumber of comprasions is ", BruteForce.number_of_compression)