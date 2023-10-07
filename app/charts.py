import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values): #DINAMICO
#def generate_bar_chart(): NO DINAMICO
  #labels = ["a","b","c"] 
  #values = [100, 200, 80]
  
  fig, ax = plt.subplots() #(ax)se refiere a las coordenadas a graficar
  ax.bar(labels, values) #(.bar)asignar los valores de la grafica(,)
  plt.savefig(f"./imgs/{name}.png")
  plt.close() #(.show)mostrar la grafica (segira mostrando el programa hasta que se interrumpa)

def generate_pie_charts(labels, values):
  fig, ax = plt.subplots() 
  ax.pie(values, labels = labels)
  #ax.pie(values, labels = labels)#(pie) Grafica de pastel, hay que indicar cuales son lo labels (reglas de la libreria)
  ax.axis("equal") #(.axis)para organizar esta grafica en el centro, (equal) forma de circulo
  plt.savefig("pie.png")
  plt.close()
  
#if __name__ == "__main__": #No dinamico
  #generate_bar_chart()


if __name__ == "__main__": #DINAMICO
  #labels = ["a","b","c"] 
  #values = [10, 40, 800]
  #generate_bar_chart(labels, values) #Dinamico
  generate_pie_charts()
  