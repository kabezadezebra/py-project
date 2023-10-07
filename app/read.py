import csv
#cada una de las columnas viene como un array
"""
def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")#ATEncion al delimitar(revisar si el csv usa "," o ";")
    for row in reader:
      print("***" * 5)
      print(row)

if __name__ == "__main__":
  read_csv("./app/data.csv")
"""
#como diccionario
"""
def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader) # iterar manualmente la primera fila
    print(header)

if __name__ == "__main__":
  read_csv("./app/data.csv")
  """
#para q la llave sea el nombre de la columna(primera fila)
"""
def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    print(header)
    for row in reader:# listas de tuplas(keys, values)
      iterable = zip(header, row)
      print(list(iterable))
      country_dict = {key: value for key, value in iterable} #diccionario (key: value)
      print(country_dict)
      

if __name__ == "__main__":
  read_csv("./app/data.csv")



"""
#retornar una lista con todos esos diccionarios
def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    data = []
    #print(header)
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data
      

if __name__ == "__main__":
  data = read_csv("./app/data.csv") #DATA
  print(data[0]) #recordar que el 0 es para llamar al primer diccionario(la cuenta empieza en 0)
