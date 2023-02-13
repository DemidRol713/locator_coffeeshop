import psycopg2
from numpy import nan
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

engine = create_engine('postgresql://demidrol:1q2w3e@localhost:5432/locator_coffeeshop')
data = pd.read_excel('/home/demidrol/Документы/Kofeyni_s_opisaniem.xlsx')

data['address'] = ''
for index in range(len(data.index)):
    data['address'][index] = ''
    if isinstance(data['Город'][index], str):
        data['address'][index] += data['Город'][index]
    if isinstance(data['Район'][index], str):
        data['address'][index] += data['Район'][index]
    if isinstance(data['Микрорайон'][index], str):
        data['address'][index] += data['Микрорайон'][index]
    if isinstance(data['Адрес'][index], str):
        data['address'][index] += data['Адрес'][index]

    # data['address'][index] = f"{data['Город'][index]} {data['Район'][index]} {data['Микрорайон'][index]} {data['Адрес'][index]}"

data['telephone'] = ''
for index in range(len(data.index)):
    data['telephone'][index] = []
    if not isinstance(data['Телефон 1'][index], float):
        data['telephone'][index].append(data['Телефон 1'][index])
    if not isinstance(data['Телефон 2'][index], float):
        data['telephone'][index].append(data['Телефон 2'][index])
    if not isinstance(data['Телефон 3'][index], float):
        data['telephone'][index].append(data['Телефон 3'][index])
    if data['telephone'][index] == set():
        data['telephone'][index] = []
    # data['telephone'][index] = {data['Телефон 1'][index], data['Телефон 2'][index], data['Телефон 3'][index]}

data['email'] = ''
for index in range(len(data.index)):
    data['email'][index] = []
    if not isinstance(data['E-mail 1'][index], float):
        data['email'][index].append(data['E-mail 1'][index])
    if not isinstance(data['E-mail 2'][index], float):
        data['email'][index].append(data['E-mail 2'][index])
    if data['email'][index] == set():
        data['email'][index] = []
    # data['email'][index] = {data['E-mail 1'][index], data['E-mail 2'][index]}

data['website'] = ''
for index in range(len(data.index)):
    data['website'][index] = []
    if not isinstance(data['Веб-сайт 1'][index], float):
        data['website'][index].append(data['Веб-сайт 1'][index])
    if not isinstance(data['Веб-сайт 2'][index], float):
        data['website'][index].append(data['Веб-сайт 2'][index])
    if data['website'][index] == set():
        data['website'][index] = []
    # data['website'][index] = {data['Веб-сайт 1'][index], data['Веб-сайт 2'][index]}

data['social_networks'] = ''
for index in range(len(data.index)):
    data['social_networks'][index] = []
    if not isinstance(data['ВКонтакте'][index], float):
        data['social_networks'][index].append(data['ВКонтакте'][index])
    if not isinstance(data['Twitter'][index], float):
        data['social_networks'][index].append(data['Twitter'][index])
    if not isinstance(data['YouTube'][index], float):
        data['social_networks'][index].append(data['YouTube'][index])
    if data['social_networks'][index] == set():
        data['social_networks'][index] = []
    # data['social_networks'][index] = {data['ВКонтакте'][index], data['Twitter'][index], data['YouTube'][index]}

data.drop('Телефон 2', axis=1, inplace=True)
data.drop('Телефон 3', axis=1, inplace=True)
data.drop('Телефон 1', axis=1, inplace=True)

data.drop('Адрес', axis=1, inplace=True)
data.drop('Город', axis=1, inplace=True)
data.drop('Район', axis=1, inplace=True)
data.drop('Микрорайон', axis=1, inplace=True)

data.drop('E-mail 1', axis=1, inplace=True)
data.drop('E-mail 2', axis=1, inplace=True)
data.drop('Веб-сайт 2', axis=1, inplace=True)
data.drop('Веб-сайт 1', axis=1, inplace=True)

data.drop('ВКонтакте', axis=1, inplace=True)
data.drop('Twitter', axis=1, inplace=True)
data.drop('YouTube', axis=1, inplace=True)
data.drop('Рубрики_Новые', axis=1, inplace=True)


data.to_sql('coffeeshop_coffeeshop', engine, if_exists='append', index=False)
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