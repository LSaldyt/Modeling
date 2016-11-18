#!/usr/bin/env python3
from math import sqrt 

def transpose(data):
    return list(map(list, zip(*data)))

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def standard_dev(data):
    resid = lambda x : x - 100
    summed_resids_squared = sum([resid(x) ** 2 for x in data])
    return sqrt(summed_resids_squared / len(data))

def confidence(data):
    zcrit = 1.645
    sd    = standard_dev(data)
    dx    = zcrit * (sd / sqrt(len(data)))
    return mean(data), dx

def pretty_confidence_stats(data, labels, filename=None):
    csv_table = []
    for statset, label in zip(data, labels):
        print(label)
        average, dx = confidence(statset)
        print('Confidence of %s +/- %s' % (average, dx))
        if filename is not None: # If we plan to write to a file
            csv_table.append([label, average, dx])
    if filename is not None:
        with open(filename, 'a') as csvfile:
            for row in csv_table:
                csvfile.write(','.join(row) + '\n')



def main():
    with open('estimates.csv', 'r') as estimates:
        content = [[float(v) for v in line.replace('\n', '').split(',')] for line in estimates]

    content = transpose(content)
    small   = content[:3]
    medium  = content[3:6]
    large   = content[6:9]

    labels  = ['Min + Max', '2 * Mean', '2 * Median']

    filename = 'confidence.csv'
    print('Small')
    pretty_confidence_stats(small, labels, filename)
    print('Medium')
    pretty_confidence_stats(medium, labels, filename)
    print('Large')
    pretty_confidence_stats(large, labels, filename)

if __name__ == '__main__':
    main()
