# cowsay is an external libary , the official name is open-source package in the website(pypi.org)
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex(f"hello, {sys.argv[1]}")