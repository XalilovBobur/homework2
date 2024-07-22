class FileReader:
    def __init__(self, filename) -> None:
        self.filename = filename
    
    def reader(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
                print(data)
        except FileNotFoundError:
            print("Fayl topilmadi tekshiring")


filereader = FileReader("example.txt")


filereader.reader()