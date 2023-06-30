# Heatmap feito utilzando cores

#importando módulo principal

import modulo_principal as mp

def heatmap_cores():
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
    legendas = ["61", "26", "25", "29",
                "71", "69", "40", "43",
                "52", "43", "33", "43",
                "40", "23", "14", "9"]

    data = {"frequencia_eixo_x": frequencia_eixo_x, 
            "frequencia_eixo_y": frequencia_eixo_y,
            "gradacao_de_cores": gradacao_de_cores,
            "legendas": legendas}
    source = mp.ColumnDataSource(data = data)
    # Criando o gráfico em si

    mp.output_file("grafico_frequencia_classica_X_frequencia_metal.html")

    heatmap_cores = mp.figure(x_range = ["Never", "Rarely", "Sometimes", "Very frequently"],
                       y_range = ["Never", "Rarely", "Sometimes", "Very frequently"], width = 1000)
    heatmap_cores.rect(x = "frequencia_eixo_x", y = "frequencia_eixo_y", color= "gradacao_de_cores", width = 1, height = 1, legend_field = "legendas", source = source)

    # Personalizações gerais do gráfico
        # Título
    heatmap_cores.title = "Heatmap feito com cores frequência ouve metal X frequência ouve clássica"
    heatmap_cores.title_location = "above"
    heatmap_cores.title.align = "center"
    heatmap_cores.title.text_font_size = "20px"
    heatmap_cores.title.text_font = "Arial"
    heatmap_cores.title.background_fill_color = "#CCCAC6"
    heatmap_cores.title.background_fill_alpha = 0.5
    heatmap_cores.title.border_line_color = "black"
    heatmap_cores.title.border_line_alpha = 0.5
        # Fundo
    heatmap_cores.background_fill_color = "#FFFDF7"
    heatmap_cores.grid.grid_line_alpha = 0.2
        # Eixos
    heatmap_cores.axis.axis_label_text_font = "Arial"
    heatmap_cores.axis.axis_label_text_font_size = "20px"

    # Personalização específica do gráfico
        # Eixo
    heatmap_cores.xaxis.axis_label = "frequência metal"
    heatmap_cores.yaxis.axis_label = "frequência música clássica"
        # Legenda
    heatmap_cores.legend.background_fill_alpha = 0.0
    heatmap_cores.legend.border_line_alpha = 0.0
    heatmap_cores.legend.label_text_font_size = "15px"
    heatmap_cores.legend.label_text_color = "white"
    
    return heatmap_cores
