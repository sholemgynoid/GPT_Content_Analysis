#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo per la trascrizione di programmi con il sistema Assembly AI

Versione 2.0

Modulo per la trascrizione di programmi info di giorni passati

Versione 2.5:
Lettura da scalette dell'ora esatta di inizio e di fine del programma.

Versione 2.6:
Inserimento della modalità 3 per inserire solo un programma contraddistinto da un codice trascrizione particolare.

Modalità 1: trascrizione programmi da scalette in un periodo da indicare
Modalità 2: trascrizione programmi da scalette del giorno precedente (da implementare)
Modalità 3: trascrizione programma specifico da scalettare in un periodo da indicare
Modalità 4: trascrizione TG non scalettati del giorno precedente (da implementare)
Modalità 5: trascrizione Link YouTube (da implementare)
Modalità 100: temp, recupero TG4 e Studio Aperto

Versione 2.6.1
22 dicembre 2023

* Cancellazione cartella file video

Versione 2.7.0

* Aggiunta trascrizione TG4 e Studio Aperto
* Aggiunto log su DB di programmi inseriti e stampati

Versione 2.7.1 2024.01.25

* Introdotto il dizionario di Custom spelling
* Introdotto recupero singoli programmi non registrati

Versione 2.7.2 2024.06.03

* Corretto un baco che bloccava il programma se Porta a porta comincia dopo le 24:00

Funzioni da implementare:

* Sistema di tutele per impedire i blocchi dei programmi
* Inserire procedura di controllo per verificare che i record inizio e fine programmi siano di numero uguale

** Caricamento su 4D delle trascrizioni dei TG nell'archivio Registrazione

