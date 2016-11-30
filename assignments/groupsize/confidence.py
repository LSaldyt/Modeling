#!/usr/bin/env python3
from math import sqrt 
from generate import read_csv
from statistics import mean

def transpose(data):
    return list(map(list, zip(*data)))

def rss(data):
    resid = lambda x : x - mean(data) 
    return sum([resid(x) ** 2 for x in data])

def standard_dev(data):
    return sqrt(rss(data) / len(data))

def confidence(data):
    zcrit = 1.645
    sd    = standard_dev(data)
    dx    = zcrit * (sd / sqrt(len(data)))
    return mean(data), dx

def pretty_stats(data, labels, filename=None):
    csv_table = []
    for statset, label in zip(data, labels):
        print('\t%s' % label)
        average, dx = confidence(statset)
        print('\t\tConfidence   | %s +/- %s' % (round(average, 3), round(dx, 3)))
        print('\t\tStandard Dev | %s' % str(standard_dev(statset)))
        print('\t\tRSS          | %s' % str(rss(statset)))

        if filename is not None: # If we plan to write to a file
            csv_table.append([label, average, dx])
    if filename is not None:
        with open(filename, 'a') as csvfile:
            for row in csv_table:
                csvfile.write(','.join([str(item) for item in row]) + '\n')


def find_confidence(inputfile, outputfile):
    content = [[float(v) for v in row] for row in read_csv(inputfile)]
    small   = transpose(content[:20])
    medium  = transpose(content[20:40])
    large   = transpose(content[40:])

    labels  = ['Min + Max', 
               '2 * Mean', 
               '2 * Median', 
               'First Quartile + Third Quartile - Min', 
               'Max - Min', 
               '(2 * Median) - Min',
               'Max + (Standard Deviation / 2) - Min']

    print('Small')
    pretty_stats(small, labels, outputfile)
    print('Medium')
    pretty_stats(medium, labels, outputfile)
    print('Large')
    pretty_stats(large, labels, outputfile)

def main():
    print('Normal')
    find_confidence('estimates.csv', 'confidence.csv')
    print('Shifted')
    find_confidence('estimates_shifted.csv', 'confidence_shifted.csv')
    print('Skewed')
    find_confidence('estimates_skewed.csv', 'confidence_skewed.csv')

if __name__ == '__main__':
    main()

# Niel Stevenson
# Cryptonomicon
