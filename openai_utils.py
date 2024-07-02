#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Modulo di interfaccia tra MongoDB e OpenAI per l'indicizzazione automatica del materiale
"""

import openai
import secret_key_openai
import json
import pandas as pd
from utilities import extract_after_slash

import openai_prompts

openai.api_key = secret_key_openai.openai_api_key
def classificazione_adc(record_da_classificare, tipo_analisi, mode):

    print(record_da_classificare.name)

    frame_pertinenti = ['STUDIO',
                        'INIZIO',
                        'FINE',
                        'COLLEGAMENTO ESTERNO',
                        'INTERVISTA']

    if tipo_analisi == 1:
        max_tokens = 16
        prompt = openai_prompts.analisi_tematica
        categorie = [elemento['Lemma'] for elemento in openai_prompts.categorie_tematiche_PROVA]
    elif tipo_analisi == 2:
        max_tokens = 5
        prompt = openai_prompts.analisi_sentiment_ue
        categorie = openai_prompts.categorie_sentiment_analysis
    elif tipo_analisi == 3:
        max_tokens = 5
        prompt = openai_prompts.analisi_sentiment_governo
        categorie = openai_prompts.categorie_sentiment_analysis
    elif tipo_analisi == 4:
        max_tokens = 5
        prompt = openai_prompts.analisi_spettro_emotivo
        categorie = openai_prompts.categorie_mood_emotivo

    prompt = prompt.replace("LISTA_CATEGORIE", f', '.join(categorie))

    if mode == 1:
        prompt = prompt.replace("NOME_EMITTENTE", record_da_classificare["Page Name"])
        prompt = prompt.replace("TIPOLOGIA_EMITTENTE", record_da_classificare["Page Description"])

        if pd.isnull(record_da_classificare["Message"]):
            messaggio = ""
        else:
            messaggio = record_da_classificare["Message"]
        if pd.isnull(record_da_classificare["Image Text"]):
            messaggio = messaggio + ""
        else:
            messaggio = messaggio + "\n" + record_da_classificare["Image Text"]
        if pd.isnull(record_da_classificare["Description"]):
            messaggio = messaggio + ""
        else:
            messaggio = messaggio + "\n" + record_da_classificare["Description"]

        if messaggio == "":
            prompt = prompt.replace("TESTO_MESSAGGIO", "Non riclassificabile")
        else:
            prompt = prompt.replace("TESTO_MESSAGGIO", messaggio)

    elif mode == 3:

        prompt = prompt.replace("ELENCO_INDICAZIONI", prompt_indicazioni (openai_prompts.categorie_tematiche_PROVA))

        prompt = prompt.replace("NOME_PROGRAMMA", record_da_classificare["Programma"])

        if pd.isnull(record_da_classificare["Soggetto"]):
            prompt = prompt.replace("NOME_SOGGETTO", 'Soggetto non presente')
        else:
            prompt = prompt.replace("NOME_SOGGETTO", record_da_classificare["Soggetto"])

        if pd.isnull(record_da_classificare["Carica"]):
            prompt = prompt.replace("RUOLO_SOGGETTO", 'Carica non presente')
        else:
            prompt = prompt.replace("RUOLO_SOGGETTO", record_da_classificare["Carica"])

        if pd.isnull(record_da_classificare["Tema"]):
            prompt = prompt.replace("TESTO_MESSAGGIO", "Notizia non riclassificabile")
        else:
            if record_da_classificare["Tipo_frame"] == "INIZIO":
                prompt = prompt.replace("TESTO_MESSAGGIO", extract_after_slash(record_da_classificare["Tema"]))
            else:
                prompt = prompt.replace("TESTO_MESSAGGIO", record_da_classificare["Tema"])

    if record_da_classificare["Tipo_frame"] in frame_pertinenti:
        prova_analisi = request_completion(prompt, max_tokens).choices[0].message.content.replace('\n', '')
    else:
        prova_analisi = 'NR'

    if prova_analisi.find(',') == -1 and tipo_analisi == 1:
        prova_analisi = prova_analisi + ', NR'

    return prova_analisi

def request_completion(prompt, max_tokens):

    completion_response = openai.chat.completions.create(
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.0,
                            max_tokens=max_tokens,
                            top_p=1,
                            frequency_penalty=0, #Se positivo, incoraggia l'uso di parole rare, se negativo incoraggia l'uso di parole frequenti
                            presence_penalty=0, #Se positivo, incoraggia l'uso di parole non presenti nel prompt
                            model='gpt-4o')

    return completion_response

def check_finetune_classes(train_file,valid_file):

    train_classes = set()
    valid_classes = set()
    with open(train_file, 'r') as json_file:
        json_list = list(json_file)
        print(len(json_list))

    for json_str in json_list:
        result = json.loads(json_str)
        train_classes.add(result['completion'])
        #print(f"result: {result['completion']}")
        #print(isinstance(result, dict))

    with open(valid_file, 'r') as json_file:
        json_list = list(json_file)
        print(len(json_list))

    for json_str in json_list:
        result = json.loads(json_str)
        valid_classes.add(result['completion'])
        #print(f"result: {result['completion']}")
        #print(isinstance(result, dict))

    if len(train_classes) == len(valid_classes):
        print('All good')

    else:
        print('Classes do not match, please prepare data again')

def prompt_indicazioni (dizionario_categorie):
    indicazioni = ''
    for lemma in dizionario_categorie:
        if lemma['Connessioni']:
            connessioni = f', '.join(lemma['Connessioni'])
            indicazioni = indicazioni + f'- Riconduci a "{lemma["Lemma"]}" le Unità di analisi relative a {connessioni}.' + '\n'

    return indicazioni


