import csv


class CsvReader:

    keys = {}
    titanic = []

    def __init__(self):

        csv_reader = csv.DictReader(open('titanic.csv', mode='r'))
        for row in csv_reader:
            #extracting all the elements from the current row and replacing the "," in the name element
            dummy = [*row.values()]
            dummy[3] = dummy[3].replace(',', '')
            for i in range(len(dummy) - 1):
                if dummy[i] == '':
                    dummy[i] = 'None'
            self.titanic.append(dummy)

        #trying to optimize the code smh
        csv_reader = csv.reader(open('titanic.csv', mode='r'))
        self.keys = csv_reader.__next__()



    def __str__(self):
        file = str(self.keys)
        for i in range(len(self.titanic)):
            file += "\n" + str(self.titanic[i])
        return file


prova = CsvReader()

print(prova)