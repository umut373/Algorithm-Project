import datetime
number_of_compression = 0

def brute_force(input, output, patern):
    count = 0
    indexes = []
    a = 0
    patern_length = len(patern)
    input_length = len(input)

    global number_of_compression
    for i in range(input_length - patern_length + 1):
        for j in range(patern_length):
            number_of_compression += 1
            if patern[j] == input[j + i]:
                if j == patern_length - 1:
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
                output_list.insert(indexes[j-1] + patern_length + counter - 1, "</MARK>")
                counter += 1
            continued = True
        else:
            if indexes[j] > indexes[j-1]+patern_length:
                output_list.insert(indexes[j-1] + patern_length + counter, "</MARK>")
                continued = False
                counter += 1
                output_list.insert(indexes[j] + counter, "<MARK>")
                counter += 1
        j += 1
    if len(indexes) != 0:
        output_list.insert(indexes[-1] + patern_length + counter, "</MARK>")
    output.write("".join(output_list))
    return count


if __name__ == "__main__":
    input_file = open("input.html", "r")
    output_file = open("output.html", "w")

    text = input_file.readline()
    input_file.close()
    pattern = input("Enter a pattern: ")

    start_time = datetime.datetime.now()
    brute_force_count = brute_force(text, output_file, pattern)
    exec_time = datetime.datetime.now() - start_time
    print(brute_force_count, "matches found\nExecution time is", exec_time.microseconds/1000000, "seconds \nNumber of comprasions is ", number_of_compression)
