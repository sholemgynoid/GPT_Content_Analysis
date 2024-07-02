#!/usr/bin/python
# -*- coding': utf-8 -*-

semaforo_globale = True

connessione_mongodb = False

time_code = {

    '1': {
        'Rete': 'Rai1',
        'Testata': 'TG1',
        'Start': '00:00:00.0',
        'End': '00:40:00.0',
        'File': '1955',
        'Language': 'italian',
        'Language_code': 'it-IT',
        'TG_PT': 1,
        'Date_shift': 0
    } ,
    '2': {
        'Rete': 'Rai2',
        'Testata': 'TG2',
        'Start': '00:30:00.0',
        'End': '01:00:00.0',
        'File': '2000',
        'Language': 'italian',
        'Language_code': 'it-IT',
        'TG_PT': 1,
        'Date_shift': 0
    } ,
    '3': {
        'Rete': 'Rai2',
        'Testata': 'TG2',
        'Start': '00:00:00.0',
        'End': '00:08:00.0',
        'File': '2100',
        'Language': 'italian',
        'Language_code': 'it-IT',
        'TG_PT': 1,
        'Date_shift': 0
    } ,
    '4': {
        'Rete': 'Rai3' ,
        'Testata': 'TG3' ,
        'Start': '00:00:00.0' ,
        'End': '00:38:00.0' ,
        'File': '1900' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 1,
        'Date_shift': 0
    } ,
    '5': {
        'Rete': 'Rete4' ,
        'Testata': 'TG4' ,
        'Start': '00:00:00.0' ,
        'End': '01:15:00.0' ,
        'File': '1850' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 1,
        'Date_shift': 0
    } ,
    '6': {
        'Rete': 'Canale5' ,
        'Testata': 'TG5' ,
        'Start': '00:00:00.0' ,
        'End': '00:40:00.0' ,
        'Language': 'italian' ,
        'File': '1955' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 1,
        'Date_shift': 0
    } ,
    '7': {
        'Rete': 'Italia1' ,
        'Testata': 'StudioAperto' ,
        'Start': '00:30:00.0' ,
        'End': '01:00:00.0' ,
        'File': '1800' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 1,
        'Date_shift': 0
    } ,
    '8': {
        'Rete': 'La7bis' ,
        'Testata': 'TGLa7' ,
        'Start': '00:03:00.0' ,
        'End': '00:30:00.0' ,
        'File': '2000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 1 ,
        'Date_shift': 0
    } ,
    '9': {
        'Rete': 'ARD' ,
        'Testata': 'ARDTagesschau' ,
        'Start': '00:00:00.0' ,
        'End': '00:20:00.0' ,
        'File': '2000' ,
        'Language': 'german' ,
        'Language_code': 'de-DE' ,
        'TG_PT': 2,
        'Date_shift': 0
    } ,
    '10': {
        'Rete': 'RaiNews24' ,
        'Testata': 'RaiNews24' ,
        'Start': '' ,
        'End': '' ,
        'File': '' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 0,
        'Date_shift': 0
    } ,
    '11': {
        'Rete': 'France2' ,
        'Testata': 'JT20Heurs' ,
        'Start': '00:00:00.0' ,
        'End': '00:35:00.0' ,
        'File': '2000' ,
        'Language': 'french' ,
        'Language_code': 'fr-FR' ,
        'TG_PT': 2,
        'Date_shift': 0
    },
    '12': {
        'Rete': 'BBC1' ,
        'Testata': 'BBCNews' ,
        'Start': '00:00:00.0' ,
        'End': '00:35:00.0' ,
        'File': '1900' ,
        'Language': 'english' ,
        'Language_code': 'en-GB' ,
        'TG_PT': 2,
        'Date_shift': 0
    },
    '13': {
        'Rete': 'TVE' ,
        'Testata': 'Telediario' ,
        'Start': '00:00:00.0' ,
        'End': '00:59:59.0' ,
        'File': '2100' ,
        'Language': 'spanish' ,
        'Language_code': 'es-ES' ,
        'TG_PT': 2,
        'Date_shift': 0
    } ,
    '16': {
        'Rete': 'Italia1' ,
        'Testata': 'StudioAperto' ,
        'Start': '00:00:00.0' ,
        'End': '00:28:00.0' ,
        'File': '1900' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 0,
        'Date_shift': 0
    },
    '17': {
        'Rete': 'La7' ,
        'Testata': 'DiMartedì' ,
        'Start': '00:15:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 7,
        'Date_shift': 0
    },
    '18': {
        'Rete': 'La7' ,
        'Testata': 'DiMartedì' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2200' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 7,
        'Date_shift': 0
    },
    '19': {
        'Rete': 'La7' ,
        'Testata': 'DiMartedì' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 7,
        'Date_shift': 0
    },
    '20': {
        'Rete': 'La7' ,
        'Testata': 'DiMartedì' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 7,
        'Date_shift': 1
    },
    '21': {
        'Rete': 'Rai1' ,
        'Testata': 'Portaaporta' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 6,
        'Date_shift': 0
    } ,
    '22': {
        'Rete': 'Rai1' ,
        'Testata': 'Portaaporta' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 6,
        'Date_shift': 1
    } ,
    '23': {
        'Rete': 'Rai1' ,
        'Testata': 'Portaaporta' ,
        'Start': '00:00:00.0' ,
        'End': '00:30:00.0' ,
        'File': '0100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 6,
        'Date_shift': 1
    },
    '24': {
        'Rete': 'Rai3' ,
        'Testata': 'Agorà' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '0800' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 8,
        'Date_shift': 0
    },
    '25': {
        'Rete': 'Rai3' ,
        'Testata': 'Agorà' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '0900' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 8,
        'Date_shift': 0
    },
    '26': {
        'Rete': 'Rai3' ,
        'Testata': 'Cartabianca' ,
        'Start': '00:19:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 9 ,
        'Date_shift': 0
    },
    '27': {
        'Rete': 'Rai3' ,
        'Testata': 'Cartabianca' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2200' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 9 ,
        'Date_shift': 0
    } ,
    '28': {
        'Rete': 'Rai3' ,
        'Testata': 'Cartabianca' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 9 ,
        'Date_shift': 0
    } ,
    '29': {
        'Rete': 'Rai3' ,
        'Testata': 'Cartabianca' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 9 ,
        'Date_shift': 1
    },
    '30': {
        'Rete': 'Rete4' ,
        'Testata': 'Staseraitalia' ,
        'Start': '00:25:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 10 ,
        'Date_shift': 0
    },
    '31': {
        'Rete': 'Rete4' ,
        'Testata': 'Staseraitalia' ,
        'Start': '00:00:00.0' ,
        'End': '00:28:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 10 ,
        'Date_shift': 0
    },
    '32': {
        'Rete': 'La7' ,
        'Testata': 'Ottoemezzo' ,
        'Start': '00:30:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 11 ,
        'Date_shift': 0
    },
    '33': {
        'Rete': 'La7' ,
        'Testata': 'Ottoemezzo' ,
        'Start': '00:00:00.0' ,
        'End': '00:35:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 11 ,
        'Date_shift': 0
    },
    '34': {
        'Rete': 'Rai3' ,
        'Testata': 'Mezzorainpiù' ,
        'Start': '00:35:00.0' ,
        'End': '01:00:00.0' ,
        'File': '1400' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 12 ,
        'Date_shift': 0
    },
    '35': {
        'Rete': 'Rai3' ,
        'Testata': 'Mezzorainpiù' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '1500' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 12 ,
        'Date_shift': 0
    },
    '36': {
        'Rete': 'Rete4' ,
        'Testata': 'Drittoerovescio' ,
        'Start': '00:25:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 14 ,
        'Date_shift': 0
    } ,
    '37': {
        'Rete': 'Rete4' ,
        'Testata': 'Drittoerovescio' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2200' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 14 ,
        'Date_shift': 0
    } ,
    '38': {
        'Rete': 'Rete4' ,
        'Testata': 'Drittoerovescio' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 14 ,
        'Date_shift': 0
    },
    '39': {
        'Rete': 'Rete4' ,
        'Testata': 'Drittoerovescio' ,
        'Start': '00:00:00.0' ,
        'End': '00:55:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 14 ,
        'Date_shift': 1
    },
    '40': {
        'Rete': 'Rete4' ,
        'Testata': 'ZonaBianca' ,
        'Start': '00:26:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 15 ,
        'Date_shift': 0
    },
    '41': {
        'Rete': 'Rete4' ,
        'Testata': 'ZonaBianca' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2200' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 15 ,
        'Date_shift': 0
    },
    '42': {
        'Rete': 'Rete4' ,
        'Testata': 'ZonaBianca' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 15 ,
        'Date_shift': 0
    },
    '43': {
        'Rete': 'Rete4' ,
        'Testata': 'ZonaBianca' ,
        'Start': '00:00:00.0' ,
        'End': '00:45:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 15 ,
        'Date_shift': 1
    },
    '44': {
        'Rete': '' ,
        'Testata': '' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2200' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 16 ,
        'Date_shift': 0
    },
    '45': {
        'Rete': '' ,
        'Testata': '' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 16 ,
        'Date_shift': 0
    },
    '46': {
        'Rete': '' ,
        'Testata': '' ,
        'Start': '00:00:00.0' ,
        'End': '00:25:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 16 ,
        'Date_shift': 1
    },
    '47': {
        'Rete': 'Rai2' ,
        'Testata': 'TG2Post' ,
        'Start': '00:00:00.0' ,
        'End': '00:30:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 17 ,
        'Date_shift': 0
    },
    '48': {
        'Rete': 'France2' ,
        'Testata': 'JT20Heurs' ,
        'Start': '00:55:00.0' ,
        'End': '01:00:00.0' ,
        'File': '1900' ,
        'Language': 'french' ,
        'Language_code': 'fr-FR' ,
        'TG_PT': 2 ,
        'Date_shift': 0
    },
    '49': {
        'Rete': 'Rete4' ,
        'Testata': 'QuartaRepubblica' ,
        'Start': '00:26:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 18 ,
        'Date_shift': 0
    } ,
    '50': {
        'Rete': 'Rete4' ,
        'Testata': 'QuartaRepubblica' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2200' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 18 ,
        'Date_shift': 0
    } ,
    '51': {
        'Rete': 'Rete4' ,
        'Testata': 'QuartaRepubblica' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 18 ,
        'Date_shift': 0
    } ,
    '52': {
        'Rete': 'Rete4' ,
        'Testata': 'QuartaRepubblica' ,
        'Start': '00:00:00.0' ,
        'End': '00:55:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 18 ,
        'Date_shift': 1
    },
    '53': {
        'Rete': 'La7' ,
        'Testata': 'PiazzaPulita' ,
        'Start': '00:10:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 19 ,
        'Date_shift': 0
    },
    '54': {
        'Rete': 'La7' ,
        'Testata': 'PiazzaPulita' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2200' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 19 ,
        'Date_shift': 0
    },
    '55': {
        'Rete': 'La7' ,
        'Testata': 'PiazzaPulita' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 19 ,
        'Date_shift': 0
    },
    '56': {
        'Rete': 'La7' ,
        'Testata': 'PiazzaPulita' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 19 ,
        'Date_shift': 1
    },
    '57': {
        'Rete': 'Rai2' ,
        'Testata': 'TG2Post' ,
        'Start': '00:00:00.0' ,
        'End': '00:25:00.0' ,
        'File': '2100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 20 ,
        'Date_shift': 1
    },
    '58': {
        'Rete': 'Canale5' ,
        'Testata': 'Matrix' ,
        'Start': '00:10:00.0' ,
        'End': '01:00:00.0' ,
        'File': '2300' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 21 ,
        'Date_shift': 0
    },
    '59': {
        'Rete': 'Canale5' ,
        'Testata': 'Matrix' ,
        'Start': '00:00:00.0' ,
        'End': '01:00:00.0' ,
        'File': '0000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 21 ,
        'Date_shift': 1
    },
    '60': {
        'Rete': 'Canale5' ,
        'Testata': 'Matrix' ,
        'Start': '00:00:00.0' ,
        'End': '00:30:00.0' ,
        'File': '0100' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 21 ,
        'Date_shift': 1
    },
    '61': {
        'Rete': 'Rai3' ,
        'Testata': 'Agorà' ,
        'Start': '00:00:00.0' ,
        'End': '00:30:00.0' ,
        'File': '1000' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT' ,
        'TG_PT': 8,
        'Date_shift': 0
    }

}

