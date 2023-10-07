#import utils
"""
data = [
  {
    "country": "colombia",
    "population": 500
  },
  {
    "country": "bolivia",
    "population": 300
  }
]

def run():#con esta funcion, no se ejecutara el archivo de manera forzosa al importarlo pero ya no se ejecutara dese la terminal(example.py)
  keys, values = utils.get_population()
  print(keys, values)
  
  country = input("pais: ")
  result = utils.population_by_country(data, country)
  print(result)

"""
import utils # clave valor
import read # de aqui se optiene la DATA
import charts # forma del grafico

def run():
  data = read.read_csv("data.csv")# especificar dentro de la carpeta actual(app)
  #filtrar solo latam
  data = list(filter(lambda item: item["Continent"] == "South America", data))
  
  countries = list(map(lambda x: x["Country/Territory"], data))
  porcentages = list(map(lambda x: x["World Population Percentage"], data))
  charts.generate_pie_charts(countries, porcentages)

  country = input("pais: ")
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"], labels, values)

# 
if __name__ == "__main__":#con este if este modulo se puede ejecutar como un script desde la terminal al archivo  (def run)solucion
  run()
#print(utils.A)
