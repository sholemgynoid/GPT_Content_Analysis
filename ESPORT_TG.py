#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
from pymongo.errors import ConnectionFailure
from MongoDB_Utilities import CONNECT_MONGODB
from utilities import pymongo_format_date
from utilities import get_date

def EXPORT_TG_TEXTS (giorno_da: int ,
                     giorno_a: int ,
                     rete: str ,
                     output_file: str
                     ):

    if rete == "11":
        lista_reti = []
        lista_reti.append (input ('Inserisci il nome della testata: '))
    else:
        lista_reti = definizione_rete_nella_query (rete)

    try:
        mydb = CONNECT_MONGODB('MEDIA', 'tg_transcript_AssAI')
    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

    days = list (range (giorno_da, giorno_a + 1))

    f_out = open (output_file + '.txt' , 'w')

    for day in days:

        for testata in lista_reti:

            search_dict = {"$and": [
                {"Data_Cares": day} ,
                {"Testata": testata}
            ]}

            n_docs = mydb.count_documents(search_dict)

            if n_docs > 0:

                tg_from_tag = mydb.find(search_dict).sort([
                        ('Posizione' , pymongo.ASCENDING)
                ])

                #output = '**** *G_{}  *T_{}'.format(str(day), testata)
                output = testata + '\n'
                output = output + str(day) + '\n'
                output = output + str(get_date(pymongo_format_date(1995, 2, 28), add_days=(day)))[0:10]

#                 if rete == '11':
#
#                     output = output + ' *H_{}'.format(ora_file)

                output = output + '\n'*2

                for response in tg_from_tag:
                    output = output + '{}'.format(response['Data'])[11:-3] + u'\n'
                    output = output + (response['Transcript'] + '\n')

                output = output + '\n'

                f_out.write (output)

            else:
                print (f'{day}, {testata}: Nessun record risponde ai criteri di ricerca.')

    f_out.close()

    print('Esportazione terminata')

def EXPORT_RECORDS_BY_KEYWORD (giorno_da: int ,
                     giorno_a: int ,
                     rete: str ,
                     db : str ,
                     collection: str ,
                     output_file: str,
                     keywords: str
                     ):

    try:
        mydb = CONNECT_MONGODB (db, collection)
    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

    days = list(range(giorno_da , giorno_a + 1))

    lista_reti = definizione_rete_nella_query (rete)

    search_dict = {"$and":
        [
        {"Data_Cares": {"$in": days}} ,
        {"testata": {"$in": lista_reti}} ,
        {"$text": {"$search": keywords}}
        ]
    }

    n_docs = mydb.count_documents(search_dict)

    if n_docs > 0:

        tg_from_tag = mydb.find (search_dict, {'score': { '$meta': "textScore" }}).sort([('score', {'$meta': 'textScore'})])

        f_out = open(output_file + '.txt' , 'w')

        output = 'Parole chiave ricerca: {}'.format(keywords) + ('\n' * 2)

        for response in tg_from_tag:
            output = output + '{}{}{}'.format('Punteggio :', response['Confidence'] , '\n')
            output = output + '{}{}{}'.format('Rete: ', response['Rete'], '\n')
            output = output + '{}{}{}'.format('Data: ', response['Data'], '\n')
            output = output + '{}{}{}'.format('Data Cares: ', response['Data_Cares'], '\n')
            output = output + '{}{}{}'.format('Posizione: ', response['Posizione'], '\n')
            output = output + '{}{}{}'.format('Testo: ', response['Transcript'], '\n'* 2)

            f_out.write (output)

            output = ""

        f_out.close()

        print('Esportazione terminata')

def definizione_rete_nella_query (indice):

    if indice == '1':
        rete = ['TG1 2000']
    elif indice == '2':
        rete = ['TG2 2030']
    elif indice == '3':
        rete = ['TG3 1900']
    elif indice == '4':
        rete = ['TG4 1850']
    elif indice == '5':
        rete = ['TG5 2000']
    elif indice == '6':
        rete = ['STUDIO APERTO 1830']
    elif indice == '7':
        rete = ['TGLa7 2000']
    elif indice == '8':
        rete = ['TG1 2000' , 'TG2 2030' , 'TG3 1900']
    elif indice == '9':
        rete = ['TG4 1850' , 'TG5 2000' , 'STUDIO APERTO 1830']
    elif indice == '10' :
        rete = ['TG1 2000' ,
                'TG2 2030' ,
                'TG3 1900',
                'TG4 1855',
                'TG5 2000',
                'STUDIO APERTO 1830',
                'TG LA7 2000']
    else:
        rete = ['Nessuna rete selezionata']
        print ('indice non valido')

    return rete

modalita_esportazione = input('Modalità esportazione (1: Esporta programmi; 2: Ricerca per parole chiave): ')

output_file = input('File di esportazione: ')

if modalita_esportazione == "2":

    keywords = input ('Inserisci parole chiave separate da uno spazio (precedute da "-" per escludere parole dalla ricerca): ')

db = 'MEDIA'
collection = 'tg_transcript_AssAI'
giorno_da = input ('Giorno di partenza: ')
giorno_a = input ('Giorno di arrivo: ')
testata = input ('Rete (1: Tg1;'
                 '2: Tg2;'
                 '3: Tg3;'
                 '4: Tg4;'
                 '5: Tg5;'
                 '6: Studio aperto;'
                 '7: La7;'
                 '8: Tg Rai;'
                 '9: Tg Mediaset,'
                 '10: Tutte,'
                 '11: Altra testata): ')

if modalita_esportazione == "1":
    EXPORT_TG_TEXTS (int (giorno_da) , int (giorno_a) , testata , output_file)
elif modalita_esportazione == "2":
    EXPORT_RECORDS_BY_KEYWORD (int (giorno_da) , int (giorno_a) , testata , db , collection , output_file, keywords)