import random
from english_words import get_english_words_set

random_input120 = open("random_input_120k.html", "w")
random_input150 = open("random_input_150k.html", "w")
random_input200 = open("random_input_200k.html", "w")
random_input1m = open("random_input_1m.html", "w")
web2lowerset = list(get_english_words_set(['web2'], lower=True))

random_input120.write("<HTML><BODY>")
for i in range(120000):
    random_input120.write(random.choice(web2lowerset))
random_input120.write("</BODY></HTML>")

random_input150.write("<HTML><BODY>")
for i in range(150000):
    random_input150.write(random.choice(web2lowerset))
random_input150.write("</BODY></HTML>")

random_input200.write("<HTML><BODY>")
for i in range(200000):
    random_input200.write(random.choice(web2lowerset))
random_input200.write("</BODY></HTML>")

random_input1m.write("<HTML><BODY>")
for i in range(1000000):
    random_input1m.write(random.choice(web2lowerset))
random_input1m.write("</BODY></HTML>")

# this is for check if there is a multiple exist
# we don't check since this is from a library
"""i = 0; cond1 = len(words); cond2 = len(words)
while i < cond1:
    j = i+1
    while j < cond2:
        print(words[i] + " " + words[j])
        if words[i] == words[j]:
            words.pop(j)
            cond2-=1
            cond1-=1
        j += 1
    i += 1
print(words)"""

