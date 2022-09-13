# 'append' mode adds new rows at the end of the table. Almost identical to 'write' mode

import csv # start with importing CSV library

my_list = ['Peter', 'Griffin']

# csv.writer function
with open('path/to/csv/file', 'a', newline='') as csvfile: # set 'a' mode
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerows(my_list)

columns = ['first_name', 'last_name']

data_dict = {'first_name': 'John', 'last_name': 'Cleese'}

# csv.DictWriter function
with open('path/to/csv/file', 'a', newline='') as csvfile: # set 'a' mode
    csv_writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=',') # use fieldnames=
    csv_writer.writerow(data_dict)
