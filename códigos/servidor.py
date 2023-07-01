# Fazendo o servidor 

# Importando o módulo principal e os gráficos

import modulo_principal as mp
import grafico_bpm_X_distribuicao_de_frequencia 
import grafico_idade_X_horas_musica_por_dia 
import grafico_frequencia_genero_mais_ouvido
import grafico_frequencia_rap_X_frequencia_surtos_depressivos
import grafico_frequencia_classica_X_distribuição_idade
import grafico_frequencia_metal_X_frequencia_insonia
import grafico_frequencia_metal_X_frequencia_classica
#import grafico_frequencia_metal_X_frequencia_folk
#import grafico_frequencia_pop_X_frequencia_rap

def bokeh_app(doc):
    
    # Gráficos
    grafico_1 = grafico_bpm_X_distribuicao_de_frequencia.linechart_simples()
    grafico_2 = grafico_idade_X_horas_musica_por_dia.scatterplot_simples()
    grafico_3 = grafico_frequencia_genero_mais_ouvido.barras_horizontais()
    grafico_4 = grafico_frequencia_rap_X_frequencia_surtos_depressivos.scatterplot_multiplo()
    grafico_5 = grafico_frequencia_classica_X_distribuição_idade.histograma_empilhado()
    grafico_6 = grafico_frequencia_metal_X_frequencia_insonia.linechart_empilhado()
    grafico_7 = grafico_frequencia_metal_X_frequencia_classica.heatmap_cores()
#   grafico_8 = grafico_frequencia_metal_X_frequencia_folk.catplot_tamanho()
#   grafico_9 = grafico_frequencia_pop_X_frequencia_rap.heatmap_transparencia()

    # Arrumando os textos que acompanham os gráficos
    
    espaco = mp.Paragraph(text = """                      """, width = 100, height = 200)
    
    text_1 = mp.Paragraph(text = """Ao lado vê-se um gráfico linechart simples utilizado para plotar duas variáveis quantitativas:
                          o BPM das músicas e a frequência que eles ocorrem. Assim, pode-se observar qual a distribuição de BPMs 
                          mais comuns.""", width = 100, height = 400, align = "center")
    text_2 = mp.Paragraph(text = """Aqui vê-se ao lado um scatterplot simples utilizando novamente duas variáveis quantitativas:
                          a idade e a quantidade de horas de músicas ouvidas no dia, para evidêniar se há alguma correlação
                          entre as duas variáveis.""", width = 100, height = 400, align = "center")
    text_3 = mp.Paragraph(text = """Neste vê-se um gráfico de barras para uma variável quantitativa, os estilos de música, e outra
                          variável quantitativa, a frequência de cada categoria.""", width = 100, height = 400, align = "center")
    text_4 = mp.Paragraph(text = """Neste outro, vê-se um scatterplot para cada categoria. O scatterplot se deve porque para cada 
                          categoria estamos analisando duas variáveis quantivativas: a frequência absoluta de pessoas e a frequência 
                          de vezes que elas presenciam casos depressivos (varia entre 0 e 10).""",
                          width = 100, height = 400, align = "center")
    text_5 = mp.Paragraph(text = """Este gráfico ao lado apresenta histogramas empilhados para representar a distribuição de idade.
                          Para cada categoria mediu-se a idade e a frequência com que aparece para se fazer os histogramas.""",
                          width = 100, height = 400, align = "center")
    text_6 = mp.Paragraph(text = """Neste outro pode-se observar um linechart simples para cada categoria da variável frequência
                          ouve metal, formando um linechart empilhado. Para cada categoria mediu-se a frequência absoluta de pessoas
                          com casos de insônia e a frequência que eles ocorrêm (varia entre 0 e 10).""", width = 100, height = 400, align = "center")
    text_7 = mp.Paragraph(text = """Por fim, este gráfico apresenta um heatmap feito com cores para as categorias frequência ouve
                          metal e frequência ouve música clássica. Cada cor representa uma frequência de pessoas anotada na legenda,
                          que, pela interatividade do bokeh, pode ser posta em cima de cada cor para ver o número de pessoas que a
                          cor representa""", width = 100, height = 400, align = "center")
    texto_explicativo = mp.Paragraph(text = """Quanto aos outros dois gráfico, não pude colocá-los nesta página porque eles não somente não apareciam, 
                                     como também impediam a geração da página como um todo. Desse modo, achei prudente removê-los e deixar
                                     apenas os que funcionaram, dado que nem consigo compreender de onde surgiu este erro. A minha hipótese
                                     é que se trata de algum problema ao gerar números no gráfico, dado que os dois gráficos ausentes 
                                     possuíam números plotados. De toda forma, eles são visíveis em pdf pelo github e seus códigos fontes também.""", 
                                     width = 1000, height = 50, align = "center")
#   text_8 = mp.Paragraph(text = """Ao""", width = 400, height = 500)
#   text_9 = mp.Paragraph(text = """Ao""", width = 400, height = 500)

    # Arrumando o layout
    
    layout_1 = mp.row(grafico_1, espaco, text_1)
    layout_2 = mp.row(grafico_2, espaco, text_2)
    layout_3 = mp.row(grafico_3, espaco, text_3)
    layout_4 = mp.row(grafico_4, espaco, text_4)
    layout_5 = mp.row(grafico_5, espaco, text_5)
    layout_6 = mp.row(grafico_6, espaco, text_6)
    layout_7 = mp.row(grafico_7, espaco, text_7)
    layout_texto_explicativo = mp.row(espaco, texto_explicativo)
#   layout_8 = mp.row(grafico_8, text_8)
#   layout_9 = mp.row(grafico_9, text_9)
    
    # Colocando-os no server
    doc.add_root(layout_1)
    doc.add_root(layout_2)
    doc.add_root(layout_3)
    doc.add_root(layout_4)
    doc.add_root(layout_5)
    doc.add_root(layout_6)
    doc.add_root(layout_7)
    doc.add_root(layout_texto_explicativo)
#   doc.add_root(mp.row(layout_8)
#   doc.add_root(mp.row(layout_9))


# Rodadando o server

server = mp.Server({'/': bokeh_app}, allow_websocket_origin=["localhost:5006"])
server.start()
server.io_loop.add_callback(server.show, "/")
server.io_loop.start()

