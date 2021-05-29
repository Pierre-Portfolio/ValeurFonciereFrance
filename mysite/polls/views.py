from django.shortcuts import render
import io as io
import pylab
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import PIL

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

######
# partie code:
######
# Fonction qui crée les DataFrame des valeurs foncieres 2020 et 2019

def loadData():
    data2020=pd.read_csv("./assets/valeursfoncieres-2020.txt", sep="|", low_memory=False)
    data2020.head()
    return data2020

def cleanData(data2020):
    # netoyage colonnes
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


############
# Partie Django
############

data2020 = cleanData(loadData())

def index(request):
    return render(request,'index.html')

def sendGraph(request,graphId):
    if graphId == 1:
        createPourcentageParRegion()
    elif graphId == 2:
        createPieceParRegion()
    elif graphId == 3:
        createRandomGraph()
    elif graphId == 4:
        createRandomGraph()
    elif graphId == 5:
        createRandomGraph()
    elif graphId == 6:
        createRandomGraph()
    elif graphId == 7:
        createRandomGraph()

    graph = 'graph.png'
    context = {'graph': graph}
    return render(request,'MoyPerDep.html',context)

def createPourcentageParRegion():
    vente = pourcentageVenteParRegion(data2020)
    vente.plot(title="Rapport valeur fonciere / Surface terrain en 2020 par departement")

    buffer = io.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save("./assets/graph.png", "PNG")
    pylab.close()

def createPieceParRegion():
    resPiece = NbPieceParRegion(data2020)
    resPiece.plot(title="Rapport piece par maison / region")
    buffer = io.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save("./assets/graph.png", "PNG")
    pylab.close()

def createRandomGraph():
    x = [1, 2, 3, 4, 5, 6]
    y = [5, 2, 6, 8, 2, 7]
    plt.plot(x, y, linewidth=2)
    plt.xlabel('x-axis')
    plt.ylabel('yaxis')
    plt.title('sample graph')
    plt.grid(True)

    buffer = io.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save("./assets/graph.png", "PNG")
    pylab.close()