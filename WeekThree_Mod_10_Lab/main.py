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


        # Other Variable
        self.dt = "0-0-0"
        self.record_flag = False

        # Icon Load
        self.camera_icon = QIcon(cap_icon_path)
        self.record_icon = QIcon(rec_icon_path)
        self.stop_icon = QIcon(stop_icon_path)

        # To save the video
        self.fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')


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

        # Video Rec Button
        self.rec_btn = QPushButton(self)
        # self.rec_btn.setIcon(self.record_icon)
        self.rec_btn.setStyleSheet("border-radius: 25; border : 2px solid black; border-width: 3px")
        self.rec_btn.setFixedSize(50,50)
        self.rec_btn.clicked.connect(self.record)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        # Add Things to the layout
        grid.addWidget(self.capture_btn,0,0)
        grid.addWidget(self.image_level,0,1,2,3)
        grid.addWidget(self.rec_btn,1,0)

        self.show()

    def update(self):
        """ update frames """
        _, self.frame = self.cap.read()
        copy_frame = self.frame

        if self.record_flag==True:
            self.out.write(copy_frame)
            self.rec_btn.setIcon(self.stop_icon)
            self.frame = cv2.circle(self.frame,(20,70),5,(0,0,255),10)
        else:
            self.rec_btn.setIcon(self.record_icon)

        frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
        height,width,channel = frame.shape
        step = channel * width

        q_frame = QImage(frame.data,width,height,step,QImage.Format_RGB888)
        self.image_level.setPixmap(QPixmap.fromImage(q_frame))

    def save_img(self):
        """ Save image from camera """
        self.get_time()
        cv2.imwrite(f"{self.dt}.jpg",self.frame)

    def record(self):
        """ Record video """
        if self.record_flag == True:
            self.record_flag = False
        else: 
            self.record_flag = True
            self.get_time()

            self.out = cv2.VideoWriter(f"{self.dt}.mp4",self.fourcc,20.0, (640,480))

    def get_time(self):
        now = datetime.datetime.now()
        self.dt = now.strftime("%m-%d-%y,%H-%M-%S")




# Run
if __name__ == '__main__':
    cap_icon_path = 'assets/cam.png'
    rec_icon_path = 'assets/videoCap.png'
    stop_icon_path = 'assets/stop.png'


    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())


    