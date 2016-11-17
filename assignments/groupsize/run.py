#!/usr/bin/env python
import os, sys, shutil, subprocess

subprocess.call(['R', '-f', sys.argv[1]])
subprocess.call(['xdg-open', 'Rplots.pdf'])
shutil.copy('Rplots.pdf', 'old_Rplots.pdf')
