""" My Camera Application
Authro: MD. ASRAFUZZAMAN SUVON
"""
import sys
from turtle import window_height, window_width
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap , QImage, QIcon
import cv2

class Window(QWidget):
    """ Main app window """
    def __init__(self):
        super().__init__()
        #  Variable for App Window
        self.window_width = 640
        self.window_height = 400

        # Image Variables
        self.img_width = 640
        self.img_height = 400

        # Set up the window
        self.setWindowTitle("My Camera App")
        self.setGeometry(0,0,self.window_width,self.window_height)
        self.setFixedSize(self.window_width,self.window_height)


        self.ui()

    def ui(self):
        """ Contains All Ui Things """

        # Image level
        self.image_level = QLabel(self)
        self.image_level.setGeometry(0,0,self.img_width,self.img_height)
        
        self.show()

    def update(self):
        """ update frames """
        pass

    def save_img(self):
        """ Save image from camera """
        pass

    def record(self):
        """ Record video """




# Run
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())


    