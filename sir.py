#!/usr/bin/env python3

from graph import graph
from fetch import fetch

#def fetch(spreadsheetId, rangeName='Sheet1!A1:D9'):

if __name__ == '__main__':
    sheetID = '1_TQhb0gI7CgD7JSZFukxBDOnYQKKetx5OAPgIDW0fqI'
    #sheetID = '1__7u0X0Jy1KnKPfB_R6PPHqKoDpBunPr_XTSEM8yCfg'        # From URL
    result  = fetch(sheetID, 'Sheet1!A1:D10')                       # 10 x 5 matrix
    values  = result['values']
    values  = [list(x) for x in zip(*values)]                       # Transpose cells
    values  = [l[1:] for l in values]                               # Get rid of titles
    convert = lambda item : float(item.replace('%', ''))            # Convert to floats
    values  = [[convert(item) for item in l] for l in values]       # ^
    graph(values, colors = [None, '#ffcc66', '#cc0000', '#9999ff']) # S in tan, I in red, R in blue


