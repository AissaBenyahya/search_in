#!/usr/bin/python3
import sys
import os
import getopt

def search(files):
    wordlist = []
    if os.path.exists(files[0]):
        with open(files[0], "r") as f:
            for line in f:
                print(line)
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
    print("usage: searchin.py -i <inputfile> [-o outputfile]")
    sys.exit(2)

def argHandler(argc, argv):
    inputfile = ''
    outputfile = ''
    if argc < 2:
        usage()
    else:
        try:                                                                           
            opts, args = getopt.getopt(argv, "hi:o:", ["help=", "input=", "output"])     
        except getopt.GetoptError:                                        
            print("usage: searchin.py -i <inputfile> [-o outputfile]")   
            sys.exit(2)
        for opt, arg in opts:
            if opt == "-h":
                usage()
            elif opt in ("-i", "--input"):
                inputfile = arg
            elif opt in ("-o", "--output"):
                outputfile = arg
            
        if not opts:    
            usage()
        return [inputfile, outputfile]
       
def main():
    files = argHandler(len(sys.argv), sys.argv[1:])
    search(files)


if __name__ == "__main__":
    main()  
