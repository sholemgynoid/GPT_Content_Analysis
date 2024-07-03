# GPT_Content_Analysis

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
