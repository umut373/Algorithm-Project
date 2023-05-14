import random

random_bitstring2m = open("random_bitstring_2m.html", "w")
random_bitstring3m = open("random_bitstring_3m.html", "w")
random_bitstring5m = open("random_bitstring_5m.html", "w")
random_bitstring10m = open("random_bitstring_10m.html", "w")

random_bitstring2m.write("<HTML><BODY>")
for i in range(2000000):
    random_bitstring2m.write(str(random.randint(0, 1)))
random_bitstring2m.write("</BODY></HTML>")

random_bitstring3m.write("<HTML><BODY>")
for i in range(3000000):
    random_bitstring3m.write(str(random.randint(0, 1)))
random_bitstring3m.write("</BODY></HTML>")

random_bitstring5m.write("<HTML><BODY>")
for i in range(5000000):
    random_bitstring5m.write(str(random.randint(0, 1)))
random_bitstring5m.write("</BODY></HTML>")

random_bitstring10m.write("<HTML><BODY>")
for i in range(10000000):
    random_bitstring10m.write(str(random.randint(0, 1)))
random_bitstring10m.write("</BODY></HTML>")