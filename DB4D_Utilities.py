#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Versione 1.0

Modulo per la interrogazione DB 4D attraverso python100

Modifica:
Lettura da scalette dell'ora esatta di inizio e di fine del programma.
"""
from typing import Dict, Any, List

from python4DBI.python4DBI import *
import logging
import time


def Estrazione_dizionario_programmi(dataCares: object, mode, codice_programma=None) -> object:
    try:
        con = python4DBI(logging_level=logging.DEBUG,
                         logging_file='/Users/pythonserver/Dropbox/GOOGLE_TG_TRANSCRIPT/PACCHETTO_TRASCRIZIONE_ASSEMBLYAI/python4DBI.log')

        # Authentication
        con.connect(
            host='192.168.0.238',
            user='Vittorio',
            password='v')
        if con.connected():
            # Get cursor
            cursor = con.cursor()

            campo = ['Ora_Inizio_Scaletta', 'Ora_Fine_Scaletta']
            dictOraInizio: dict[Any, Any] = {}
            dictOraFine: Dict[Any, Any] = {}
            dictFinale: list[dict[Any, Any] | list[dict[Any, Any]]] = [dictOraInizio, dictOraFine]
            if mode < 3 or mode == 7 :
                query_cod_trascr = "> 0"
            elif mode == 3:
                query_cod_trascr = "= " + codice_programma

            query = """
                    SELECT SCAL_Master.%s,
                           SCAL_Master.Data_Scaletta,
                           SCAL_Archivio_Programmi.Descrizione,
                           SCAL_Archivio_Programmi.Codice_Trascrizione,
                           SCAL_Archivio_Programmi.ID_Rete,
                           SCAL_Archivio_Programmi.ID_Genere
                    FROM   SCAL_Master sm
                    JOIN   SCAL_Archivio_Programmi sap
                        ON sm.ID_Programma = sap.ID
                    WHERE  Data_Scaletta = %s AND Tipologia_Scaletta = %s AND sap.Codice_Trascrizione %s
                    """

            for i in range(2):

                result = cursor.prepare_statement(query=query % (campo[i], dataCares, str(i + 1), query_cod_trascr,))

                if result is FOURD_OK:

                    # Execute the query
                    cursor.execute(query=query % (campo[i], dataCares, str(i + 1), query_cod_trascr,))

                    # Check the results
                    if cursor.row_count > 0:
                        # Fetch all the results
                        result_rows = cursor.fetch_all()

                        # Print result page to console
                        cursor.print_result(headers=cursor.description, rows=result_rows)

                        names = [name[0] for name in cursor.description]
                        dictFinale[i] = [dict(zip(names, row)) for row in result_rows]
                        print(dictFinale[i])
                else:
                    # Handle wrong statement
                    pass
            # Close cursor
            cursor.close()

            comboDict = []

            for i in range(len(dictFinale[0])):
                comboDict.append({**dictFinale[0][i], **dictFinale[1][i]})

        # Close the socket connection
        con.close()

        return (comboDict)

    except Warning as e:
        # Handle error
        pass
    except Error as e:
        # Handle error
        print(e)
        pass
    except Exception as e:
        # Handle error
        print(e)
        pass


def Costruzione_piano_file_orari(programma):
    # Se l'ora di inizio è minore dell'ora di fine, modifico le ore (+24) nel loop e il giorno (+1) nel dizionario
    #
    # Aggiungo un modulo per la trascrizione del TG1 e del TG5 che tenga conto del fatto che i file delle 20
    # cominciano alle 19:55

    programmaTrascrizione = []

    oraInizio = programma['ORA_INIZIO_SCALETTA'].hour

    if programma['ORA_INIZIO_SCALETTA'].hour > programma['ORA_FINE_SCALETTA'].hour:
        oraFine = programma['ORA_FINE_SCALETTA'].hour + 24
    else:
        oraFine = programma['ORA_FINE_SCALETTA'].hour

    if programma['ORA_INIZIO_SCALETTA'].hour < 2:
        oraInizio = programma['ORA_INIZIO_SCALETTA'].hour + 24
        oraFine = programma['ORA_FINE_SCALETTA'].hour + 24

    for n in range(oraInizio, oraFine + 1):
        if n > 23 or n < 2:
            oraFile = n - 24
            giornoFile = programma['DATA_SCALETTA'] + 1
            dayGap = 1
        else:
            oraFile = n
            giornoFile = programma['DATA_SCALETTA']
            dayGap = 0

        if oraFile == programma['ORA_INIZIO_SCALETTA'].hour:
            if oraInizio == oraFine:
                endFile = (programma['ORA_FINE_SCALETTA'].minute+1)-programma['ORA_INIZIO_SCALETTA'].minute
            else:
                endFile = 60-programma['ORA_INIZIO_SCALETTA'].minute
            programmaTrascrizione.append({'File': str(oraFile),
                                          'Data': str(giornoFile),
                                          'Rete': str(programma['ID_RETE']),
                                          'Start': "{0:02}".format(programma['ORA_INIZIO_SCALETTA'].minute),
                                          'End': endFile,
                                          'DayGap': dayGap})

        elif (oraFile == programma['ORA_FINE_SCALETTA'].hour):
            programmaTrascrizione.append({'File': str(oraFile),
                                          'Data': str(giornoFile),
                                          'Rete': str(programma['ID_RETE']),
                                          'Start': '00',
                                          'End': programma['ORA_FINE_SCALETTA'].minute + 1,
                                          'DayGap': dayGap})
        else:
            programmaTrascrizione.append({'File': str(oraFile),
                                          'Data': str(giornoFile),
                                          'Rete': str(programma['ID_RETE']),
                                          'Start': '00',
                                          'End': 60,
                                          'DayGap': dayGap})

    return (programmaTrascrizione)
