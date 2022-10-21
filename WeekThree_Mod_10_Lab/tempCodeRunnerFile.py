""" My Camera Application
Authro: MD. ASRAFUZZAMAN SUVON
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap , QImage, QIcon
from PyQt5.QtCore import QTimer
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


        # Icon Load
        self.camera_icon = QIcon(cap_icon_path)


        # Set up the window
        self.setWindowTitle("My Camera App")
        self.setGeometry(0,0,self.window_width,self.window_height)
        self.setFixedSize(self.window_width,self.window_height)

        # Setup Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.ui()

    def ui(self):
        """ Contains All Ui Things """

        # Image level
        self.image_level = QLabel(self)
        self.image_level.setGeometry(0,0,self.img_width,self.img_height)

        # Capture Button
        self.capture_btn = QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)


        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
        self.show()

    def update(self):
        """ update frames """
        _, self.frame = self.cap.read()

        frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
        height,width,channel = frame.shape
        step = channel * width

        q_frame = QImage(frame.data,width,height,step,QImage.Format_RGB888)
        self.image_level.setPixmap(QPixmap.fromImage(q_frame))

    def save_img(self):
        """ Save image from camera """
        pass

    def record(self):
        """ Record video """




# Run
cap_icon_path = 'assets/cam.png'

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())


    