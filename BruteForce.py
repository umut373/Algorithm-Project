import datetime

import BoyerMoore

count = 0
def brute_force(input, output, patternn):
    index = 0
    for i in range(len(input) - len(patternn)+1):
        for j in range(len(patternn)):
            if patternn[j] == input[j+i]:
                if j == len(patternn)-1:
                    output.write(input[index: i] + "<MARK>" + patternn + "</MARK>")
                    index = i + j + 1
                    global count
                    count += 1
            else:
                break
    output.write(input[index:len(input)])


if __name__ == "__main__":
    input_file = open("random_input_1m.html", "r")
    output_file = open("output.html", "w")

    text = input_file.readline()
    input_file.close()
    pattern = input("Enter a pattern: ")

    start_time = datetime.datetime.now()
    brute_force_count = brute_force(text, output_file, pattern)
    exec_time = datetime.datetime.now() - start_time
    print(count, "matches found\nExecution time is", exec_time.microseconds)
