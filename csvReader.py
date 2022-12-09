import csv

class csvReader:

    keys = {}
    titanic = []

    def reader(self):
        with open('titanic.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self.keys = {", ".join(row)}
                self.titanic.append({", ".join(row.values())})
                line_count += 1

    def __str__(self):
        file = str(self.keys)
        for i in range (len(self.titanic)):
            file += "\n" + str(self.titanic[i])
        return file


prova = csvReader()

prova.reader()
print(prova)