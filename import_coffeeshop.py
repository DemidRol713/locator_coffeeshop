import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

# engine = create_engine('postgresql://demidrol:1q2w3e@localhost:5432/locator_coffeeshop')
data = pd.read_excel('/home/demidrol/Документы/Kofeyni_s_opisaniem.xlsx')

data['address'] = ''
for index in range(len(data['Адрес'])):
    data['address'][index] = f"{data['Город'][index]} {data['Район'][index]} {data['Микрорайон'][index]} {data['Адрес'][index]}"

data['telephone'] = ''
for index in range(len(data['Телефон 1'])):
    data['telephone'][index] = {data['Телефон 1'][index], data['Телефон 2'][index], data['Телефон 3'][index]}
data['email'] = ''
for index in range(len(data['E-mail 1'])):
    data['email'][index] = {data['E-mail 1'][index], data['E-mail 2'][index]}

data['website'] = ''
for index in range(len(data['Веб-сайт 1'])):
    data['website'][index] = {data['Веб-сайт 1'][index], data['Веб-сайт 2'][index]}

data['social_networks'] = ''
for index in range(len(data['ВКонтакте'])):
    data['social_networks'][index] = {data['ВКонтакте'][index], data['Twitter'][index], data['YouTube'][index]}

data.to_excel('/home/demidrol/Документы/Kofeyni_s_opisaniem_final.xlsx', index=False)
data.to_csv('/home/demidrol/Документы/Kofeyni_s_opisaniem_final.csv', index=False)

#
# data = pd.read_excel('/home/demidrol/Документы/Kofeyni_s_opisaniem_final.xlsx', index_col=0)
# data.to_csv("/home/demidrol/Документы/Kofeyni_s_opisaniem_final.csv", index=False)

# data['address'] = ''
# for index in range(len(data['Адрес'])):
#     data['address'][index] = pd.array([data['Город'][index], data['Район'][index], data['Микрорайон'][index], data['Адрес'][index]])
#
# data['telephone'] = ''
# for index in range(len(data['Телефон 1'])):
#     data['telephone'][index] = pd.array([data['Телефон 1'][index], data['Телефон 2'][index], data['Телефон 3'][index]])
# data['email'] = ''
# for index in range(len(data['E-mail 1'])):
#     data['email'][index] = pd.array([data['E-mail 1'][index], data['E-mail 2'][index]])
#
# data['website'] = ''
# for index in range(len(data['Веб-сайт 1'])):
#     data['website'][index] = pd.array([data['Веб-сайт 1'][index], data['Веб-сайт 2'][index]])
#
# data['social_networks'] = ''
# for index in range(len(data['ВКонтакте'])):
#     data['social_networks'][index] = pd.array([data['ВКонтакте'][index], data['Twitter'][index], data['YouTube'][index]])