#coding: utf-8
#O arquivo contém questões definidas com sua respectiva
import json
# respostas, dificuldades e alternativas
with open("questoes.json") as file:
    questoes = json.load(file)
with open("opcoes.json") as file:
    opcoes = json.load(file)
with open("dificuldades.json") as file:
    dificuldade = json.load(file)

def atualizacao_de_arquivos():
    with open("questoes.json", "w") as outfile:
        json.dump(questoes, outfile)
    with open("dificuldades.json", "w") as outfile:
        json.dump(dificuldade, outfile)
    with open("opcoes.json", "w") as outfile:
        json.dump(opcoes, outfile)

exec(open("Perguntas_Definidas.py").read())
#print(questoes)
#print(alternativa)
#print(dificuldade)
#print(opcoes)

