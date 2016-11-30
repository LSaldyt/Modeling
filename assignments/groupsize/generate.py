#!/usr/bin/env python3
from random import randint, random

def gen_experiment(experiment_size=20, a=0, b=100, skew=False):
    generator = lambda : randint(a, b) * (1 if not skew else random())
    measured = []
    for i in range(experiment_size):
        generated = generator() 
        while generated in measured:
            generated = generator() 
        measured.append(generated)
    return measured

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

def generate(filename, a, b, skew=False):
    spacing = [' '] * 7
    content = []
    content.append(['Small:'])
    for i in range(20):
        content.append(spacing + gen_experiment(20, a, b, skew))
    content.append(['Med:'])
    for i in range(20):
        content.append(spacing + gen_experiment(50, a, b, skew))
    content.append(['Large:'])
    for i in range(20):
        content.append(spacing + gen_experiment(80, a, b, skew))
    write_csv(filename, content)

def main():
    generate('measured.csv', 0, 100)
    generate('measured_shifted.csv', 100, 200)
    generate('measured_skewed.csv', 0, 100, True)

if __name__ == '__main__':
    main()
