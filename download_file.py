import os
import requests

url = "https://scalettarai.osservatorio.it/MI_COPY/202405/10681_20240527/10681_20240527_Rai1/10681_20240527_1600_Rai1.mov"
percorso_cartella = "/Users/vittorio/PycharmProjects/Excel_to_Python/FileVideo/"
nome_file = "10681_20240527_1600_Rai1.mov"
percorso_completo = percorso_cartella + nome_file

response = requests.get(url, verify=False)
response.raise_for_status()

with open(percorso_completo, 'wb') as file:
    file.write(response.content)
