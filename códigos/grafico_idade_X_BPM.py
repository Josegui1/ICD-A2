#Importando o módulo principal

import modulo_principal as mp

#Criando o ColumnDataSource referente ao gráfico proposto

data = {"idade" : mp.dataframe["Age"], "BPM" : mp.dataframe["BPM"]}
source = mp.ColumnDataSource(data = data)

#Criando o gráfico em si

mp.output_file("Idade_X_BPM.html")

figure = mp.figure()
figure.triangle(x = "idade", y = "BPM", source = source)
mp.show(figure)

