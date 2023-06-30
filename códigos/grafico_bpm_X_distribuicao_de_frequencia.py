# Linechart de frequencia simples

# Importando o módulo principal

import modulo_principal as mp

def linechart_simples():
    # Criando o ColumnDataSource

    frequencia_absoluta_bpm = mp.dataframe["BPM"].value_counts()
    frequencia_absoluta_bpm_ordenada = dict(sorted(dict(frequencia_absoluta_bpm).items()))

    bpm = list(frequencia_absoluta_bpm_ordenada.keys())
    frequencia = list(frequencia_absoluta_bpm_ordenada.values())

    data = {"bpm": bpm, "frequencia": frequencia}
    source = mp.ColumnDataSource(data = data)

    # Criando o gráfico em si

    mp.output_file("grafico_distribuicao_frequencia_bpm.html")

    linechart_simples = mp.figure(x_range = (40, 220), y_range = (0, 45), width = 1000)
    linechart_simples.line(x = "bpm", y = "frequencia", source = source ,width = 2, color = "#B80601")

    # Personalizações gerais do gráfico
        # Título
    linechart_simples.title = "Linechart simples bpm X frequência nas músicas"
    linechart_simples.title_location = "above"
    linechart_simples.title.align = "center"
    linechart_simples.title.text_font_size = "20px"
    linechart_simples.title.text_font = "Arial"
    linechart_simples.title.background_fill_color = "#CCCAC6"
    linechart_simples.title.background_fill_alpha = 0.5
    linechart_simples.title.border_line_color = "black"
    linechart_simples.title.border_line_alpha = 0.5
        # Fundo
    linechart_simples.background_fill_color = "#FFFDF7"
    linechart_simples.grid.grid_line_alpha = 0.2
        # Eixos
    linechart_simples.axis.axis_label_text_font = "Arial"
    linechart_simples.axis.axis_label_text_font_size = "20px"

    # Personalização específica
    linechart_simples.xaxis.axis_label = "BPM"
    linechart_simples.yaxis.axis_label = "Frequência de músicas com este BPM"
    
    return linechart_simples


