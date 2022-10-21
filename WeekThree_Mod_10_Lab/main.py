""" My Camera Application
Authro: MD. ASRAFUZZAMAN SUVON
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap , QImage, QIcon
from PyQt5.QtCore import QTimer
import cv2
import datetime

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
        # layout
        grid = QGridLayout()
        self.setLayout(grid)


        # Image level
        self.image_level = QLabel(self)
        self.image_level.setGeometry(0,0,self.img_width,self.img_height)

        # Capture Button
        self.capture_btn = QPushButton(self)
        self.capture_btn.setIcon(self.camera_icon)
        self.capture_btn.setStyleSheet("border-radius: 25; border : 2px solid black; border-width: 3px")
        self.capture_btn.setFixedSize(50,50)
        self.capture_btn.clicked.connect(self.save_img)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        # Add Things to the layout
        grid.addWidget(self.capture_btn,0,0)
        grid.addWidget(self.image_level,0,1)

        
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
        cv2.imwrite(f"{self.dt}.jpg",self.frame)

    def record(self):
        """ Record video """

    def get_time(self):
        now = datetime.datetime.now()
        self.dt = now.strftime("%m-%d-%y,%H-%M-%S")




# Run
cap_icon_path = 'assets/cam.png'

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())


    