from colorImage import *
import os

# main
path = input('ingrese la ruta de la imagen')            # se pide que ingrese la ruta de la imagen
image_name = input('ingrese el nombre de la imagen')    # se pide que ingrese el nombre de la imagen
path_file = os.path.join(path, image_name)              # se crea la ruta de la imagen
ci = colorImage(path_file)                              # se ingresa a la clase la ruta de la imagen

ci.displayProperties()                                  # se accede al método displayProperties
print('alto=',ci.alto,'ancho=', ci.ancho)               # se imprime el valor de la altura y ancho de la imagen

ci.makeGray()                                           # se accede al método makeGray

ci.colorizeRGB('red')                                   # se accede al método colorizeRGB y se ingresa 'red'

ci.makeHue()                                            # se accede al método makeHue
