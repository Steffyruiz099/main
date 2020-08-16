from math import *
import numpy as np
import cv2
import os


class colorImage:
    def __init__(self, path_file):                                      # se crea el constructor y se pide la ruta de la imagen
        self.image = cv2.imread(path_file)                              # se carga la imagen via OpenCV

    def displayProperties(self):                                        # se crea el método
        self.alto, self.ancho, self.canal = self.image.shape            # se piden las propiedades de la imagen

    def makeGray(self):                                                 # se crea el método
        self.img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)         # se convierte la imagen en su versión de grises
        cv2.imshow('imagen0', self.img)                                 # se visualiza la imagen0 que es la imagen en grises
        cv2.waitKey(0)                                                  # se espera por una intevención del usuario

    def colorizeRGB(self, valor):                                       # se crea el método
        if valor == 'red':                                              # se pregunta por el valor ingresado y se compara con 'red'
            self.red_image = np.copy(self.image)                        # si el valor es igual a 'red' se crea una copia de la imagen
            self.red_image[:,:,0] = 0                                   # se pone el valor de B en 0
            self.red_image[:, :, 1] = 0                                 # se pone el valor de G en 0
            cv2.imshow('imagen1', self.red_image)                       # se visualiza la imagen1, la cual es una versión rojiza de la original
            cv2.waitKey(0)                                              # se espera por una intevención del usuario

        if valor == 'bluel':                                            # se pregunta por el valor ingresado y se compara con 'bluel'
            self.bluel_image = np.copy(self.image)                      # si el valor es igual a 'bluel' se crea una copia de la imagen
            self.bluel_image[:, :, 1] = 0                               # se pone el valor de G en 0
            self.bluel_image[:, :, 2] = 0                               # se pone el valor de R en 0
            cv2.imshow('imagen1', self.bluel_image)                     # se visualiza la imagen1, la cual es una versión azulada de la original
            cv2.waitKey(0)                                              # se espera por una intevención del usuario

        if valor == 'green':                                            # se pregunta por el valor ingresado y se compara con 'green'
            self.green_image = np.copy(self.image)                      # si el valor es igual a 'green' se crea una copia de la imagen
            self.green_image[:, :, 0] = 0                               # se pone el valor de B en 0
            self.green_image[:, :, 2] = 0                               # se pone el valor de R en 0
            cv2.imshow('imagen1', self.green_image)                     # se visualiza la imagen1, la cual es una versión verdosa de la original
            cv2.waitKey(0)                                              # se espera por una intevención del usuario

    def makeHue(self):                                                  # se crea el método
        self.hue = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)          # se convierte la imagen en su versión de HSV
        self.chue = np.copy(self.image)                                 # se crea una copia de la imagen
        self.chue[:, :, 1] = 255                                        # se pone el valor de S en 255
        self.chue[:, :, 2] = 255                                        # se pone el valor de V en 255
        self.rhue = cv2.cvtColor(self.chue, cv2.COLOR_HSV2BGR)          # se convierte la imagen de nuevo a la versión RGB
        cv2.imshow('imagen2', self.rhue)                                # se visualiza la imagen2 una versión de tonos/colores resaltados de la imagen original
        cv2.waitKey(0)                                                   # se espera por una intevención del usuario