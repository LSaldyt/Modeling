#!/usr/bin/env python3
from fetch import fetch

#sheetId = '10JbiYwJH4eJHjSBS1mPj7lQ6RpZaP0PN1HgXu_gVKss'
sheetId = '13_OfCVf0pI1pDAV1GYtATZt2slUexAgonN7VGFKJprk'

def main():
    result = fetch(sheetId, rangeName='Data!A1:R57')
    values = result.get('values', [])
    for systemdata in values[1:]:
        name    = systemdata[2]
        x, y, z = tuple(systemdata[-4:-1])
        coords  = '(%s, %s, %s)' % (x, y, z)
        print('System: %s %s' % (name.rjust(20), coords.ljust(5)))


if __name__ == '__main__':
    main()
