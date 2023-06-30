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
    
    # Colocando-os no server
    doc.add_root(mp.row(grafico_1))
    doc.add_root(mp.row(grafico_2))
    doc.add_root(mp.row(grafico_3))
    doc.add_root(mp.row(grafico_4))
    doc.add_root(mp.row(grafico_5))
    doc.add_root(mp.row(grafico_6))
    doc.add_root(mp.row(grafico_7))
#   doc.add_root(mp.row(grafico_8))
#   doc.add_root(mp.row(grafico_9))


# Rodadando o server
server = mp.Server({'/': bokeh_app})
server.start()
server.io_loop.add_callback(server.show, "/")
server.io_loop.start()

