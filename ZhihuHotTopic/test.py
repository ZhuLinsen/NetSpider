import csv

with open('data.csv', 'w') as csvfile:
    writer=csv.writer(csvfile,delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1001', 'tom', '22'])
    