import datetime
count = 0
def brute_force():
    index = 0
    for i in range(len(text) - len(pattern)+1):
        for j in range(len(pattern)):
            if pattern[j] == text[j+i]:
                if j == len(pattern)-1:
                    output_file.write(text[index: i] + "<MARK>" + pattern + "</MARK>")
                    index = i + j + 1
                    global count
                    count += 1
            else:
                break
    output_file.write(text[index:len(text)])


if __name__ == "__main__":
    input_file = open("random_input_120k.html", "r")
    output_file = open("output.html", "w")

    text = input_file.readline()
    input_file.close()
    pattern = input("Enter a pattern: ")

    start_time = datetime.datetime.now()
    brute_force()
    exec_time = datetime.datetime.now() - start_time
    print(count,"matches found\nExecution time is", exec_time.microseconds)
