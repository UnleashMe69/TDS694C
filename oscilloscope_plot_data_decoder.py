#!/usr/bin/env python3

"""Reads a file containing encoded plot data, decodes and then prints plot data in a csv file"""

import re
import os
import csv
import sys
import argparse

def main():
    """This is the main function. We will use regex to extract the key parameters
    Then we will decode the encoded data and prints the raw decoded data into a csv file
    so we can plot the data

    An example file containing the key data we need to extract is available
    with this Python script in the repository"""

    # Firstly, we need to extract the following parameters, using regex,
    # to decode sent by the oscilloscope

    xze = re.search('^.*XZE (.+);PT_O.*', first_line)
    if xze:
        xze = xze.group(1)
#        print("xze: ", end = '')
#        print(xze)

    xin = re.search('^.*XIN (.+);XZ.*', first_line)
    if xin:
        xin = xin.group(1)
#        print("xin: ", end = '')
#        print(xin)

    pt_o = re.search('^.*PT_O (.+);YUN.*', first_line)
    if pt_o:
        pt_o = pt_o.group(1)
#        print("pt_o: ", end = '')
#        print(pt_o)

    yze = re.search('^.*YZE (.+);:.*', first_line)
    if yze:
        yze = yze.group(1)
#        print("yze: ", end = '')
#        print(yze)

    ymu = re.search('^.*YMU (.+);YOF.*', first_line)
    if ymu:
        ymu = ymu.group(1)
#        print("ymu: ", end = '')
#        print(ymu)

    yof = re.search('^.*YOF (.+);YZE.*', first_line)
    if yof:
        yof = yof.group(1)
#        print("yof: ", end = '')
#        print(yof)

# We need to extract number of points (to plot the data)

    nr_p = re.search('^.*NR_P (.+);PT_F.*', first_line)
    if nr_p:
        nr_p = nr_p.group(1)
#        print("nr_p: ", end = '')
#        print(nr_p)

# Secondly, we need to extract all the 'y' values. Here's how:

# We get rid of everything that comes before :CURV

    pattern = re.compile(r'^.+:CURV.([\d]*)')

# At this stage, we got our 'y' values
# We strip the carriage return after the last 'y' value

    y_values = pattern.sub(r'\1', first_line.strip('\n'))

# We split all the 'y' values at every ','

    pattern = re.compile(',')
    y_list = pattern.split(y_values)

# All 'y' values are now in y_list


# Thirdly, we need to calculate X_n and Y_n using the following
# formulae found in the Programmer's manual
    # X_n = XZE + XIN * (n - PT_O)
    # Y_n = YZE + YMU * (y - YOF)

    print('[*] Decoding data and writing to file: {}\n'.format(outfile))

# Last but not least, we write the decoded data into a csv file

    with open(outfile, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['X_n', 'Y_n'])
        for index in range(0, int(nr_p)):
            filewriter.writerow([str(float(xze) + float(xin) *
                                     (index - int(pt_o))),
                                 str(float(yze) + float(ymu) * (int(y_list[index])
                                                                - float(yof)))])

    print('[*] Data succesfully decoded and written to file: {}!'.format(outfile))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                        help="Specify a file encoded data from the oscilloscope.")
    parser.add_argument("-o", '--outfile',
                        help="Writes the decoded data in a csv file")
    args = parser.parse_args()

    if not args.file and not args.outfile:
        parser.print_help()
        print("\n[-] Please specify an input file (-f) and the name of an", end='')
        print(" output file (-o plot_data.csv).\n")
        sys.exit(0)
    else:
        file = args.file
        outfile = args.outfile
        if not os.path.exists(file):
            print("\n[-] The file cannot be found or you do not have permission", end='')
            print(" to open the file. Please check the path and try again\n")
            sys.exit(0)
        print('\n[*] Reading file: {}\n'.format(file))
        with open(file, encoding="utf8", errors='ignore') as fh:
            first_line = fh.readline()

main()
