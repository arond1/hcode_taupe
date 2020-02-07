import solveur
import os

def parser():
    f = open('./hcode_taupe/a_example.in', "r")
    lines1 = f.readlines()
    f.close()
    print(lines1)
    line_one = lines1[0].split(' ')
    line_two = lines1[1].split(' ')
    print(line_one)
    print(line_two)
    line_one[1] = line_one[1].split('\n')[0]
    print(line_one)
    line_two[len(line_two)-1] = line_two[len(line_two)-1].split('\n')[0]
    print(line_two)
    slice = int(line_one[0])
    types = int(line_one[1])
    values = []
    for i in line_two:
        values.append(int(i))
    solveur.solveur(slice, types, values)

parser()
