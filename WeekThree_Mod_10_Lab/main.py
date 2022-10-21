import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap , QImage, QIcon
import cv2

class Window(QWidget):
    """ Main app window """
    def __init__(self):
        super().__init__()

        self.window_width = 600
        self.window_height = 400

    def ui(self):
        """ Contains All Ui Things """
        pass

    def update(self):
        """ update frames """
        pass

    def save_img(self):
        """ Save image from camera """
        pass

    def record(self):
        """ Record video """

    