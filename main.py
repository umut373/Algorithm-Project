'''
# Burak Karayagli - 150121824
# Ege Keklikci - 150121029
# Umut Ozil - 150121019
'''

import datetime

def generate_shift_table():
    #iterating through the pattern
    for i in range(p_length - 1):
        #setting the value of the key to the length of the pattern - 1 - i
        shift_table[pattern[i]] = p_length - 1 - i

def generate_good_suffix_table():
    i = p_length 
    j = p_length + 1
    bpos = [0] * (p_length + 1) #bpos initialized with 0s
    bpos[i] = j

    # case 1 and borders
    while i > 0:
        # if character at position i-1 is not equivalent to character at j-1, 
        # continue searching to right of the pattern for border
        while j <= p_length and pattern[i - 1] != pattern[j - 1]:
            # if the preceding characters of borders are different,
            # assign the shift value to corresponfing index to good_suffix_table
            if good_suffix_table[p_length - j] == 0:
                good_suffix_table[p_length - j] = j - i #distance between left and right border of suffix

            j = bpos[j] # use the next widest border

        # characers matched, new border is found
        i -= 1
        j -= 1
        bpos[i] = j

    # case 2
    j = bpos[0]
    for i in range(p_length + 1):
        # set the elements of good_suffix_table to 
        # border position of the pattern, if it has no value
        if good_suffix_table[p_length - i] == 0:
            good_suffix_table[p_length - i] = j

        # if the suffix shorter than border position, 
        # use the next widest border
        if i == j:
            j = bpos[j]

#function for printing the tables
def print_tables():
    print("\n-----Bad Symbol Table-----")
    for element in shift_table :
        print(element, end = ' -> ')
        print(shift_table[element])
    print("* ->", p_length, "\n")

    print("-----Good Suffix Table-----")
    print("k     shift")
    for i in range(p_length+1) :
        print(i, end = '\t')
        print(good_suffix_table[i])
    print("\n")

def brute_force():
    for i in range(t_length - p_length + 1):
        j = 0
        #checking every character in the pattern
        while j < p_length:
            number_of_comparisons[0] += 1
            if pattern[j] != text[j + i]:
                break
            j += 1
        #if the pattern is found
        if j == p_length:
            number_of_occourences[0] += 1

def horspool():
    i = p_length - 1
    #while i is less than the length of the text
    while i < t_length:
        k = 0
        #while k is less than the length of the pattern and
        #starting from the end of the pattern, the pattern is equal to the text at i - k
        #increment k
        while k < p_length and pattern[p_length - 1 - k] == text[i - k]:
            number_of_comparisons[1] += 1
            k += 1
        #after the while loop, if k is equal to the length of the pattern
        #incremnt the number of occourences by 1
        if k == p_length:
            number_of_occourences[1] += 1
        else :
            number_of_comparisons[1] += 1
        #if pattern is not equal to the text at i
        #increment i by the value of the shift table at text[i]
        if text[i] in shift_table:
            i += shift_table[text[i]]
        #else increment i by the length of the pattern
        else:
            i += p_length


def boyer_moore():
    i = 0
    #iterate through the text
    while i < (t_length - p_length):
        k = 0
        #check if characters match starting from the right of the pattern
        while k < p_length and text[p_length + i - k - 1] == pattern[p_length - k - 1]:
            number_of_comparisons[2] += 1
            k += 1      

        #pattern is found
        if k == p_length:
            if read_count == 1:
                index = i
            else :
                index = ((read_count-1)*char_number) - p_length + 1 + i #calculate the index of the pattern in the text
            indexes.append(index)

            number_of_occourences[2] += 1
            i += good_suffix_table[p_length] - 1
        #shifting the pattern
        else:
            number_of_comparisons[2] += 1
            d1 = max((shift_table.get(text[p_length+i-k-1], p_length) - k), 1) # bad-symbol
            d2 = good_suffix_table[k] # good-suffix
            i += max(d1, d2) - 1
             
        i += 1

#function for running the algorithms and calculating the execution times
def search():
    start = datetime.datetime.now()
    brute_force()
    end = datetime.datetime.now()
    execetuion_times[0] += (end - start).total_seconds() * 1000

    start = datetime.datetime.now()
    horspool()
    end = datetime.datetime.now()
    execetuion_times[1] += (end - start).total_seconds() * 1000

    start = datetime.datetime.now()
    boyer_moore()
    end = datetime.datetime.now()
    execetuion_times[2] += (end - start).total_seconds() * 1000

#function for marking the occurrences and making the output file
def mark_occurrences():
    i = 0
    k = 0
    last_index = 0 #last index of the text that is added to the output file
    #iterate through the indexes
    while i < len(indexes):
        index1 = indexes[i]
        output = ""
        #adding the opening tag of the mark
        output = input_file.read(index1 -  last_index) + "<MARK>"
        j = i + 1
        temp = index1
        #iterate through the indexes and finding the last overlapping occourence
        while j < len(indexes):
            index2 = indexes[j]
            if index2 >= temp + p_length:
                break   
            temp = index2
            j += 1

        index2 = indexes[j - 1]
        #adding the closing tag of the mark
        output += input_file.read(index2 + p_length - index1) + "</MARK>"
        
        output_file.write(output)
        
        last_index = input_file.tell()
        i = j

    #adding the rest of the text to the output file
    output_file.write(input_file.read())
    
#function for printing the results
def print_results():
    print("-----Results-----")

    print("Brute Force:")
    print("Number of comparisons:", number_of_comparisons[0])
    print("Number of occourences:", number_of_occourences[0])
    print("Execution time:", execetuion_times[0], "ms\n")

    print("Horspool:")
    print("Number of comparisons:", number_of_comparisons[1])
    print("Number of occourences:", number_of_occourences[1])
    print("Execution time:", execetuion_times[1], "ms\n")

    print("Boyer Moore:")
    print("Number of comparisons:", number_of_comparisons[2])
    print("Number of occourences:", number_of_occourences[2])
    print("Execution time:", execetuion_times[2], "ms\n")


if __name__ == '__main__' :
    # names of the input and output files
    input_path = "input.html"
    output_path = "output.html"

    input_file = open(input_path, "r") #opening the input file

    pattern = input("Enter a pattern: ") 
    p_length = len(pattern)

    shift_table = {}
    good_suffix_table = [0] * (p_length + 1)

    generate_shift_table()
    generate_good_suffix_table()
    print_tables()

    #lists for storing the results
    #index 0 for brute force
    #index 1 for horspool
    #index 2 for boyer moore
    number_of_comparisons = [0, 0, 0]
    number_of_occourences = [0, 0, 0]
    execetuion_times = [0.0, 0.0, 0.0]

    #list for store the indexes where the pattern is found
    indexes = []

    char_number = 500 #number of characters to be read at a time
    read_count = 0 #number of times the input file is read
    text = ""
    #this loop is for reading the input file piece by piece 
    while 1 :
        read = input_file.read(char_number) 
        #if the end of the file is reached break the loop
        if not read :
            break
        read_count += 1   
        t_length = len(text)
        #add the last p_length-1 characters of the previous read to the current read
        text = text[t_length-p_length+1:] + read
        t_length = len(text)
        search()

    input_file.close() 
    print_results()

    input_file = open(input_path , "r") #reopen the input file for marking the occourences
    output_file = open(output_path , "w") #open the output file for writing
    mark_occourences()
    input_file.close()
    output_file.close()