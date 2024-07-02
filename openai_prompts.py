#!/usr/bin/python
# -*- coding': utf-8 -*-

analisi_tematica_prova = """Sei un analista junior in gruppo di ricerca sull'analisi dei media e dell'agenda setting. Stai analizzando l'agenda dei programmi di informazione per determinare i temi più trattati nel dibattito pubblico. Devi attenerti strettamente alle indicazioni che riceverai.

Riceverai la sintesi di notizie, dibattiti o video, che chiamerò di seguito "unità di analisi" e che ti fornirò in fondo al prompt. Riclassifica l'unità di analisi sulla base dei seguenti passi:

0. Le categorie tematiche che utilizzerai per indicizzare le unità di analisi devono essere sintetiche, in modo da permettere poi aggregazioni significative del materiale analizzato.
1. Attribuisci ad ogni unità di analisi un tema primario. Non usare mai "Politica" come categoria tematica. Se non sei sicuro del significato della frase, non indicare il tema primario, ma usa "NR".
2. Se e solo se ritieni che la classificazione non sia esauriente, individua un tema secondario. Non assegnare all'Unità di analisi un tema secondario basandoti su un'unica parola dell'Unità di analisi, ma guarda al significato generale dell'Unità di analisi. Se non sei sicuro del significato della frase, non indicare il tema secondario.
3. Se non sei riuscito a individuare nessun tema per l'unità di analisi, indica nell'output "NR".
4. In nessun caso dovrai indicare più di due temi per l'unità di analisi. Se ne individui più di due, indica solo i due temi principali.

Per chiarire la metodologia, usa gli esempi contenuti di seguito:

#### INIZIO ESEMPI

--------------Esempio di input--------------
Unità di analisi: L'uso di tecnologie di desalinizzazione per limitare l'impatto della crisi climatica sulle risorse idriche
--------------Esempio di output--------------
Clima, Innovazione

--------------Esempio di input--------------
Unità di analisi: Dichiarazioni di Chiara Ferragni sul suo rapporto con la Bauli
--------------Esempio di output--------------
Influencer

--------------Esempio di input--------------
Unità di analisi: Test delle nuove procedure per gestire le richieste di permesso di soggiorno alla Questura
--------------Esempio di output--------------
Pubblica amministrazione

--------------Esempio di input--------------
Unità di analisi: I migliori metodi per lucidare l'argenteria
--------------Esempio di output--------------
Altro

--------------Esempio di input--------------
Unità di analisi: Sagittario, nuove opportunità sentimentali per i nati nella prima decade
--------------Esempio di output--------------
Altro

#### FINE ESEMPI

Programma: >>>>>>NOME_EMITTENTE<<<<<<
Unità di analisi: >>>>>>TESTO_MESSAGGIO<<<<<<

La classificazione tematica è:
"""

