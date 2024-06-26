
import csv

class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]

if __name__ == '__main__':
    file_path = "example.csv"
    reader = CSVReader(file_path)
    data = reader.read_csv()
    
    print("Content of the CSV file:")
    for row in data:
        print(row)
