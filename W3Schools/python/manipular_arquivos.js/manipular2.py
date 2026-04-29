import os

path = os.path.dirname(__file__)

f = open(path + "/myfile.txt", "x")
f.close()