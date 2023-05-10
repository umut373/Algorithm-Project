import datetime

def brute_force():
    print(len(text) - len(pattern)-1)
    for i in range(len(text) - len(pattern)-1):
        for j in range(len(pattern)):
            if pattern[j] == text[j+i]:
                if j == len(pattern)-1:
                    output = text[:i] + "<MARK>" + pattern + "</MARK>" + text[i + len(pattern):]
                    output_file.write(output)
            else:
                break

if __name__ == "__main__":
    input_file = open("input.html", "r")
    output_file = open("output.html", "w")

    text = input_file.readline()
    input_file.close()
    pattern = input("Enter a pattern: ")

    start_time = datetime.datetime.now()
    brute_force()
    exec_time = datetime.datetime.now() - start_time
    print("Execution time is", exec_time.microseconds)