import csv
def main():
    extensions = loadExtensions()
    input_file = inputFile()
    getExtenion(input_file, extensions)

def getExtenion(file:str,dic:dict):
    for suffix, file_type in dic.items():
        if file.endswith(suffix):
            print(file_type[0])  # Retorna o primeiro valor da lista
            return
    print('application/octet-stream')

def inputFile():
    return input("File name: ").strip().lower()

def loadExtensions(f='extensions.csv'):

    with open(f, mode = 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        extensionDict = {}
        
        for row in reader:
            extensionDict[row[0]] = row [1:]
    return extensionDict
main()