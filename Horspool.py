import codecs
import datetime

file_name = "resource.html"

counter = [0]


#Shift table maker
def shift_table(pattern):
    table = {}
    #iterating through the pattern
    for i in range(len(pattern) - 1):
        #setting the value of the key to the length of the pattern - 1 - i
        table[pattern[i]] = len(pattern) - 1 - i
    return table


def Horspool(pattern, file_name, counter, indexes = []):
    with codecs.open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
    
    
    #making the shift table
    table = shift_table(pattern)
    #setting i to the length of the pattern - 1
    i = len(pattern) - 1
    #while i is less than the length of the text
    while i < len(text):
        k = 0
        #while k is less than the length of the pattern and
        #starting from the end of the pattern, the pattern is equal to the text at i - k
        #increment k
        while k < len(pattern) and pattern[len(pattern) - 1 - k] == text[i - k]:
            counter[0]+=1
            k += 1

        #this while loop is increase k until the mismatch or the pattern is found

        #after the while loop, if k is equal to the length of the pattern
        #pattern is found at print the index
        if k == len(pattern):
            #index is i - k + 1
            index = i - k + 1
            indexes.append(index)
            print("Found at index " + str(i - k + 1))
        #if pattern is not equal to the text at i
        #increment i by the value of the shift table at text[i]
        if text[i] in table:
            counter[0]+=1
            i += table[text[i]]
        #else increment i by the length of the pattern
        else:
            counter[0]+=1
            i += len(pattern)
    
    return indexes

#write <mark> </mark> around the pattern
#patterns are found at indexes
def mark_indexes(indexes, pattern, file_name):
    with codecs.open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
    #setting the start and end of the pattern
    new_pattern = "<mark>" + pattern + "</mark>"

    #for each match
    for index in indexes:
        text = text[:index] + new_pattern + text[index + len(pattern):]
    
    #create a new html file with the marked pattern
    with codecs.open("marked.html", "w", encoding="utf-8") as f:
        f.write(text)

  
# text = "0a1b2c3d4e5-6-7-8-9"
#        #0123456789
# new_text = "!!!" + text[3:6] + "!!!"
# #replace the text at index 3 to 6 with new_text
# text = text[:3] + new_text + text[6:]
# print(text)

pattern = "worker"

start = datetime.datetime.now()
found_indexes = Horspool(pattern, file_name, counter)
end = datetime.datetime.now()

mark_indexes(found_indexes, pattern, file_name)
print("Number of comparisons: " + str(counter[0]))

#print in milliseconds
print("Time taken: " + str((end - start).total_seconds() * 1000) + "ms")