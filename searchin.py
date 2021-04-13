#!/usr/bin/python3
import sys
import os
import getopt
import codecs
import re

def search(files):
    wordlist = []
    count = 0
    if os.path.exists(files[1]):
        with open(files[1], "r") as f:
            line = f.readlines()
            wordlist = [x.strip() for x in line]
    else:
        print("ERROR: The file {} is not exist".format(files[1]))

    if os.path.exists(files[0]):
        with codecs.open(files[0], "r", 'iso-8859-1') as sf:
            content = sf.read().split("\n")

        for i, line in enumerate(content):
            for word in wordlist:
                if word in line:
                    print("{} {} ".format(i,line))
                    count = count + 1
                    break
                else:
                    continue
        print("Number of matched lines are {}".format(count))
    else:
        print("ERROR: The file {} is not exist".format(files[0]))

def usage():
    print("""\
                 ### --------------------------------------------------------------------###
                 |   Version: 1.0                                                          |
                 |   Description: searchin is a command line searches inside a file        |
                 |   for a givin words by the user and returns number of matched           |
                 |   lines and their position in the file.                                 |
                 |   Licence: searchin is free software released under the "GNU General    |
                 |   Public License v3.0                                                   |
                 |   Copyright (c) 2021 Aissa Ben yahya - https://github.com/AissaBenyahya |
                 ###---------------------------------------------------------------------###
                 """)
    print("usage: searchin.py -f <file_to_search_in> -w <wordlistfile> [-o outputfile]")
    sys.exit(2)

def argHandler(argc, argv):
    wordlist = ''
    outputfile = ''
    sfile = '' # The file to search in
    if argc < 2:
        usage()
    else:
        try:                                                                           
            opts, args = getopt.getopt(argv, "hf:w:o:", ["help=", "file=", "wordlist=", "output"])     
        except getopt.GetoptError:                                        
            print("usage: searchin.py -f <file_to_search_in> -w <wordlistfile> [-o outputfile]")
            sys.exit(2)
        for opt, arg in opts:
            if opt == "-h":
                usage()
            elif opt in ("-f", "--file"):
                sfile = arg
            elif opt in ("-w", "--wordlist"):
                wordlist = arg
            elif opt in ("-o", "--output"):
                outputfile = arg
            
        if not opts:    
            usage()
        return [sfile, wordlist, outputfile]
       
def main():
    files = argHandler(len(sys.argv), sys.argv[1:])
    search(files)


if __name__ == "__main__":
    main()  
