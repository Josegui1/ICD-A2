#importando módulo principal

import modulo_principal as mp

crosstab = mp.pd.crosstab(mp.dataframe["Frequency [Folk]"], mp.dataframe["Frequency [Metal]"])
print(crosstab)

# Servindo o ColumnDataSource

frequencia_eixo_x = ["Never", "Rarely", "Sometimes", "Very frequently",
                     "Never", "Rarely", "Sometimes", "Very frequently",
                     "Never", "Rarely", "Sometimes", "Very frequently",
                     "Never", "Rarely", "Sometimes", "Very frequently"]
frequencia_eixo_y = ["Never", "Never", "Never", "Never",
                     "Rarely", "Rarely", "Rarely", "Rarely",
                     "Sometimes", "Sometimes", "Sometimes", "Sometimes",
                     "Very frequently", "Very frequently", "Very frequently", "Very frequently"]
    # A ideia é associar cada ponto a um tamanho proporcional a quantidade de entrada de uma tabela cruzada que contém os dois valores
tamanhos_ordenados = [126, 44, 39, 38, 55, 62, 27, 40, 26, 38, 30, 32, 17, 17, 16, 14]

# Criando o gráfico em si

mp.output_file("grafico_frequencia_metal_X_frequencia_folk.html")

figure = mp.figure(x_range = ["Never", "Rarely", "Sometimes", "Very frequently"],
                   y_range = ["Never", "Rarely", "Sometimes", "Very frequently"])
figure.square(x = frequencia_eixo_x, y = frequencia_eixo_y, size = tamanhos_ordenados)
mp.show(figure)

