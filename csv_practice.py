import csv     # imports the csv module

# with open('csvfile.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'])

with open('csvfile.csv', 'rt') as f:
    reader = csv.DictReader(f)
    exampleData = list(reader)

    for i in range(len(exampleData)):
        for key in reader:
            print "key: %s , value: %s" % (key, reader[key])
        print exampleData[i]['first_name'], exampleData[i]['last_name']
        print exampleData[i]
    # print exampleData[1]['first_name']
    # print exampleData[2]
    # for row in reader:
    #     print row


       
# f = open('csvfile.csv')
# csv_f = csv.reader(f)

# for row in csv_f:
#   print row
# # .reader(new_variable)
# This allows you to grab information from the file opened
# .next()
# This functions reads one line and returns it in list format