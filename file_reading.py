import csv # start with importing CSV library

# now you need to obtain an access to CSV file you want to read. There are to ways to do that:
# 1) 
with open('path\to\csv\file', 'r', newline='') as f: # specify a path to the csv file or provide just a name of it (e.g. file1.csv) if your file is in the project directory
                                                     # actually, you don't need to write 'r' as it is a default option
                                                     # if f file is a file object, it should be opened with newline=''
  #
  csv_reader = csv.reader(f, delimeter=',')
  #
  for row in f:
    print()
  
