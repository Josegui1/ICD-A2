#Importando o módulo principal

import modulo_principal as mp

#Criando o ColumnDataSource referente ao gráfico proposto

data = {"x_value" : mp.dataframe["Age"], "y_value" : mp.dataframe["Hours per day"]}
source = mp.ColumnDataSource(data = data)

#Criando o gráfico em si

mp.output_file("Idade_X_Horas_por_dia.html")

figure = mp.figure()
figure.circle(x = "x_value", y = "y_value", source = source)
mp.show(figure)
