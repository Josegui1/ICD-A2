# Importando as bibliotecas necessárias
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource

# Criando o dataframe

dataframe = pd.read_csv(r"C:\Users\jguil\Documents\Datasets_for_analysis\Music_and_mental_health_dataset\mxmh_survey_results.csv")

# Limpando o dataframe

dataframe = dataframe.loc[dataframe["BPM"] <= 500] 
dataframe = dataframe.loc[dataframe["BPM"] >= 30] 
dataframe = dataframe.loc[dataframe["Hours per day"] <= 24]

"""
       'Timestamp', 'Age', 'Primary streaming service', 'Hours per day',
       'While working', 'Instrumentalist', 'Composer', 'Fav genre',
       'Exploratory', 'Foreign languages', 'BPM', 'Frequency [Classical]',
       'Frequency [Country]', 'Frequency [EDM]', 'Frequency [Folk]',
       'Frequency [Gospel]', 'Frequency [Hip hop]', 'Frequency [Jazz]',
       'Frequency [K pop]', 'Frequency [Latin]', 'Frequency [Lofi]',
       'Frequency [Metal]', 'Frequency [Pop]', 'Frequency [R&B]',
       'Frequency [Rap]', 'Frequency [Rock]', 'Frequency [Video game music]',
       'Anxiety', 'Depression', 'Insomnia', 'OCD', 'Music effects',
       'Permissions'
"""  
