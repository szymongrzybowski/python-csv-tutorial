import csv # start with importing CSV library

# now you need to obtain an access to CSV file you want to read. There are to ways to do that:
# 1) 'with open' method -- the suggested way -- file will automatically close after the operation is performed.
with open('path/to/csv/file', 'r', newline='') as csvfile: # specify a path to the csv file (e.g. C:/Users/folder1/file1.csv) or provide just a name of it (e.g. file1.csv) if your file is in the project directory
                                                     # actually, you don't need to write 'r' as it is a default option
                                                     # if csvfile is a file object, it should be opened with newline=''. Otherwise, you may face a problem with additional blank lines between two rows
                                                     
    # Here you have to decide whether you want to use standard reader or DictReader which organizes the data from table in a form of dictionary. Let's continue with csv.reader
    csv_reader = csv.reader(csvfile, delimeter=',') # delimeter= is used to set a separator which will separate data. The most popular one is comma but you can use also colon
    # the following line divides the table's rows into columns. Example: row[0] = first column
    for row in csv_reader: # for every row in the table 
        print(row) # you can print all rows in the table or...
        #            output: ['first_name', 'last_name'] <-- header
        #                    ['Eric', 'Idle']
        #                    ['John', 'Cleese']
        print(row[0]) # you can print only one column with specified number (in this example it's the first one)

        # or you can assign variables to the specified rows
        id = row[0]
        first_name = row[1]
        last_name = row[2]
        print(id, first_name, last_name) # therefore they can be used in other operations

# if you just want to print data from table, it is possible to skip csv.reader and do that with read() method
with open('path/to/csv/file', 'r', newline='') as csvfile:
    f = csvfile.read()
    print(f)
# output: first_name,last_name <-- header
#         Eric,Idle
#         John,Cleese

# 2) without 'WITH open()' and with read() method applied - this method is faster but you have to remember to close file with close() method
csvfile = open('path/to/csv/file', 'r')
f = csvfile.read()
print(f)
csvfile.close()

# There is also DictReader method which operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter
# Dictionary example: dict_example = {'first_name': 'Peter', 'last_name': 'Griffin'}
with open('path/to/csv/file', 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    for row in csv_reader:
        print(row['first_name'], row['last_name']) # prints columns 'first_name' and 'last_name'
        # output: Eric Idle   <-- only values
        #         John Cleese
        print(row['first_name'])
        # output: Eric        <-- only values
        #         John
        # alternatively:
        print(row)
        # output: {'first_name': 'Eric', 'last_name': 'Idle'}    <-- keys and values
        #         {'first_name': 'John', 'last_name': 'Cleese'}
        # in the case of DictReader it is impossible to print something like row[0]

# CSV reader in a function:
def read_file(filename): 
    with open(filename, 'r', newline='') as csvfile: 
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:    
            print(row)
# call a function
read_file('csv_file.csv') # or path to file

# here's how to read a specific row (or rows) from the table by using list comprehension (more on this topic: https://stackoverflow.com/questions/26464567/csv-read-specific-row)
with open('path/to/csv/file', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    specific_row = [row for idx, row in enumerate(csv_reader) if idx == 5 ] # read row no. 5
    specific_rows = [row for idx, row in enumerate(csv_reader) if idx in (5,10) ] # read rows from no. 5 to no. 10

# while reading a file you may want to skip header:
with open('path/to/csv/file', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader) # next() skips the first row
    for row in csv_reader:
        print(row)
# next() method can be used with csv.reader and csv.DictReader as well

# Complete code:

import csv

with open('path/to/csv/file', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        id = row[0]
        first_name = row[1]
        last_name = row[2]
        print(row)
        print(row[0])
        print(id, first_name, last_name)

with open('path/to/csv/file', 'r', newline='') as csvfile:
    f = csvfile.read()
    print(f)

csvfile = open('path/to/csv/file', 'r')
f = csvfile.read()
print(f)
csvfile.close()

with open('path/to/csv/file', 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    for row in csv_reader:
        print(row['first_name'], row['last_name'])
        print(row['first_name'])
        print(row)

def read_file(filename): 
    with open(filename, 'r', newline='') as csvfile: 
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:    
            print(row)

read_file('file1.csv')

with open('path/to/csv/file', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    specific_row = [row for idx, row in enumerate(csv_reader) if idx == 5] 
    specific_rows = [row for idx, row in enumerate(csv_reader) if idx in (5,10)]

with open('path/to/csv/file', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        print(row)