#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import config
import sys
import datetime
from pymongo.errors import ConnectionFailure


def IMPORT_DOCS_IN_MONGO(doc, mydb):
    #    try:
    mydb.insert_one(doc)

def CONNECT_MONGODB(db, collection):
    try:
        c = pymongo.MongoClient('mongodb://localhost:27017/')
    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

    config.connessione_mongodb = True

    mydb = c[db][collection]
    return mydb

def CLOSE_CONNECTION(db):

    db.client.close()

def GET_POSITION_INDEX(mydb, testata, giorno_cares):
    search_dict = {"$and": [
        {"Data_Cares": giorno_cares},
        {"Testata": testata}
    ]}

    max_index = mydb.count_documents(search_dict)

    print(max_index)

    return max_index

def AGGIORNAMENTO_LOG_DB (db: object, giorno_cares: object, data: object, testata: object, rete: object) -> object:

    log_db = CONNECT_MONGODB(db, 'log_programmi_trascritti')

    log_doc = {
        'giorno_cares' : giorno_cares ,
        'data' : data,
        'testata' : testata ,
        'rete'  : rete ,
        'trascritto' : 1 ,
        'esportato' : 1 ,
        't_salvataggio' : datetime.datetime.now()
    }

    IMPORT_DOCS_IN_MONGO(log_doc, log_db)

def lista_programmi_trascritti_per_giorno (giorno):

    mydb = CONNECT_MONGODB('MEDIA', 'log_programmi_trascritti')
    search_dict = {'giorno_cares': giorno}

    n_docs = mydb.count_documents(search_dict)

    if n_docs > 0:
        response = mydb.find (search_dict)
        programmi_trascritti = [elemento['testata'] for elemento in response]
    else:
        programmi_trascritti = []

    return programmi_trascritti

