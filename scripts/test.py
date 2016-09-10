#!/usr/bin/env python3
from fetch import fetch

sheetId = '10JbiYwJH4eJHjSBS1mPj7lQ6RpZaP0PN1HgXu_gVKss'

def main():
    result = fetch(sheetId, rangeName='Sheet1!A1:D9')
    values = result.get('values', [])[1:]
    print(values)


if __name__ == '__main__':
    main()