analisi_tematica = """Sei un analista junior in gruppo di ricerca sull'analisi dei media e dell'agenda setting. Stai analizzando l'agenda dei programmi di informazione per determinare i temi più trattati nel dibattito pubblico e non hai alcuna autonomia decisionale sulla metodologia. Devi quindi attenerti strettamente alle indicazioni che riceverai. 

Riceverai la sintesi di notizie, dibattiti o video, che chiamerò di seguito "unità di analisi" e che ti fornirò in fondo al prompt. Riclassifica l'unità di analisi sulla base dei seguenti passi:

1. Attribuisci ad ogni unità di analisi un tema primario. Usa come categorie gli elementi contenuti nella seguente lista, separati da una virgola, che denominiamo "Lista delle micro": >>>>>>LISTA_CATEGORIE<<<<<<.
2. Se e solo se ritieni che la classificazione non sia esauriente, individua un tema secondario: per individuare il tema secondario, usa come categorie solo gli elementi contenuti nella "Lista delle micro". Non assegnare all'Unità di analisi un tema secondario basandoti su un'unica parola dell'Unità di analisi, ma guarda al significato generale dell'Unità di analisi. Se non trovi una corrispondenza diretta e chiara tra Unità di analisi e una delle categorie contenute nella "Lista delle micro", non indicare il tema secondario. Se non sei sicuro del significato della frase, non indicare il tema secondario. Non usare mai "Altro" come tema secondario.
3. Compi la seguente operazione di controllo: verifica che il tema o i temi che hai scelto nel passo "1" e "2" siano contenuti nella "Lista delle micro". Sia il tema primario sia l'eventuale tema secondario che hai scelto nel passo "1" e "2" devono essere contenuti nella "Lista delle micro".
4. Se il tema primario e l'eventuale tema secondario che hai scelto sono entrambi contenuti nella "Lista delle micro", usali come output. Altrimenti, esegui i passi successivi.
5. Fai una prima verifica di controllo: se il tema primario che hai scelto nel passo "1" non è contenuto nella "Lista delle micro", ricordati che non hai alcuna autonomia decisionale, e verifica se il tema primario che hai scelto non possa essere ricondotto con una corrispondenza diretta e chiara a una delle categorie contenute nella "Lista delle micro". Se riesci a ricondurlo a una delle categorie contenute nella "Lista delle micro", usa quest'ultima categoria.
6. Se il tema che hai scelto nel passo "1" non può essere ricondotto a una delle categorie contenute nella "Lista delle micro", indica "Altro" nell'output.
7. Fai una seconda verifica di controllo: se il tema secondario che hai scelto nel passo "2" non è contenuto nella "Lista delle micro", ricordati che non hai alcuna autonomia decisionale, e verifica se il tema secondario che hai scelto non possa essere ricondotto con una corrispondenza diretta e chiara a una delle categorie contenute nella "Lista delle micro". Se riesci a ricondurlo a una delle categorie contenute nella "Lista delle micro", usa quest'ultima categoria. Se il tema che hai scelto nel passo "2" non può essere ricondotto a una delle categorie contenute nella "Lista delle micro", non indicare il tema secondario.
8. Se non sei riuscito a individuare nessun tema per l'unità di analisi, indica nell'output "NR".
9. In nessun caso dovrai indicare più di due temi per l'unità di analisi. Se ne individui più di due, indica solo i due temi principali.
10. Per l'individuazione del tema, tieni conto anche del Programma in cui va in onda la notizia, del Soggetto parlante e della Carica del soggetto parlante, che ti indicherò alla fine del prompt.
11. L'output che fornirari deve comprendere SOLO l'indicazione dei due temi individuati separati da una virgola, secondo questo esempio:
Elezioni, Europa

Per chiarire la metodologia, usa le indicazioni relative alla classificazione tematica delle Unità di analisi contenute di seguito:

ELENCO_INDICAZIONI

Programma: >>NOME_PROGRAMMA<<
Soggetto parlante: >>NOME_SOGGETTO<<
Ruolo soggetto parlante: >>RUOLO_SOGGETTO<<

Unità di analisi: >>TESTO_MESSAGGIO<<

La classificazione tematica è:
"""

analisi_spettro_emotivo = """You are trained to analyze and detect the emotional mood of given texts. If you're unsure about an answer of a certain emotional mood, you have to say 'NR'.
Analyze the following political statement and establish the main emotional mood.
Return the answer in one single word. If the text contains words whose meaning you don't know, try to return the emotional mood of the text omitting the words you don't know.
The categories of the emotional mood variable can be found in the follwing list, separated by a comma: LISTA_CATEGORIE

Politician: NOME_EMITTENTE
Statement: TESTO_MESSAGGIO

The main emotional mood is:
"""

analisi_sentiment_ue = """Sei un analista addestrato nell'analisi del contenuto e nell'analisi del sentiment.
Devi determinare l'atteggiamento nei confronti dell'Unione europea e delle istituzioni europee contenuto nei post su Facebook di diversi soggetti politici.
Le possibili risposte sono contenute nella seguente lista, separate da una virgola: LISTA_CATEGORIE.

Politico: NOME_EMITTENTE
Carica politica dell'autore del messaggio: TIPOLOGIA_EMITTENTE
Messaggio: TESTO_MESSAGGIO

Per la valutazione dell'atteggiamento nei confronti del Governo, tieni anche conto del politico autore del messaggio e della sua carica politica.

L'atteggiamento nei confronti dell'Unione europea o delle Istituzioni europee è: 
"""

