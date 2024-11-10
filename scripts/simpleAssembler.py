#!/usr/bin/env python3

# imports
import sys # for input args
import array as array # for array management


# print list of argv
# Checks for positive number of elements
def print_argv():
    try:
        print(sys.argv[1:])
        return
    except IndexError:
        print("Missing input files")
        sys.exit(1)
        return

# splits input string into an array of strings (chars)
def splitter(ascii, index):
    try:
        ascii_arr = ascii.split()
    except ValueError:
        print("Error in line: " + str(index))
        sys.exit(2)
    if len(ascii) == 4:
        retval = ascii.split()
    elif len(ascii) > 4:
        print("Too many values in line: " + str(index))
        sys.exit(3)
    elif len(ascii) < 4:
        print("Not enough values in line: " + str(index))
        sys.exit(4)
    return

# converts each char in array to hex value
def ascii_to_int(ascii_arr,index):
    int_arr = []
    try:
        for i in range(len(ascii_arr)):
            int_arr[i].append(int(ascii_arr[i], 16))  
        return int_arr
    except ValueError:
        print("Cant convert line to hex: " + str(index))
        sys.exit(5)



        


# python script to convert text file of hex values 
# to a binary file of uint16_t values

# parse input file name and location

# parse output file name and location

# read input file line
# for each line, convert it to uint16_t
# append uint16_t to output file



def main():
    print("Generating binary file for {print_argv()}\n")
    for i in range(1, len(sys.argv)):
        print("Generating binary file for {sys.argv[i]}\n")
        try:
            f = open(sys.argv[i], "r")
        except FileNotFoundError:
            print("File not found: " + sys.argv[i])
            sys.exit(6)
        hex_arr = []
        ascii_arr = splitter(sys.argv[i],i)
        for j in range(len(ascii_arr)):
            hex_arr.append(ascii_to_int(ascii_arr[j], j))



if __name__ == "__main__":
    main()