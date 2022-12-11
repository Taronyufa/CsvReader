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

    def get_column(self, key):
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

    def get_by_value(self, key, value):
        # checking if the key parameter is a valid key
        if key in self.keys:
            index = self.keys.index(key)
        else:
            return f'please return a valid key between {self.keys}'

        # taking all the element that have the value at the key element
        string = ''
        for i in range(len(self.titanic)):
            if self.titanic[i][index] == value:
                string += '\n' + str(self.titanic[i])
        return string

    def get_row(self, key):
        if (key < 892) and (key > 0):
            return str(self.titanic[key - 1])
        else:
            return 'index out of bound'

    def get_stats(self, key):
        # percent of male or survived in the ship
        if (key == 'Survived') or (key == 'Sex'):
            index = self.keys.index(key)

            pass

        # takes the values of all the passenger and then does the average
        elif (key == 'Fare') or (key == 'Age'):
            index = self.keys.index(key)
            result = 0
            for i in range(len(self.titanic)):
                if self.titanic[i][index] is not None:
                    result += float(self.titanic[i][index])
            return f'\n average {key} in titanic passenger is ' + str(result // 891)

        # no correct values in input
        else:
            return '\n insert a valid key between [Survived, Sex, Fare, Age]'


prova = CsvReader()

print(prova)
print(prova.get_column('Name'))
print('\n' + prova.get_row(50))
print(prova.get_by_value('Age', '22'))
print(prova.get_stats('Fare'))
