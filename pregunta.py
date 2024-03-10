"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

#data = pd.read_table("clusters_report.txt")
#print(data.iloc[0:1])
#data_dict = data.to_dict(orient='list')
#print(data_dict)

palabras = []
dicc = {'cluster':[],
        'cantidad_de_palabras_clave':[],
        'porcentaje_de_palabras_clave':[],
        'principales_palabras_clave':[]}

def ingest_data():
    cluster = open("clusters_report.txt", mode="r")
    for line in cluster:
        line = line.rstrip()
        palabras.append(line)
    header = palabras[:2]
    #datos = palabras[4:]
    #print(palabras)
    #print("hola",palabras[4][3].isdigit())
    
    for p in range(4,len(palabras)):
        linea = palabras[p]
        n_elementos = 3  # Ejemplo: quieres separar los primeros 3 elementos
        
        if linea.strip() != "":
            #print("linea",linea)
            if linea.split()[0].isdigit() == True:
                #print("claro que si")
            # Dividir el texto por espacios
                partes = linea.split()

            # Separar las primeras N partes y luego unir el resto
                parte1 = partes[:n_elementos]
                #parte2 = " ".join(partes[2:3])
                parte2 = " ".join(partes[n_elementos:])
                parte2 = parte2.replace('%', '').lstrip()

            # Combinar la parte separada y la parte unida en una lista
                resultado = parte1 +[parte2]
                #print("res",resultado)
            else:
                resultado[-1] += linea.lstrip()
                #print("linea",linea)

        if int(resultado[0]) not in dicc['cluster']:
            dicc['cluster'].append(int(resultado[0]))
            dicc['cantidad_de_palabras_clave'].append(int(resultado[1]))
            numero = resultado[2].replace(',', '.')
            dicc['porcentaje_de_palabras_clave'].append(float(numero))
            dicc['principales_palabras_clave'].append(resultado[3])

    return pd.DataFrame(dicc)

        

print(ingest_data())
    