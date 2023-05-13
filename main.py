import datetime

def generate_shift_table():
    #iterating through the pattern
    for i in range(p_length - 1):
        #setting the value of the key to the length of the pattern - 1 - i
        shift_table[pattern[i]] = p_length - 1 - i

def generate_good_suffix_table():
    i = p_length 
    j = p_length + 1
    bpos = [0] * (p_length + 1)
    bpos[i] = j

    while i > 0 :
        while j <= p_length and pattern[i-1] != pattern[j-1] :
            if good_suffix_table[p_length-j] == 0 :
                good_suffix_table[p_length-j] = j - i

            j = bpos[j]
        
        i -= 1
        j -= 1
        bpos[i] = j

    j = bpos[0]
    for i in range(p_length  + 1) :
        if good_suffix_table[p_length-i] == 0 :
            good_suffix_table[p_length-i] = j

        if i == j :
            j = bpos[j]

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
        while j < p_length:
            number_of_comparisons[0] += 1
            if pattern[j] != text[j + i]:
                break
            j += 1
        number_of_comparisons[0] += 1
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
        #pattern is found at print the index
        if k == p_length:
            number_of_occourences[1] += 1
            #index is i - k + 1
        else :
            number_of_comparisons[1] += 1
        #if pattern is not equal to the text at i
        #increment i by the value of the shift table at text[i]
        if text[i] in shift_table:
            i += shift_table[text[i]]
        #else increment i by the length of the pattern
        else:
            i += p_length
    
    #return indexes

def boyer_moore():
    i = 0
    while i < (t_length - p_length) :
        k = 0
        while k < p_length and text[p_length+i-k-1] == pattern[p_length-k-1] :
            number_of_comparisons[2] += 1
            k += 1      

        if k == p_length :
            if read_count == 1 :
                index = i
            else :
                index = ((read_count-1)*char_number) - p_length + 1 + i
            indexes.append(index)

            number_of_occourences[2] += 1
            i += good_suffix_table[p_length] - 1
        else :
            number_of_comparisons[2] += 1
            d1 = max((shift_table.get(text[p_length+i-k-1], p_length) - k), 1)
            d2 = good_suffix_table[k]
            i += max(d1, d2) - 1
             
        i += 1

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

def mark_occourences(): 
    i = 0
    k = 0
    end_indexes = [0]
    while i < len(indexes):
        index1 = indexes[i]
        output = ""
        output = input_file.read(index1-end_indexes[k]) + "<MARK>"
        j = i+1
        end = 0
        temp = index1
        while j < len(indexes):
            index2 = indexes[j]
            if index2 >= temp + p_length:
                break   
            temp = index2
            j += 1
 
        index2 = indexes[j-1]
        output += input_file.read(index2+p_length-index1) + "</MARK>"

        end += index2 + p_length
        end_indexes.append(end)
        k += 1
        
        output_file.write(output)
        i = j

    output_file.write(input_file.read())
    
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


input_file = open("input.html", "r")

pattern = input("Enter a pattern: ")
p_length = len(pattern)

shift_table = {}
good_suffix_table = [0] * (p_length + 1)

generate_shift_table()
generate_good_suffix_table()
print_tables()

number_of_comparisons = [0, 0, 0]
number_of_occourences = [0, 0, 0]
execetuion_times = [0.0, 0.0, 0.0]

indexes = []

char_number = 250
read_count = 0
text = ""
while 1 :
    read = input_file.read(char_number) 
    if not read :
        break
    read_count += 1   
    t_length = len(text)
    text = text[t_length-p_length+1:] + read 
    t_length = len(text)
    search()

input_file.close()
print_results()

input_file = open("input.html", "r")
output_file = open("output.html", "w")
mark_occourences()
input_file.close()
output_file.close()