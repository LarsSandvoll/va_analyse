from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.utils import iface
import os.path


def LagShape(filnavn, filter, nyeVektorlag, selectedLayer):                                     # Danner nye vektorlag basert på gruppene valgt i analysen
    if os.path.isfile(nyeVektorlag.text() + filnavn + '.shp'):
        os.remove(nyeVektorlag.text() + filnavn + '.shp')                                       # Hvis ett vektolag med samme navn allerede finnes, fjern denne filen
    
    selectedLayer.selectByExpression(filter)                                                    # Velger delere av ledningsnettverket basert på filter som er blitt valgt i analysen
    fn = nyeVektorlag.text() + filnavn + '.shp'                                                 # Lager en ny shape fil av det valgte delen 
    writer = QgsVectorFileWriter.writeAsVectorFormat(selectedLayer, fn, 'utf-8', \
    driverName='ESRI Shapefile', onlySelected=True)                                             # Skriver den nye shape filen som vektorformat
    selected_layer = iface.addVectorLayer(fn, '','ogr')                                         # Legger det nye vektorlaget inn som ett aktivt vektorlag


def LagFarge(filnavn, verdi, a, b, c, d, e):                                                    # Definerer fargen til de nye vektorlagene basert på vedien hentet fra excel
    newlayers = QgsProject.instance().mapLayersByName(filnavn)                                  # Henter de nye vektorlagene som er blitt generert tidligere 
    newlayer = newlayers[0]
    renderer = newlayer.renderer()
    newlayer.renderer().symbol().symbolLayer(0).setWidth(0.55)                                  # Setter tegneregel for bredden til linjen
    if verdi >= a:                                                                              # Hvis resultat verdien er høyere enn valgt verdi for a gjør dette:
        newlayer.renderer().symbol().symbolLayer(0).setColor(QColor.fromRgb(250,0,0))           # Setter fargen til rød
        newlayer.triggerRepaint()                                                               # Endrer fargen
        iface.layerTreeView().refreshLayerSymbology(newlayer.id())                              # Oppdaterer vektorlaget
    elif verdi >= b and verdi < a:                                                              # Hvis resultat verdien er mellom valgt verdi for a og b gjør dette:
        newlayer.renderer().symbol().symbolLayer(0).setColor(QColor.fromRgb(250,140,0))         # Setter fargen til orasje
        newlayer.triggerRepaint()
        iface.layerTreeView().refreshLayerSymbology(newlayer.id())
    elif verdi >= c and verdi < b:                                                              # Hvis resultat verdien er mellom valgt verdi for b og c gjør dette:
        newlayer.renderer().symbol().symbolLayer(0).setColor(QColor.fromRgb(250,250,0))         # Setter fargen til gul
        newlayer.triggerRepaint()
        iface.layerTreeView().refreshLayerSymbology(newlayer.id())
    elif verdi >= d and verdi < c:                                                              # Hvis resultat verdien er mellom valgt verdi for c og d gjør dette:
        newlayer.renderer().symbol().symbolLayer(0).setColor(QColor.fromRgb(115,220,0))         # Setter fargen til grønn
        newlayer.triggerRepaint()
        iface.layerTreeView().refreshLayerSymbology(newlayer.id())
    elif verdi >= e and verdi < d:                                                              # Hvis resultat verdien er mellom valgt verdi for d og e gjør dette:
        newlayer.renderer().symbol().symbolLayer(0).setColor(QColor.fromRgb(0,155,0))           # Setter fargen til mørk grønn
        newlayer.triggerRepaint()
        iface.layerTreeView().refreshLayerSymbology(newlayer.id())
    else:                                                                                       # Hvis resultat verdien ikke har en verdi gjør dette:
        newlayer.renderer().symbol().symbolLayer(0).setColor(QColor.fromRgb(0,0,0))             # Setter fargen til svart
        newlayer.triggerRepaint()
        iface.layerTreeView().refreshLayerSymbology(newlayer.id())



def FindReplace(string, dictionary):                                                            # Setter inn verdier for parametere i en 'string'
    # is the item in the dict?
    for item in string:
        # iterate by keys
        if item in dictionary.keys():
            # look up and replace
            string = string.replace(item, dictionary[item])
    # return updated string
    return string
    print(string)
    
    