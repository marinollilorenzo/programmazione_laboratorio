class CSVFile:
    
    def __init__(self, filepath):
        self.filepath = filepath
    
    def get_data(self):
        lst = []
        with open (self.filepath, 'r') as fi:
            for line in fi.readlines():
                lst.append(line.strip("\n").split(","))
        return lst




csv_file = CSVFile("DOCS/shampo.csv")
lst = csv_file.get_data()
print(lst)
print("\n\n\n")
for item in lst:
    print(item)

