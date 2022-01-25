
import pandas, xport.v56, csv

with open('C:\\Users\\skbra\\PycharmProjects\\comprog01\\example.xpt', 'rb') as library:
    #library = xport.v56.load(f)
    with open('C:\\Users\\skbra\\PycharmProjects\\comprog01\\out.csv', 'rb') as out:
        writer = csv.DictWriter(out, [f['name'] for f in library.fields])
        for row in library:
            writer.writerow(row)