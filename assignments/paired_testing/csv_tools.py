#!/usr/bin/env python3
def write_csv(filename, content):
    with open(filename, 'w') as csvfile:
        for line in content:
            for i, item in enumerate(line):
                csvfile.write(str(item))
                if i != len(line) - 1:
                    csvfile.write(',')
            csvfile.write('\n')

def read_csv(filename):
    with open(filename, 'r') as content:
        return [[v for v in line.replace('\n', '').split(',')] for line in content]

