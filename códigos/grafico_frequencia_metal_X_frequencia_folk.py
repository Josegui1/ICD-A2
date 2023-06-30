# Gráfico categórico de tamanho

#importando módulo principal

import modulo_principal as mp

def catplot_tamanho():
    
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
    tamanhos_ordenados_em_string = list(map(str, tamanhos_ordenados))

    data = {"frequencia_eixo_x": frequencia_eixo_x, 
            "frequencia_eixo_y": frequencia_eixo_y, 
            "tamanhos_ordenados": tamanhos_ordenados,
            "tamanhos_ordenados_em_string": tamanhos_ordenados_em_string}
    source = mp.ColumnDataSource(data = data)

    # Criando o gráfico em si

    mp.output_file("grafico_frequencia_metal_X_frequencia_folk.html")

    catplot_tamanho = mp.figure(x_range = ["Never", "Rarely", "Sometimes", "Very frequently"],
                       y_range = ["Never", "Rarely", "Sometimes", "Very frequently"], width = 1000)
    catplot_tamanho.circle(x = "frequencia_eixo_x", y = "frequencia_eixo_y", size = "tamanhos_ordenados", color = "#FF9578", source = source)
    numeros = mp.LabelSet(x = "frequencia_eixo_x", y = "frequencia_eixo_y",
                          text = "tamanhos_ordenados_em_string",
                          x_offset=-9, y_offset=-6, text_color = "black",
                          source = source, render_mode = "canvas")

    catplot_tamanho.add_layout(numeros)

    # Personalizações gerais do gráfico
        # Título
    catplot_tamanho.title = "Gráfico categórico de tamanho frequência ouve folk X frequência ouve metal"
    catplot_tamanho.title_location = "above"
    catplot_tamanho.title.align = "center"
    catplot_tamanho.title.text_font_size = "20px"
    catplot_tamanho.title.text_font = "Arial"
    catplot_tamanho.title.background_fill_color = "#CCCAC6"
    catplot_tamanho.title.background_fill_alpha = 0.5
    catplot_tamanho.title.border_line_color = "black"
    catplot_tamanho.title.border_line_alpha = 0.5
        # Fundo 
    catplot_tamanho.background_fill_color = "#FFFDF7"
    catplot_tamanho.grid.grid_line_alpha = 0.2
        # Eixos
    catplot_tamanho.axis.axis_label_text_font = "Arial"
    catplot_tamanho.axis.axis_label_text_font_size = "20px"

    # Personalização específica do gráfico
        # Eixo
    catplot_tamanho.xaxis.axis_label = "frequência metal"
    catplot_tamanho.yaxis.axis_label = "frequência folk"
    
    return catplot_tamanho
    
  # Esse gráfico, por alguma razão que desconheço, não pode ser posto no server em bokeh