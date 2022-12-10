import csv


class CsvReader:

    def __init__(self):

        self.titanic = []
        csv_reader = csv.DictReader(open('titanic.csv', mode='r'))
        for row in csv_reader:

            # extracting all the elements from the current row and replacing the "," in the name element
            dummy = [*row.values()]
            dummy[3] = dummy[3].replace(',', '')

            # replacing every blank space with None
            for i in range(len(dummy)):
                if dummy[i] == '':
                    dummy[i] = None
            self.titanic.append(dummy)

        # trying to optimize the code smh
        csv_reader = csv.reader(open('titanic.csv', mode='r'))
        self.keys = csv_reader.__next__()

    def __str__(self):
        file = str(self.keys)
        for i in range(len(self.titanic)):
            file += "\n" + str(self.titanic[i])
        return file

    def print_column(self, key):

        # taking the index of key
        if key in self.keys:
            index = self.keys.index(key)
        else:
            return f'please write a valid key between {self.keys}'

        # extracting all the elements that need to be printed
        string = ""
        for i in range(len(self.titanic)):
            string += "\n" + self.titanic[i][index]
        return string

    def print_row(self, key):
        if (key < 892) and (key > 0):
            return self.titanic[key - 1]
        else:
            return 'Index out of bound'


prova = CsvReader()

print(prova)
print(prova.print_column('Name'))
print('\n' + prova.print_row(0))
