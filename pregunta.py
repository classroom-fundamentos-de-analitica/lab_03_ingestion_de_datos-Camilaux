"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import re
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
resultados = []

def ingest_data():
    cluster = open("clusters_report.txt", mode="r")
    for line in cluster:
        line = line.rstrip()
        palabras.append(line)
    
    for p in range(4,len(palabras)):
        linea = palabras[p]
        n_elementos = 3  
        
        if linea.strip() != "":
            if linea.split()[0].isdigit() == True:
            # Dividir el texto por espacios
                partes = linea.split()

            # Separar las primeras N partes y luego unir el resto
                parte1 = partes[:n_elementos]
                parte2 = " ".join(partes[n_elementos:])
                parte2 = parte2.replace('%', ' ').strip()

            # Combinar la parte separada y la parte unida en una lista
                resultado = parte1 +[parte2]
            else:
                sin_espacio = re.sub(r'\s+', ' ', linea)
                resultado[-1] += sin_espacio.rstrip()
        resultados.append(resultado)

    for r in resultados:
        if int(r[0]) not in dicc['cluster']:
            dicc['cluster'].append(int(r[0]))
            dicc['cantidad_de_palabras_clave'].append(int(r[1]))
            numero = r[2].replace(',', '.')
            dicc['porcentaje_de_palabras_clave'].append(float(numero))
            texto = r[3].replace(".", "")
            dicc['principales_palabras_clave'].append(texto)

    return pd.DataFrame(dicc)

        

print(ingest_data())
    #"maximum power point tracking, fuzzy-logic based control, photo voltaic (pv), photo-voltaic system, differential evolution algorithm, evolutionary algorithm, double-fed induction generator (dfig), ant colony optimisation, photo voltaic array, firefly algorithm, partial shade"