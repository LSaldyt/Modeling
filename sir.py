#!/usr/bin/env python3

from graph import graph
from fetch import fetch

#def fetch(spreadsheetId, rangeName='Sheet1!A1:D9'):

if __name__ == '__main__':
    sheetID = '1__7u0X0Jy1KnKPfB_R6PPHqKoDpBunPr_XTSEM8yCfg'
    results = fetch(sheetID, 'Sheet1!A1:D10')
    values  = results['values']
    values  = [list(x) for x in zip(*values)]
    values  = [l[1:] for l in values]
    convert = lambda item : float(item.replace('%', ''))
    values  = [[convert(item) for item in l] for l in values]
    print(values)
    graph(values[0], values[1], values[2:])


