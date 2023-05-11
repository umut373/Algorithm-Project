import datetime
number_of_compression = 0

def brute_force(input, output, patternn):
    count = 0
    indexes = []
    a = 0
    global number_of_compression
    for i in range(len(input) - len(patternn) + 1):
        for j in range(len(patternn)):
            number_of_compression += 1
            if patternn[j] == input[j + i]:
                if j == len(patternn) - 1:
                    indexes.append(i)
                    count += 1
            else:
                break
    output_list = list(input)

    j = 0
    counter = 0
    continued = False
    while j < len(indexes):
        if not continued:
            if j == 0:
                output_list.insert(indexes[j] + counter, "<MARK>")
                counter += 1
            else:
                output_list.insert(indexes[j] + counter, "<MARK>")
                counter += 1
                output_list.insert(indexes[j-1] + len(patternn) + counter-1, "</MARK>")
                counter += 1
            continued = True
        else:
            if indexes[j] > indexes[j-1]+len(patternn):
                output_list.insert(indexes[j-1]+len(patternn)+counter, "</MARK>")
                continued = False
                counter += 1
                output_list.insert(indexes[j] + counter, "<MARK>")
                counter += 1
        j += 1
    if len(indexes) != 0:
        output_list.insert(indexes[-1]+len(patternn)+counter, "</MARK>")
    output.write("".join(output_list)
)
    return count


if __name__ == "__main__":
    input_file = open("random_input_1000.html", "r")
    output_file = open("output.html", "w")

    text = input_file.readline()
    input_file.close()
    pattern = input("Enter a pattern: ")

    start_time = datetime.datetime.now()
    brute_force_count = brute_force(text, output_file, pattern)
    exec_time = datetime.datetime.now() - start_time
    print(brute_force_count, "matches found\nExecution time is", exec_time.microseconds, "\nNumber of comprasions is ", number_of_compression)
