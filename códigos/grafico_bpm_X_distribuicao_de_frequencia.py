# Importando o módulo principal

import modulo_principal as mp

# Criando o ColumnDataSource

frequencia_absoluta_bpm = mp.dataframe["BPM"].value_counts()
frequencia_absoluta_bpm_ordenada = dict(sorted(dict(frequencia_absoluta_bpm).items()))
bpm = list(frequencia_absoluta_bpm_ordenada.keys())
frequencia = list(frequencia_absoluta_bpm_ordenada.values())

# Criando o gráfico em si

mp.output_file("grafico_distribuicao_frequencia_bpm.html")

figure = mp.figure(x_range = (40, 220), y_range = (0, 45))
figure.line(x = bpm, y = frequencia, width = 2)
mp.show(figure)

