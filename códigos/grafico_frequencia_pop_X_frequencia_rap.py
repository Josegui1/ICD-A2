# importando módulo principal

import modulo_principal as mp

crosstab = mp.pd.crosstab(mp.dataframe["Frequency [Rap]"], mp.dataframe["Frequency [Pop]"])
print(crosstab)

# servindo os dados ao ColumnsDataSource

frequencia_eixo_x = ["Never", "Rarely", "Sometimes", "Very frequently",
                     "Never", "Rarely", "Sometimes", "Very frequently",
                     "Never", "Rarely", "Sometimes", "Very frequently",
                     "Never", "Rarely", "Sometimes", "Very frequently"]
frequencia_eixo_y = ["Never", "Never", "Never", "Never",
                     "Rarely", "Rarely", "Rarely", "Rarely",
                     "Sometimes", "Sometimes", "Sometimes", "Sometimes",
                     "Very frequently", "Very frequently", "Very frequently", "Very frequently"]

gradiente = [0.330, 0.510, 0.630, 0.570,
             0.090, 0.390, 0.930, 0.750,
             0.150, 0.270, 0.690, 0.870,
             0.030, 0.210, 0.450, 0.810]

#O gráfico em si

mp.output_file("grafico_frequencia_rap_X_frequencia_pop.html")

figure = mp.figure(x_range = ["Never", "Rarely", "Sometimes", "Very frequently"],
                   y_range = ["Never", "Rarely", "Sometimes", "Very frequently"])
figure.square(x = frequencia_eixo_x, y = frequencia_eixo_y, color = "darkred", fill_alpha = gradiente, size = 100)
mp.show(figure)

