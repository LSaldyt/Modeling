#!/usr/bin/env python
import os, sys, subprocess

subprocess.call(['R', '-f', sys.argv[1]])
subprocess.call(['xdg-open', 'Rplots.pdf'])
