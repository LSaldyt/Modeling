#!/usr/bin/env python3

def transpose(data):
    return list(map(list, zip(*data)))

def average_dist(data):
    pass

with open('estimates.csv', 'r') as estimates:
    content = [[float(v) for v in line.replace('\n', '').split(',')] for line in estimates]

content = transpose(content)
small   = content[:3]
medium  = content[3:6]
large   = content[6:9]
