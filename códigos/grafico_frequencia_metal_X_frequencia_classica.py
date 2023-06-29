#importando módulo principal

import modulo_principal as mp

crosstab = mp.pd.crosstab(mp.dataframe["Frequency [Classical]"], mp.dataframe["Frequency [Metal]"])
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
gradacao_de_cores = [(181, 30, 27), (73, 12, 11), (54, 9, 8), (91, 15, 14),
                     (218, 36, 32), (200, 33, 30), (127, 21, 19), (145, 24, 22),
                     (163, 27, 24), (145, 24, 22), (109, 18, 16), (145, 24, 22),
                     (127, 21, 19), (36, 6, 5), (18, 3, 3), (0, 0, 0)]

# Criando o gráfico em si

mp.output_file("grafico_frequencia_classica_X_frequencia_metal.html")

figure = mp.figure(x_range = ["Never", "Rarely", "Sometimes", "Very frequently"],
                   y_range = ["Never", "Rarely", "Sometimes", "Very frequently"])
figure.square(x = frequencia_eixo_x, y = frequencia_eixo_y, color= gradacao_de_cores, size = 100)
mp.show(figure)