#!/usr/bin/env python3
import os, sys, shutil, subprocess

print(sys.argv[1])
subprocess.call(['R', '-f', sys.argv[1]])
subprocess.call(['xdg-open', 'Rplot001.png'])
#shutil.copy('R0001.png', 'R0002.png')
