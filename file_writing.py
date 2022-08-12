import csv # start with importing CSV library

# Creating CSV file:
# 'write' mode is intended to fill the new CSV file (i.e. blank file) with data. If you use 'w' mode on a CSV file that contains some data, its contents will be overwritten.
# you can use csv.writer to create new CSV files in the chosen directory. After executing the script below, the new CSV file will be automatically created in the chosen directory.
# of course, you can create csv files via Excel, Google Sheets or Notepad

my_list = ['Paul', 'Smith'] # will be used later

# opens the CSV file. Opened file will be marked as a 'csvfile' (variable)
with open('path/to/csv/file', 'w', newline='') as csvfile: # remember to use newline=''
    # standard csv.writer
    csv_writer = csv.writer(csvfile, delimiter=',')
    # write a single row
    csv_writer.writerow(['Eric', 'Idle'])
    # write data from list
    csv_writer.writerow(my_list)
    # write many rows
    csv_writer.writerows(
        ['John', 'Cleese'],
        ['Robert', 'Smith'],
        ['Peter', 'Griffin']
    )

# csv.DictWriter:
columns = ['first_name', 'last_name'] # will be used as a header in fieldnames parameter

data_dict = {'first_name': 'John', 'last_name': 'Cleese'}

with open('path/to/csv/file', 'w', newline='') as csvfile:
    # dict writer
    csv_writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=',') # set fieldnames= parameter
    csv_writer.writerow(data_dict)
    csv_writer.writerow({'first_name': 'Robert', 'last_name': 'Smith'})
    # writerows() in DictReader is slightly trickier
    csv_writer.writerows([
        {'first_name': 'Robert', 'last_name': 'Smith'},
        {'first_name': 'Paul', 'last_name': 'Jones'}
    ])

# writeheader() method will add header on top of the table 
# firstly, you have to create a list that will contain column names
header = ['first_name', 'last_name']
# writeheader() only works with DictWriter
csv_writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=',')
csv_writer.writeheader()
# scroll down to find full code with writeheader()

# csv.writer inside a function
def filewriting(filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(['John', 'Smith'])

filewriting('file1.csv')

# Complete code:

my_list = ['Paul', 'Smith']

with open('path/to/csv/file', 'w', newline='') as csvfile: 
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(['Eric', 'Idle'])
    csv_writer.writerow(my_list)
    csv_writer.writerows(
        ['John', 'Cleese'],
        ['Robert', 'Smith'],
        ['Peter', 'Griffin']
    )

columns = ['first_name', 'last_name'] 

data_dict = {'first_name': 'John', 'last_name': 'Cleese'}

with open('path/to/csv/file', 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=',') 
    csv_writer.writerow(data_dict)
    csv_writer.writerow({'first_name': 'Robert', 'last_name': 'Smith'})
    csv_writer.writerows([
        {'first_name': 'Robert', 'last_name': 'Smith'},
        {'first_name': 'Paul', 'last_name': 'Jones'}
    ])

header = ['first_name', 'last_name']

with open('path/to/csv/file', 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=',')
    csv_writer.writeheader()
    csv_writer.writerow({'first_name': 'Robert', 'last_name': 'Smith'})

def filewriting(filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(['John', 'Smith'])
        
filewriting('file1.csv')