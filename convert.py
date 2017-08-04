import csv
from io import StringIO

quotedData = StringIO()
m = ()

with open('doc/gubernatorial_candidates.csv') as f:
    reader = csv.reader(f)
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for row in reader:
        firsts = ''.join([word[0:1].upper() for word in row[0].split(' ')])
        row[1:3] = [' '.join(map(str, row[1:3]))]
        # print (row[1:3])

        # row.insert(0,firsts)
        a = tuple(row)
        print (a[0])
        m = m + (a)
        # writer.writerow(a)



print(m)
# print (quotedData2.getvalue())
# p = List(quotedData.getvalue())