reti_dic = {
    'Rai1': {
        'Codice' : '1',
        'Testata': 'TG1' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'Rai2': {
        'Codice' : '2',
        'Testata': 'TG2' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'Rai3': {
        'Codice' : '4',
        'Testata': 'TG3' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'Rete4': {
        'Codice' : '5',
        'Testata': 'TG4' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'Canale5': {
        'Codice' : '6',
        'Testata': 'TG5' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'Italia1': {
        'Codice' : '7',
        'Testata': 'StudioAperto' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'La7': {
        'Codice' : '8',
        'Testata': 'TGLa7' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'La7bis': {
        'Codice' : '8',
        'Testata': 'TGLa7' ,
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'ARD': {
        'Codice' : '9',
        'Testata': 'ARDTagesschau' ,
        'Language': 'german' ,
        'Language_code': 'de-DE'
    } ,
    'RaiNews24': {
        'Codice' : '10',
        'Language': 'italian' ,
        'Language_code': 'it-IT'
    } ,
    'BBC1' : {
        'Codice': '12' ,
        'Testata': 'BBCNews' ,
        'Language': 'english' ,
        'Language_code': 'en-GB'
    } ,
    'TVE' : {
        'Codice': '13' ,
        'Testata': 'Telediario' ,
        'Language': 'spanish' ,
        'Language_code': 'es-ES'
    } ,
    'France2' : {
        'Codice': '11' ,
        'Testata': 'JT20Heurs' ,
        'Language': 'french' ,
        'Language_code': 'fr-FR'
    }
    # 'Ellas': {
    #     'Codice': '50' ,
    #     'Testata': 'Ta Nea' ,
    #     'Language': 'greek' ,
    #     'Language_code': 'el-GR'
    # },
    # 'Jornal8': {
    #     'Codice': '51' ,
    #     'Testata': 'Jornal da 8' ,
    #     'Language': 'portuguese' ,
    #     'Language_code': 'pt-PT'
    # }
}

progr_approfondimento = {

    6: {
        'Testata': 'Portaaporta',
        'Rete': 'Rai1'
    },
    7: {
        'Testata': 'Dimartedì',
        'Rete': 'La7'
    },
    8: {
        'Testata': 'Agorà',
        'Rete': 'Rai3'
    },
    9: {
        'Testata': 'Cartabianca' ,
        'Rete': 'Rai3'
    },
    10: {
        'Testata': 'Staseraitalia' ,
        'Rete': 'Rete4'
    },
    11: {
        'Testata': 'Ottoemezzo' ,
        'Rete': 'La7'
    },
    12: {
        'Testata': 'Mezzorainpiù' ,
        'Rete': 'Rai3'
    },
    13: {
        'Testata': 'Nonèlarena' ,
        'Rete': 'La7'
    },
    14: {
        'Testata': 'Dirittoerovescio' ,
        'Rete': 'Rete4'
    },
    15: {
        'Testata': 'ZonaBianca' ,
        'Rete': 'Rete4'
    },
    16: {
        'Testata': 'Popolosovrano' ,
        'Rete': 'Rai2'
    },
    17: {
        'Testata': 'TG2Post' ,
        'Rete': 'Rai2'
    },
    18: {
        'Testata': 'QuartaRepubblica' ,
        'Rete': 'Rete4'
    },
    19: {
        'Testata': 'PiazzaPulita' ,
        'Rete': 'La7'
    },
    20: {
        'Testata': 'TG2Post' ,
        'Rete': 'Rai2'
    },
    21: {
        'Testata': 'Controcorrente' ,
        'Rete': 'Rete4'
    },
    22: {
        'Testata': 'InOnda' ,
        'Rete': 'La7'
    },

}

reti = [
    'Rai1' ,
    'Rai2' ,
    'Rai3' ,
    'Rete4' ,
    'Canale5' ,
    'Italia1' ,
    'La7' ,
    'BBC1' ,
    'France2' ,
    'TVE' ,
    'ARD'
]

# Il dizionario utilizza il giorno della settimana generato da weekday(): 1=lunedì, 2=martedì, ecc

cadenza_programmi = {
    1:[17,18],
    2:[6,7,9,17],
    3:[6,17],
    4:[6,17,14],
    5:[6,17],
    6:[],
    7:[12,15]
}

dizionario_reti = {
    '1': 'Rai1' ,
    '2': 'Rai2' ,
    '3': 'Rai3' ,
    '6': 'Rete4' ,
    '4': 'Canale5' ,
    '5': 'Italia1' ,
    '14': 'La7bis'
}

tipologia_programma = {
    1: 'TG Italiani' ,
    2: 'Approfondimento'
}

# dizionario_TG4 = {
#     'CODICE_TRASCRIZIONE': 2,
#     'DATA_SCALETTA': giorno,
#     'DESCRIZIONE': 'TG4 1855',
#     'ID_GENERE': 1,
#     'ID_RETE': 6,
#     'ORA_FINE_SCALETTA': datetime.time(19, 56, 59),
#     'ORA_INIZIO_SCALETTA': datetime.time(18, 58)}
# }