import csv


class CsvReader:

    keys = {}
    titanic = []

    def __init__(self):
        with open('titanic.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self.keys = {", ".join(row)}

                #extracting all the elements from the current row and replacing the "," in the name element
                dummy = [*row.values()]
                dummy[3] = dummy[3].replace(',', '')
                self.titanic.append(dummy)
                line_count += 1

    def __str__(self):
        file = str(self.keys)
        for i in range(len(self.titanic)):
            file += "\n" + str(self.titanic[i])
        return file


prova = CsvReader()

print(prova)