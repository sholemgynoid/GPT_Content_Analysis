import openai
import pandas as pd
import numpy as np
import json
import os
import argparse
from argparse import RawTextHelpFormatter

from openai_utils import classificazione_adc

help_text_mode = '1: Analisi del contenuto e analisi del sentiment di un file CrowdTangle Facebook o Instagram,'
help_text_mode = help_text_mode + '\n2: Analisi del contenuto e analisi del sentiment di un frame di trascrizione di un Talk show,'
help_text_mode = help_text_mode + '\n3: Analisi tematica di una notizia del TG o di una scaletta da matrice di esportazione.'
help_text_mode = help_text_mode + '\n4: NN,'
help_text_mode = help_text_mode + '\n5: NN,'
help_text_mode = help_text_mode + '\n6: NN.'

parser = argparse.ArgumentParser(description='Programma per la trascrizione con AssemblyAI di programmi tv, di file, di link YouTube', formatter_class=RawTextHelpFormatter)
parser.add_argument('mode', type=int, choices= [1, 2, 3, 4, 5, 6], default= 1, help=help_text_mode)
parser.add_argument('-v', '--verbose', help= 'Restituisce output verboso', action= 'store_true')
arg_group = parser.add_mutually_exclusive_group()
arg_group.add_argument('-l', '--link', type=str, default= '', help='Link del filmato YouTube da trascrivere')
arg_group.add_argument('-p', '--pathFile', type=str, default= '', help='Percorso del file locale da trascrivere')

args = parser.parse_args()

mode = args.mode

if mode == 1:
    file_to_open = input ('File CrowdTangle da analizzare: ')
    file_sn = pd.read_csv(file_to_open, sep = ";")
elif mode == 3:
    file_to_open = input ('File expo scalette da analizzare: ')
    file_sn = pd.read_csv(file_to_open, sep = "\t")

if mode == 3:
    file_sn = file_sn[file_sn["Genere_programma"].str.contains("APPROFONDIMENTO INFORMATIVO|INFOTAINMENT-CONTENITORE")]
    file_sn.to_csv('DB Indicizzazione filtrato.csv')

row_count = len(file_sn)

print (file_sn.shape)

#file_sn = file_sn.sample (n= 20)
#file_sn = file_sn.iloc [[19]]

lista_out = file_sn.apply(lambda record: classificazione_adc(record, 1, mode), axis=1)
df_out = pd.DataFrame({'id': lista_out.index, 'temi': lista_out.values})
df_out.to_csv('out_temi.csv')

df_out[['Tema1', 'Tema2']] = df_out['temi'].str.split(',', expand = True)
df_out.drop('id', axis='columns', inplace=True)
df_out.reset_index(drop=True, inplace=True)
file_sn.reset_index(drop=True, inplace=True)
print (df_out.shape)

file_sn = pd.concat ([file_sn, df_out], axis=1)
file_sn.to_csv('Output Temi.csv')

if mode == 1:
    file_sn['SentimentUe'] = file_sn.apply(lambda record: classificazione_adc(record, 2, mode),axis=1)
    file_sn['SentimentGov'] = file_sn.apply(lambda record: classificazione_adc(record, 3, mode),axis=1)
    file_sn['MoodEmotivo'] = file_sn.apply(lambda record: classificazione_adc(record, 4, mode),axis=1)

file_sn.to_csv('output.csv')
