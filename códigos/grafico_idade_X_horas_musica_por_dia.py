#Importando o módulo principal

import modulo_principal as mp

#Criando o ColumnDataSource referente ao gráfico proposto

data = {"idade" : mp.dataframe["Age"], "horas por dia" : mp.dataframe["Hours per day"]}
source = mp.ColumnDataSource(data = data)

#Criando o gráfico em si

mp.output_file("Idade_X_Horas_por_dia.html")

figure = mp.figure()
figure.circle(x = "idade", y = "horas por dia", source = source)
mp.show(figure)
