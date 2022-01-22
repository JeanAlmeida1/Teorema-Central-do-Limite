# -*- coding: utf-8 -*-
"""testando o teorema central do limite.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y2z_2cHuTyuZJ9jZ2OpHIQqnN7q3KV6O
"""

import numpy as np
import random 
import matplotlib.pyplot as plt
import seaborn as sns

"""#TEOREMA CENTRAL DO LIMITE

O Teorema do Limite Central é um dos conceitos mais importantes da estatística. Ele nos diz que, independente da distribuição populacional, a distribuição das médias amostrais tenderá a uma distribuição normal na medida que o tamanho das amostras aumenta.

Consideremos uma população qualquer, com média e desvio padrão bem definidos, que siga uma distribuição de probabilidade qualquer. Podemos retirar várias amostras dessa população, tirar a média de cada uma delas e plotar uma distribuição das médias amostrais. Independente da distribuição da população, essa distribuição das médias amostrais tenderá a uma distribuição normal na medida que nosso "n" aumenta, com média igual à média populacional e desvio padrão amostral igual ao desvio padrão populacional dividido por $\sqrt{n}$. 

"""

#Criando uma população de 10000 elementos que não obedecem a uma distribuição normal. Como exemplo, vou gerar valores que obedecem a uma distribuição exponencial:

pop = []
for i in range(0,10000):
  pop.append(random.expovariate(1))

#Plotando o histograma da população

sns.displot(pop, kind='hist', kde=False, bins=50, color='mediumslateblue')

plt.title('Histograma da população', fontsize=20, color='mediumslateblue')
plt.xlabel('Values')

#Criando 100 amostras de diferentes tamanhos. Por exemplo,as 100 amostras de tamanho 30 cada serão salvas na lista A2, e a média da média dessas amostras, na variável M2.

n = [10,30,100,300]

A1 = []
M1 = []
A2 = []
M2 = []
A3 = []
M3 = []
A4 = []
M4 = []

amostras= [A1,A2,A3,A4]
medias = [M1,M2,M3,M4]

for j in range(0,4):
  for i in range(0,100):
    amostras[j].append(random.sample(pop,k=n[j]))
    medias[j].append(np.mean(amostras[j]))

medias = [M1,M2,M3,M4]

print('A média da população é: {0:.4f}. '.format(np.mean(pop)))
for i in range(0,4):
  print('A média das média amostrais de tamanho {} é: {:.4f}.'.format(n[i],np.mean(medias[i])))

"""Podemos ver que a média amostral se aproxima da média populacional na medida que temos amostras maiores. """

#Plotando a distribuição das médias amostrais


sns.set_theme('talk',style='whitegrid', palette='bright')
fig = sns.displot(medias, aspect=4, kde=True, legend=False)
sns.set_style("whitegrid")
legenda = ['n = 10', 'n = 30', 'n = 100', 'n = 300']
plt.legend(title='Tamanho das amostras', loc='upper left', labels=legenda)
plt.xlabel('Values')
plt.title('Distribuições das médias amostrais', loc='center', fontsize=30, color='mediumslateblue')
plt.show()

"""Podemos perceber que na medida que o tamanho das amostras aumenta, a distribuição tende a uma normal, mesmo que a população obedeça uma distribuição diferente (que no nosso exemplo, era a exponencial). """

#ANALISANDO O DESVIO PADRÃO

print('O desvio padrão da população é: {0:.4f}. '.format(np.std(pop)))
for i in range(0,4):
  print('O desvio padrão da média amostral de tamanho {} é: {:.4f}.'.format(n[i],np.std(medias[i])))

"""No caso, o desvio padrão não converge ao desvio padrão populacional, e sim à fórmula STD amostral = *STD populacional* / $\sqrt{n}$

Portanto quanto maior o tamanho da amostra, menor o desvio padrão amostral. 
"""