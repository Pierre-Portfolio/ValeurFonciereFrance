#!/usr/bin/env python
# coding: utf-8

# # PROJET PYTHON FINAL A3 

# On import DataFrame et numpy

# In[2]:


# storing and anaysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# Fonction qui crée les DataFrame des valeurs foncieres 2020 et 2019

# In[3]:

def loadData():
    data2020=pd.read_csv("../../../../../../../Downloads/valeursfoncieres-2020.txt", sep="|", low_memory=False)
    data2020.head()
    return data2020

# On commence le netoyage des données

# In[4]:


#netoyage colonnes
def cleanData(data2020):
    column_with_nan = data2020.columns[data2020.isna().any()]
    for column in column_with_nan:
        if data2020[column].isna().sum()*100.0/data2020.shape[0] > 50:
            data2020.drop(column,1, inplace=True)
    uselesscolum = ['Section','No plan','Nombre de lots','Code type local','Nature culture','No voie','No disposition']
    data2020.drop(uselesscolum,axis=1, inplace=True)

    # netoyage lignes
    data2020 = data2020.dropna(axis=0, thresh=14)

    # On convertie certaine colonnes en float
    data2020["Valeur fonciere"] = data2020["Valeur fonciere"].str.replace(',', '.')
    data2020.head()
    data2020["Valeur fonciere"] = pd.to_numeric(data2020["Valeur fonciere"])
    data2020["Surface reelle bati"] = pd.to_numeric(data2020["Surface reelle bati"])
    data2020["Code postal"] = data2020["Code postal"].astype({'Code postal': 'int32'})
    return data2020


def pourcentageVenteParRegion(data2020):
    # On calcul le prix au metre carré de chaque commune
    tempPrix2020 = data2020
    tempPrix2020 = tempPrix2020[(tempPrix2020["Surface terrain"]>0)]
    tempPrix2020["Prix m2"] = (tempPrix2020["Valeur fonciere"] / tempPrix2020["Surface terrain"])
    tmp2020 = tempPrix2020.groupby(["Code departement"])["Valeur fonciere","Surface terrain","Prix m2"].mean()
    tmp2020.style.background_gradient(cmap='Blues')

    tmp2020['Code departement'] = tmp2020.index
    tmp2020.plot(x='Code departement',y='Prix m2')
    #type(tmp2020)
    # Pourcentage de vente par region
    DataFrameVenteMaison2020 = data2020[data2020['Nature mutation'] == "Vente"]
    vente = DataFrameVenteMaison2020.groupby(["Code departement"])["Nature mutation"].count() / len(DataFrameVenteMaison2020)
    #vente.plot(title="Rapport valeur fonciere / Surface terrain en 2020 par departement")
    return vente


def NbPieceParRegion(data2020):
    # Moyenne du nombre de piece par region
    DataFrameNbPiece2020 = data2020[data2020['Nombre pieces principales'] != 0]
    resPiece = DataFrameNbPiece2020.groupby(["Code departement"])["Nombre pieces principales"].mean()# / len(DataFramenbPiece2020)
    return resPiece

def autre():
    # On calcul le ratio terrain total par rapport a celui de la maison
    dataSuperficie = data2020
    dataSuperficie = dataSuperficie[(dataSuperficie["Surface terrain"]>0)]
    dataSuperficie = dataSuperficie[(dataSuperficie["Surface reelle bati"]>0)]
    dataSuperficie["ratioTerrainMaison"] = (tempPrix2020["Surface reelle bati"] / tempPrix2020["Surface terrain"])
    tmpBis2020 = dataSuperficie.groupby(["Code departement"])["ratioTerrainMaison"].mean() / len(dataSuperficie)
    #tmp.style.background_gradient(cmap='Blues')
    tmpBis2020.plot()
    type(tmp2020)


    # # ON COMPARE A 2019

    # In[13]:


    #On initialise les data
    data2019=pd.read_csv("../../../../../../../Downloads/valeursfoncieres-2019.txt", sep="|", low_memory=False)
    #netoyage colonnes
    column_with_nan = data2019.columns[data2019.isna().any()]
    for column in column_with_nan:
        if data2019[column].isna().sum()*100.0/data2019.shape[0] > 50:
            data2019.drop(column,1, inplace=True)
    uselesscolum = ['Section','No plan','Nombre de lots','Code type local','Nature culture','No voie','No disposition']
    data2019.drop(uselesscolum,axis=1, inplace=True)
    #Netoyage lignes
    data2019 = data2019.dropna(axis=0,thresh=14)
    data2019["Valeur fonciere"] = data2019["Valeur fonciere"].str.replace(',','.')
    #changement type colums
    data2019["Valeur fonciere"] = pd.to_numeric(data2019["Valeur fonciere"])
    data2019["Surface reelle bati"] = pd.to_numeric(data2019["Surface reelle bati"])
    data2019["Code postal"] = data2019["Code postal"].astype({'Code postal': 'int32'})
    data2019


    # In[14]:


    # On calcul le prix au metre carré de chaque commune en 2019
    tempPrix2019 = data2019
    tempPrix2019 = tempPrix2019[(tempPrix2019["Surface terrain"]>0)]
    tempPrix2019["Prix m2"] = (tempPrix2019["Valeur fonciere"] / tempPrix2019["Surface terrain"])
    tmp2019 = tempPrix2019.groupby(["Code departement"])["Valeur fonciere","Surface terrain","Prix m2"].mean()
    tmp2019['Code departement'] = tmp2019.index
    tmp2019.plot(x='Code departement',y='Prix m2',title="Rapport valeur fonciere / Surface terrain en 2019 par departement")


    # In[15]:


    # On fusionne les 2 graphs ( rapport vente par departement )
    tmp2020


    # In[16]:


    tmpDuo2020 = tmp2020["Prix m2"]
    tmpDuo2019 = tmp2019["Prix m2"]
    plt.figure(figsize=(12,5))
    ax1 = tmpDuo2019.plot(color='blue', grid=True, label='Count')
    ax2 = tmpDuo2020.plot(color='red', grid=True, secondary_y=True, label='Sum')


    # In[ ]:





    # In[ ]:





    # In[ ]:




