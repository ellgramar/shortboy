import sys # for input args
import struct


def main():
    print("Generating binary file for {print_argv()}\n")
    # argv[1] is the output file
    ofile = open(sys.argv[1], "wb")
    # argv[2:] are the input files
    for i in range(2, len(sys.argv)):
        print("Generating binary file for {sys.argv[i]}\n")
        try:
            infile = open(sys.argv[i], "r")
        except FileNotFoundError:
            print("File not found: " + sys.argv[i])
            sys.exit(1)
        for line in infile:
            hex_val = line.strip()
            if hex_val: #ignore empty lines
                 # Convert hex string to an integer, then pack it as a uint16_t
                binary_value = struct.pack('>H', int(hex_val, 16))
                ofile.write(binary_value)

        infile.close()
        


if __name__ == "__main__":
    main()