# (giustifica molto brevemente la tua scelta)

analisi_sentiment_governo = """Sei un analista addestrato nell'analisi del contenuto e nell'analisi del sentiment.
Devi determinare l'atteggiamento nei confronti del Governo italiano attualmente in carica, della Presidente del Consiglio e dei ministri attualmente in carica contenuto nei post su Facebook di diversi soggetti politici.
Le possibili risposte sono contenute nella seguente lista, separate da una virgola: LISTA_CATEGORIE.
Nel caso in cui non venga nominato esplicitamente il Governo o il ruolo dei Ministri, tieni conto dell'eventuale ruolo di Governo ricoperto dalle persone indicate dai cognomi contenuti nel messaggio.
Per la valutazione dell'atteggiamento nei confronti del Governo, tieni anche conto del politico autore del messaggio e della sua carica politica.

Politico autore del messaggio: NOME_POLITICO
Carica politica dell'autore del messaggio: TIPOLOGIA_EMITTENTE
Messaggio: TESTO_MESSAGGIO

L'atteggiamento nei confronti del Governo e dei Ministri è: 
"""

# (giustifica molto brevemente la tua scelta)

categorie_tematiche_PROVA = [
    {"Lemma": "Africa", "Macro": "Esteri e politica estera", "Connessioni": ['Sahel']},
    {"Lemma": "Aggressioni razziste", "Macro": "Questioni sociali", "Connessioni": ['Aggressioni e pestaggi per motivi etnici o religiosi']},
    {"Lemma": "Agricoltura", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Alimentazione", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": ['diete', 'consigli alimentari sulla salute', 'veganesimo', 'vegetarianesimo']},
    {"Lemma": "Altro cronaca nera", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "America", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Animali", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Arte", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Asia", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Assistenza sociale", "Macro": "Questioni sociali", "Connessioni": []},
    {"Lemma": "Attività di intelligence", "Macro": "Difesa e sicurezza", "Connessioni": []},
    {"Lemma": "Bioetica", "Macro": "Salute e sanità", "Connessioni": []},
    {"Lemma": "Cambiamenti climatici", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Campagna elettorale", "Macro": "Politica interna", "Connessioni": []},
    {"Lemma": "Catastrofi naturali", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Celebrità", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": ['Vicende relative a Vip e celebrità', 'Gossip']},
 #   {"Lemma": "Censura e libertà di espressione", "Macro": "Questioni sociali", "Connessioni": []},
    {"Lemma": "Chiesa", "Macro": "Religione", "Connessioni": []},
    {"Lemma": "Cina", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Cinema", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Commercio internazionale", "Macro": "Economia e finanza", "Connessioni": ["libero scambio, dispute commerciali tra Stati, politiche di protezionismo, impatto del commercio globale", 'Usa questa voce solo quando è esplicito il contesto internazionale nella notizia']},
    {"Lemma": "Concorrenza", "Macro": "Economia e finanza", "Connessioni": ['Antitrust', 'Bolkenstein', 'Licenze taxi', 'Concessioni balneari']},
    {"Lemma": "Consumi", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Convivenza civile", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": ['Educazione e rispetto reciproco']},
    {"Lemma": "Cosmesi e cura personale", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": []},
    {"Lemma": "Criminalità colletti bianchi", "Macro": "Criminalità e cronaca nera", "Connessioni": ['Frode', 'Corruzione']},
    {"Lemma": "Criminalità giovanile", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "Criminalità informatica", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "Criminalità organizzata", "Macro": "Criminalità e cronaca nera", "Connessioni": ['mafia', 'camorra', 'ndrangheta']},
    {"Lemma": "Crisi economica", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Crisi umanitaria", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Cronaca estera", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Cronaca", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": []},
    {"Lemma": "Cucina", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": ['ricette', 'prodotti tipici']},
    {"Lemma": "Cybersecurity", "Macro": "Difesa e sicurezza", "Connessioni": []},
    {"Lemma": "Diritti civili", "Macro": "Questioni sociali", "Connessioni": ["Privacy e trattamento dati", 'Discriminazioni etniche e religiose']},
    {"Lemma": "Diritti umani", "Macro": "Questioni sociali", "Connessioni": ['Pena di morte', 'Tortura', "Tribunale dell'Aia"]},
    {"Lemma": "Disabilità", "Macro": "Questioni sociali", "Connessioni": []},
    {"Lemma": "Occupazione e disoccupazione", "Macro": "Economia e finanza", "Connessioni": ['Formazione professionale']},
    {"Lemma": "Droga", "Macro": "Criminalità e cronaca nera", "Connessioni": ['Spaccio', 'Narcotraffico']},
    {"Lemma": "Ecologia", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Elezioni", "Macro": "Politica interna", "Connessioni": ['Elezioni politiche', 'Elezioni europee ', 'Astensionismo']},
    {"Lemma": "Energia e politiche energetiche", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Energie rinnovabili", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Epidemie", "Macro": "Salute e sanità", "Connessioni": []},
    {"Lemma": "Europa", "Macro": "Esteri e politica estera", "Connessioni": ["Unione europea", 'Bolkenstein', 'Nelle notizie a tema Ue privilegia sempre la voce "Europa"']},
    {"Lemma": "Evasione fiscale", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "Fai da te", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": []},
    {"Lemma": "Famiglia", "Macro": "Questioni sociali", "Connessioni": []},
    {"Lemma": "Festività", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": []},
    {"Lemma": "Fitness", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": []},
    {"Lemma": "Forze dell'ordine", "Macro": "Difesa e sicurezza", "Connessioni": []},
    {"Lemma": "Fumetti", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Giochi e concorsi", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": ["Usa se nella unità di classificazione c'è la parola 'gioco'"]},
    {"Lemma": "Giustizia", "Macro": "Criminalità e cronaca nera",
     "Connessioni": ['Riforma della giustizia', 'ANM', 'CSM', 'Separazione delle carriere']},
    #    {"Lemma": "Gossip", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": ['Vicende relative a Vip e celebrità']},
    {"Lemma": "Governo", "Macro": "Politica interna", "Connessioni": ['Solo notizie sul Governo italiano']},
    {"Lemma": "Guerra", "Macro": "Difesa e sicurezza", "Connessioni": []},
    {"Lemma": "Immigrazione", "Macro": "Questioni sociali", "Connessioni": []},
    {"Lemma": "Imprenditoria", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Incidenti", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "Incidenti sul lavoro", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "Indagini e arresti", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "Industria", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Influencer", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": []},
    {"Lemma": "Infrastrutture", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Innovazione tecnologica", "Macro": "Scienza e tecnologia", "Connessioni": []},
    {"Lemma": "Inquinamento", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Intelligenza artificiale", "Macro": "Scienza e tecnologia", "Connessioni": []},
    {"Lemma": "Lavoro precario", "Macro": "Economia e finanza", "Connessioni": ['Salario minimo']},
    {"Lemma": "Leader politici", "Macro": "Politica interna", "Connessioni": []},
    {"Lemma": "Leader religiosi", "Macro": "Religione", "Connessioni": []},
    {"Lemma": "Leggi e decreti", "Macro": "Politica interna", "Connessioni": []},
    {"Lemma": "Letteratura", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "LGBTQ+", "Macro": "Questioni sociali", "Connessioni": ['Transfobia', 'Coppie omogenitoriali', 'Diritti comunità LGBTQ+', 'Aggressioni omotransfobiche']},
    {"Lemma": "Linguaggio d'odio", "Macro": "Questioni sociali", "Connessioni": ['Bullismo', 'Body shaming']},
    {"Lemma": "Made in Italy", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Medioriente", "Macro": "Esteri e politica estera", "Connessioni": ['Hamas', 'Netanyahu', 'Israele', 'Palestina']},
    {"Lemma": "Mercato finanziario", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Meteo", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": []},
    {"Lemma": "Moda", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": []},
    {"Lemma": "Multinazionali", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Musica", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "NATO", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Nucleare", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Omicidio", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "ONU", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Operazioni militari", "Macro": "Difesa e sicurezza", "Connessioni": []},
    {"Lemma": "Opposizioni", "Macro": "Politica interna", "Connessioni": []},
    {"Lemma": "Partiti", "Macro": "Politica interna", "Connessioni": ['Cronaca parlamentare', 'Relazioni tra leader', 'Dibattito politico', 'Candidature', 'Alleanze politiche', 'Simboli politici']},
    {"Lemma": "Patrimonio culturale", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Pensioni", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Piccole e medie imprese", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Politica estera", "Macro": "Esteri e politica estera", "Connessioni": ['Diplomazia', 'Onu', 'G7', 'Corte Giustizia Aia']},
    {"Lemma": "Politiche della casa", "Macro": "Economia e finanza", "Connessioni": ['Superbonus', 'Piano casa', 'Condoni edilizi']},
    {"Lemma": "Politiche economiche", "Macro": "Economia e finanza", "Connessioni": ['Legge di Bilancio', 'Conti pubblici', 'Tagli di spesa', 'Gestione risorse pubbliche', 'Concessioni balneari']},
    {"Lemma": "Politica locale", "Macro": "Politica interna", "Connessioni": ['Elezioni locali', 'Amministrazione enti locali']},
    {"Lemma": "Povertà", "Macro": "Questioni sociali", "Connessioni": []},
    {"Lemma": "Problemi dell'informazione", "Macro": "Cultura, storia, spettacolo", "Connessioni": ['Fake news', 'Carta stampata', 'Questioni legate al giornalismo']},
    {"Lemma": "Processi giudiziari", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "Proteste e mobilitazioni", "Macro": "Questioni sociali", "Connessioni": []},
    {"Lemma": "Pubblica amministrazione", "Macro": "Politica interna", "Connessioni": []},
    {"Lemma": "Questioni di genere", "Macro": "Questioni sociali", "Connessioni": ['Gender gap', 'aborto', 'organizzazione dei consultori']},
    {"Lemma": "Questioni giovanili", "Macro": "Questioni sociali", "Connessioni": ['Bullismo']},
    {"Lemma": "Questioni interreligiose", "Macro": "Religione", "Connessioni": []},
    {"Lemma": "Questioni legate all'infanzia", "Macro": "Questioni sociali", "Connessioni": ['Diritti dei bambini', 'Pedofilia']},
    {"Lemma": "Referendum", "Macro": "Politica interna", "Connessioni": []},
    {"Lemma": "Religione", "Macro": "Religione", "Connessioni": []},
    {"Lemma": "Ricerca scientifica", "Macro": "Scienza e tecnologia", "Connessioni": []},
    {"Lemma": "Riforme fiscali e imposte", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Riforme istituzionali", "Macro": "Politica interna", "Connessioni": ['Premierato']},
    {"Lemma": "Riforme sanitarie", "Macro": "Salute e sanità", "Connessioni": []},
    {"Lemma": "Riforme scolastiche", "Macro": "Istruzione", "Connessioni": []},
    {"Lemma": "Risorse natrali", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Robotica e automazione", "Macro": "Scienza e tecnologia", "Connessioni": []},
    {"Lemma": "Salute mentale", "Macro": "Salute e sanità", "Connessioni": []},
    {"Lemma": "Salute", "Macro": "Salute e sanità", "Connessioni": []},
    {"Lemma": "Scuola", "Macro": "Istruzione", "Connessioni": []},
    {"Lemma": "Servizi finanziari e istituzioni bancarie", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Sindacati", "Macro": "Politica interna", "Connessioni": []},
    {"Lemma": "Sistema carcerario", "Macro": "Criminalità e cronaca nera", "Connessioni": ["Violenze all'interno delle carceri", 'Sovraffollamento carcerario']},
    {"Lemma": "Sistema sanitario nazionale", "Macro": "Salute e sanità", "Connessioni": ["Carenza di medici", "Finanziamento della sanità pubblica"]},
    {"Lemma": "Social media", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Sostenibilità ambientale", "Macro": "Ambiente e natura", "Connessioni": []},
    {"Lemma": "Sport", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Storia", "Macro": "Cultura, storia, spettacolo", "Connessioni": ['Commemorazioni storiche']},
    {"Lemma": "Storie di vita", "Macro": "Costume e società/curiosità e cronaca rosa", "Connessioni": ['Relazioni sentimentali', 'Relazioni familiari', 'Relazioni di amicizia', 'Relazioni di vicinato']},
    {"Lemma": "Sudamerica", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Teatro", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Tensioni religiose", "Macro": "Religione", "Connessioni": []},
    {"Lemma": "Terrorismo", "Macro": "Difesa e sicurezza", "Connessioni": []},
    {"Lemma": "Trasporti", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "Trattati e accordi internazionali", "Macro": "Esteri e politica estera", "Connessioni": []},
    {"Lemma": "Truffa", "Macro": "Criminalità e cronaca nera", "Connessioni": []},
    {"Lemma": "Turismo", "Macro": "Economia e finanza", "Connessioni": []},
    {"Lemma": "TV", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Università", "Macro": "Istruzione", "Connessioni": []},
    {"Lemma": "Valori e ideologie", "Macro": "Politica interna", "Connessioni": ['Fascismo e antifascismo', 'Costituzione']},
    {"Lemma": "Videogiochi", "Macro": "Cultura, storia, spettacolo", "Connessioni": []},
    {"Lemma": "Violenza di genere", "Macro": "Criminalità e cronaca nera", "Connessioni": ["Molestie sessuali", 'Femminicidi', 'Stalking', 'Usa solo se è esplicita nel testo la presenza di una donna come vittima']},
    {"Lemma": "Violenza e criminalità comune", "Macro": "Criminalità e cronaca nera", "Connessioni": ['Risse', 'Furti', 'Rapine']},
    {"Lemma": "Volontariato", "Macro": "Questioni sociali", "Connessioni": ["Associazionismo"]}
]

categorie_tematiche = [
    {"Lemma": "Africa", "Macro": "Esteri e politica estera", "Connessioni": ["Sahel", "Paesi del Maghreb", "Paesi Subsahariani"]},
    {"Lemma": "Agricoltura", "Macro": "Economia"},
    {"Lemma": "Alimentazione", "Macro": "Salute e sanità"},
    {"Lemma": "America", "Macro": "Esteri e politica estera"},
    {"Lemma": "Animali", "Macro": "Ambiente e natura"},
    "Anziani",
    "Arte",
    "Asia",
    "Bambini",
    "Banche",
    "Benessere",
    "Calcio",
    "Cambiamenti climatici",
    "Campagna elettorale",
    "Cancro",
    "Catastrofi naturali",
    "Celebrità",
    "Chiesa",
    "Cina",
    "Cinema",
    "Clima",
    "Consumatori",
    "Corruzione",
    "Criminalità",
    "Cronaca",
    "Cucina",
    "Cultura",
    "Democrazia",
    "Diagnosi",
    "Digitale",
    "Diplomazia",
    "Diritti delle donne",
    "Diritti umani",
    "Disabilità",
    "Discriminazione",
    "Disoccupazione",
    "Droga",
    "Ecologia",
    "Economia",
    "Educazione",
    "Elezioni",
    "Energia",
    "Epidemie",
    "Europa",
    "Fai da te",
    "Fake news",
    "Famiglia",
    "Farmaci",
    "Fiction",
    "Finanza",
    "Fisco",
    "Gas",
    "Giovani",
    "Giustizia",
    "Globalizzazione",
    "Governo",
    "Guerra",
    "Identità",
    "Immigrazione",
    "Incidente",
    "Industria",
    "Influencer",
    "Informazione",
    "Innovazione",
    "Inquinamento",
    "Intelligenza artificiale",
    "Intrattenimento",
    "Lavoro",
    "Lavoro precario",
    "LGBTQ",
    "Libri",
    "Locale",
    "Made in Italy",
    "Mafia",
    "Maggioranza",
    "Malattie",
    {"Lemma": "Medicina", "Macro": "Salute e sanità"}, #???
    {"Lemma": "Medio Oriente", "Macro": "Esteri e politica estera"},
    {"Lemma": "Meteo",  "Macro": "Cronaca"},
    {"Lemma": "Automotive", "Macro": "Economia"},
    {"Lemma": "Moda", "Macro": "Costume e società"}, #???
    {"Lemma": "Multinazionali", "Macro": "Economia"}, #???
    {"Lemma": "Musica", "Macro": "Cultura storia e spettacolo"},
    {"Lemma": "NATO", "Macro": "Esteri e politica estera"},
    {"Lemma": "Energia nucleare", "Macro": "Economia"},
    {"Lemma": "Omicidio", "Macro": "Criminalità"},
    {"Lemma": "ONU", "Macro": "Esteri e politica estera"},
    {"Lemma": "Opposizioni", "Macro": "Politica interna"},
    {"Lemma": "Pubblica amministrazione", "Macro": "Politica interna"},
    {"Lemma": "Partiti", "Macro": "Politica interna"},
    {"Lemma": "Pensioni", "Macro": "Economia"},
    {"Lemma": "Petrolio", "Macro": "Economia"},
    {"Lemma": "Piccole medie imprese", "Macro": "Economia"},
    #"Politica interna", -> Macro
    #"Politica internazionale", -> Macro
    {"Lemma": "Povertà", "Macro": "Questioni sociali"},
    {"Lemma": "Prevenzione", "Macro": "Salute e sanità"},
    {"Lemma": "Psicologia", "Macro": "Salute e sanità"},
    {"Lemma": "Razzismo", "Macro": "Questioni sociali"},
    {"Lemma": "Referendum",  "Macro": "Politica interna"},
    {"Lemma": "Religione", "Macro": "Religione"},
    {"Lemma": "Ricerca scientifica", "Macro": "Scienza e Tecnologia"},
    {"Lemma": "Riciclo rifiuti", "Macro": "Ambiente e natura"},
    {"Lemma": "Riforme istituzionali", "Macro": "Politica interna"},
    {"Lemma": "Energie rinnovabili", "Macro": "Ambiente e natura"},
    #"Salute", -> Macro
    {"Lemma": "Salute mentale", "Macro": "Salute e sanità"},
    #"Sanità", -> Macro
    #"Scienza", -> Macro
    {"Lemma": "Scuola", "Macro": "Istruzione"},
    {"Lemma": "Sindacati", "Macro": "Economia"}, #??? Possibili diverse declinazioni del tema
    {"Lemma": "Social network", "Macro": ["Cultura storia e spettacolo", "Scienza e Tecnologia"]}, #Fattibilità informatica di una seconda riclassificazione
    {"Lemma": "Sostenibilità ambientale", "Macro": "Ambiente e natura"},
    #"Sport", -> Macro
    {"Lemma": "Storia", "Macro": "Cultura storia e spettacolo"},
    {"Lemma": "Sud America", "Macro": "Esteri e politica estera"},
    {"Lemma": "Teatro", "Macro": "Cultura storia e spettacolo"},
    #"Tecnologia", ? Come suddividerlo? -> Macro
    {"Lemma": "Terapie", "Macro": "Salute e sanità"}, #?
    {"Lemma": "Terrorismo internazionale", "Macro": "Esteri e politica estera"},
    {"Lemma": "Terrorismo interno", "Macro": "Difesa e sicurezza"},
    {"Lemma": "Trasporti", "Macro": "Economia"},
    {"Lemma": "Truffe", "Macro": "Criminalità"},
    {"Lemma": "Turismo", "Macro": "Costume e società"}, #Questione della possibile declinazione in diversi frame
    {"Lemma": "Tv", "Macro": "Cultura storia e spettacolo"}, #Questione della possibile declinazione in diversi frame
    {"Lemma": "Ue", "Macro": "Esteri e politica estera"},
    {"Lemma": "Vaccini", "Macro": "Salute e sanità"},
    {"Lemma": "Violenza di genere", "Macro": "Questioni sociali"},
    {"Lemma": "Altro", "Macro": "Altro"},
    {"Lemma": "NR", "Macro": "Non classificato"}
]

categorie_mood_emotivo = [
    'anticipation',
    'anger',
    'disgust',
    'fear',
    'joy',
    'sadness',
    'surprise',
    'trust'
]

categorie_sentiment_analysis = [
    'positivo',
    'negativo',
    'neutro',
    'non pertinente'
]

categorie_temi_macro = [

]