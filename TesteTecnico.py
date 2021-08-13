'''
1) Desenvolva um script em python para retornar o primeiro valor não repetido de uma string.

Exemplo:
input -> 'teste'
output -> 's'
input -> 'engenharia de dados'
output -> 'g'
'''

# Script:


# Primeiramente, foi criada uma função, que será chamada mais tarde

# Essa função tem por responsabilidade percorrer toda a string e diferenciar as letras na dada palavra ou frase inserida e, por fim, acusar àquela primeira que não possui repetição

# Caso só existam letras que possuem repetição, a função retornará que não existem palavras ou letras únicas, isto é, sem repetição, na palavra ou frase inserida.

def first_letter_without_repetition(string):
    letters_order = []
    counting = {}
    for i in string:
        if i in counting:
            counting[i] += 1
        else:
            counting[i] = 1
            letters_order.append(i)
    for i in letters_order:
        if counting[i] == 1:
            return i
    return ("Não há letras únicas, isto é, sem repetição, na palavra ou frase inserida.")

# Agora, chama-se a função first_letter_without_repetition, ao mesmo tempo que se pede ao usuário que insira uma palavra ou frase e, para o caso do mesmo inserir um número, str converte imediatamente o mesmo para string

# Também colocasse o .lower() para minimizar todas as letras inseridas pelo usuário, para que o script considere todas  as letras igualmente, pois o Python é case sensitive

print(first_letter_without_repetition(input("Digite uma palavra ou frase aqui: ")))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
# 2) O conjunto de dados flor Íris ou conjunto de dados Íris de Fisher é um conjunto de dados multivariados introduzido pelo estatístico e biólogo britânico Ronald Fisher em seu artigo de 1936. 
Desenvolva um script em python para encontrar a média do petal_length de cada espécie presente no dataset. 
Utilize a função pd.read_csv() para baixar o conteúdo disponível na url https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv
'''

# Script:

# Primeiro, importam-se as bibliotecas necessárias para o script

import pandas as pd
import numpy as np

# Usa-se a biblioteca pandas para importa o dataset, em csv, para o nosso script

flowers = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print(flowers)

# Agora, separam-se as espécies em um set, apenas para conferir quantas espécies diferentes existem no dataset, para fins de análise e conferência

species = set(flowers.species)

print(species)

number_of_species = len(set(flowers.species))

print(number_of_species)

# Agora, utiliza-se o summary, da biblioteca numpy, para mostrar um apanhado estatístico geral do dataset

summary = flowers.describe()

print(summary)

# Agora, finalmente, agrupa-se o dataset nas 3 espécies vistas anteriormente e calcula-se a média de suas colunas, incluindo a requisitada petal_length

flowers.groupby("species").agg(["mean"])
