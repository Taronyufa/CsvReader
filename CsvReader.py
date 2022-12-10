import csv


class CsvReader:

    def __init__(self):
        self.titanic = []
        csv_reader = csv.DictReader(open('titanic.csv', mode='r'))
        for row in csv_reader:

            # removing the ',' from the Name
            dummy = [*row.values()]
            dummy[3] = dummy[3].replace(',', '')

            # replacing blank spaces with None
            for i in range(len(dummy) - 1):
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
        # checking if the key parameter is a valid key
        if key in self.keys:
            index = self.keys.index(key)
        else:
            return f'please return a valid key between {self.keys}'

        # taking all the elements at key index
        string = ''
        for i in range(len(self.titanic)):
            string += '\n' + self.titanic[i][index]
        return string

    def print_by_value(self, key, value):
        pass

    def print_row(self, key):
        if (key < 892) and (key > 0):
            return str(self.titanic[key - 1])
        else:
            return 'index out of bound'

    def statistic_sex(self):
        pass


prova = CsvReader()

print(prova)
print(prova.print_column('Name'))
print('\n' + prova.print_row(1))