"""

import time
from builtins import int, input

import os
from shutil import rmtree
import argparse
from argparse import RawTextHelpFormatter

import config
import datetime
from shutil import rmtree

from MongoDB_Utilities import CONNECT_MONGODB
from MongoDB_Utilities import IMPORT_DOCS_IN_MONGO
from MongoDB_Utilities import GET_POSITION_INDEX
from MongoDB_Utilities import AGGIORNAMENTO_LOG_DB
from MongoDB_Utilities import lista_programmi_trascritti_per_giorno

from gs_file_uploading import upload_blob
from gs_file_uploading import delete_blob

from utilities import COPIA_FILE_VIDEO_PROGR, sum_milliseconds_to_time
from utilities import get_date
from utilities import pymongo_format_date
from utilities import EXPO_PROGRAMMI
from utilities import make_unique_dir
from utilities import get_cares_date
from utilities import DIZIONARIO_TG4
from utilities import DIZIONARIO_STAP

from transcribe_AAI import main

from DB4D_Utilities import Estrazione_dizionario_programmi
from DB4D_Utilities import Costruzione_piano_file_orari

os.environ ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ ["HOME"] + "/Dropbox/GOOGLE_TG_TRANSCRIPT/PACCHETTO_TRASCRIZIONE_ASSEMBLYAI/trascrizione-tg-4a25e1fba16b.json"

help_text_mode = '1: trascrizione tutti programmi periodo (inserire "data_da" e "data_a"),'
help_text_mode = help_text_mode + '\n2: trascrizione tutti programmi giorno precedente,'
help_text_mode = help_text_mode + '\n3: trascrizione programma specifico in periodo da definire (NB: serve codice programma Scalette),'
help_text_mode = help_text_mode + '\n4: trascrizione TG non scalettati giorno precedente,'
help_text_mode = help_text_mode + '\n5: trascrizione link YouTube (aggiungere link con parametro opzionale -l),'
help_text_mode = help_text_mode + '\n6: trascrizione file locale (aggiungere percorso file con parametro opzionale -p)'
help_text_mode = help_text_mode + '\n7: trascrizione file locale (aggiungere percorso file con parametro opzionale -p)'
help_text_mode = help_text_mode + '\n100: trascrizione TG Studio Aperto e TG4'

parser = argparse.ArgumentParser(description='Programma per la trascrizione con AssemblyAI di programmi tv, di file, di link YouTube', formatter_class=RawTextHelpFormatter)
parser.add_argument('mode', type=int, choices= [1, 2, 3, 4, 5, 6, 7, 100], default= 1, help=help_text_mode)
parser.add_argument('-lc', '--languageCode', type= str, help= 'Codice del linguaggio del file da trascrivere, per default è "it"', default= 'it')
parser.add_argument('-v', '--verbose', help= 'Restituisce output verboso', action= 'store_true')
arg_group = parser.add_mutually_exclusive_group()
arg_group.add_argument('-l', '--link', type=str, default= '', help='Link del filmato YouTube da trascrivere')
arg_group.add_argument('-p', '--pathFile', type=str, default= '', help='Percorso del file locale da trascrivere')

args = parser.parse_args()

mode = args.mode
lang_code = args.languageCode

#Inserisco la API Key dell'Osservatorio di Pavia
api_key: str = "0704da77e4464085933b09e8b364a865"

#Inserisco la DataCares = 0 per le operazioni di trasformazione tra DataCares e data in formato gg-mm-aaaa
date_1 = datetime.datetime(1995, 2, 28)

#Immagazzino in una variabile il tempo di partenza del programma
start_time = time.time()

if mode == 1:
    giorno_cares_da = int(input("Data cares iniziale da trascrivere: "))
    giorno_cares_a = int(input("Data cares finale da trascrivere: "))
    local = True
elif mode == 2 or mode == 4:
    giorno_cares_da = get_cares_date(datetime.date.today()) - 1
    giorno_cares_a = get_cares_date(datetime.date.today()) - 1
    local = True
elif mode == 3:
    giorno_cares_da = int(input("Data cares iniziale da trascrivere: "))
    giorno_cares_a = int(input("Data cares finale da trascrivere: "))
    cod_programmi = input("Codici programmi da trascrivere (separati da spazio): ")
    local = True
elif mode == 5:
    local = False
    # Modulo per la trascrizione di filmati youtube, da implementare
    pass
elif mode == 6:
    local = True
    # Modulo per la trascrizione di file locali, da implementare
    pass
elif mode == 7:
    giorno_cares_da: int = int(input("Data cares da completare: "))
    giorno_cares_a = giorno_cares_da
elif mode == 100:
    giorno_cares_da = int(input("Data cares iniziale da trascrivere: "))
    giorno_cares_a = int(input("Data cares finale da trascrivere: "))
    local = True
    # Modulo temporaneo per il recupero dei TG di Rete4 e Italia1

if giorno_cares_a >= giorno_cares_da:

    for giorno in range(giorno_cares_da, giorno_cares_a + 1):

        if mode < 3:
            dizionarioProgrammi = Estrazione_dizionario_programmi(giorno, int(mode))
            dizionarioProgrammi.append(DIZIONARIO_TG4(giorno))
            dizionarioProgrammi.append(DIZIONARIO_STAP(giorno))

        elif mode == 3:
            lista_programmi = list(map(int, cod_programmi.split()))
            dizionarioProgrammi = []
            for programma in lista_programmi:
                dizionarioProgrammi = dizionarioProgrammi + Estrazione_dizionario_programmi(giorno, int(mode), str(programma))

        elif mode == 7:
            dizionarioProgrammi = Estrazione_dizionario_programmi(giorno, int(mode))
            dizionarioProgrammi.append(DIZIONARIO_TG4(giorno))
            dizionarioProgrammi.append(DIZIONARIO_STAP(giorno))
            programmi_trascritti = lista_programmi_trascritti_per_giorno(giorno)
            for programma in programmi_trascritti:
                progr_index = next(index for (index, d) in enumerate(dizionarioProgrammi) if d["Testata"] == programma)
                dizionarioProgrammi.pop(progr_index)

        elif mode == 100:
            dizionarioProgrammi = []
            #dizionarioProgrammi.append(DIZIONARIO_TG4(giorno))
            dizionarioProgrammi.append(DIZIONARIO_STAP(giorno))

        if len(dizionarioProgrammi) > 0:

            for programma in dizionarioProgrammi:

                if mode == 4:
                    genere_programma: str = 'TG italiani'
                else:
                    genere_programma = config.tipologia_programma[programma["ID_GENERE"]]

                etichetta_testata = programma['DESCRIZIONE'].replace(':', '')

                fileOrari = Costruzione_piano_file_orari(programma)

                directory_in_str = make_unique_dir()

                for fileVideo in fileOrari:

                    rete = config.dizionario_reti[fileVideo['Rete']]
                    ora = fileVideo['File']
                    minuto = fileVideo['Start']

                    dict_file_info = COPIA_FILE_VIDEO_PROGR(giorno + fileVideo['DayGap'],
                                                            rete,
                                                            ora,
                                                            fileVideo['Start'],
                                                            fileVideo['End'],
                                                            directory_in_str)

                    filename= f"{dict_file_info['nome_file']}.flac"

                    i = 0
                    TG_record = {}
                    testata = ''
                    testo_TG = ''
                    confidenza = 0.0
                    db = 'MEDIA'
                    collection = 'tg_transcript_AssAI'

                    start_time = time.time()

                    mydb = CONNECT_MONGODB(db, collection)

                    if config.connessione_mongodb:

                        percorso = os.path.join(os.fsdecode(directory_in_str), filename)

                        if args.verbose:
                            print(f'Uploading file {filename}')

                        # url_file_to_transcribe = upload_blob('fileaudio_oss',
                        #                                      percorso,
                        #                                      filename)

                        paragraphs: object = main(percorso,
                                                  api_key,
                                                  lang_code,
                                                  True,
                                                  programma["ID_GENERE"])

                        i = GET_POSITION_INDEX(mydb, etichetta_testata, giorno)

                        date_shift = fileVideo['DayGap']

                        for k in paragraphs:

                            i = i + 1
                            testo_TG = k['text']
                            confidenza = k['confidence']
                            start = sum_milliseconds_to_time(int(ora), int(minuto), k['start'])

                            TG_record = {
                                'Posizione': i,
                                'Data_Cares': giorno,
                                'Data': get_date(pymongo_format_date(1995, 2, 28, start), add_days=(giorno)),
                                'Orario_File': ora,
                                'Rete': rete,
                                'Genere': genere_programma,
                                'Testata': etichetta_testata,
                                'Transcript': testo_TG,
                                'Confidence': confidenza,
                                'T_scrittura': datetime.datetime.now()
                            }

                            if config.reti_dic[rete]['Language'] != "greek":
                                TG_record['language'] = config.reti_dic[rete]['Language']

                            IMPORT_DOCS_IN_MONGO(TG_record, mydb)

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print(
                            f"Successfully inserted document: {filename}. Text available at MongoDB:MEDIA:tg_transcript")
                        i = 0

                    else:

                        print('Connessione con MongoDB fallita')

                    #delete_blob('fileaudio_oss', filename)

                EXPO_PROGRAMMI(int(giorno), mydb, etichetta_testata)

                print(f"Cancello la directory {directory_in_str}.")

                AGGIORNAMENTO_LOG_DB (db, giorno, get_date(pymongo_format_date(1995, 2, 28, start), add_days=(giorno)), etichetta_testata, rete)

                rmtree (directory_in_str)

else:
    print ("Giorno di partenza maggiore del giorno di arrivo")

print("--- Process completed in {} seconds ---".format(time.time() - start_time))
