from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel(self)
        self.label.setGeometry(50,50,700,200)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFrameShape(QFrame.Panel)
        self.label.setFont(QFont("Tahoma",60))
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.digital)
        
        self.resize(800,500)
        self.show()
    def digital(self):
        time = QTime.currentTime()
        last_time = time.addSecs(1)
        label_time = last_time.toString("hh:mm:ss")
        self.label.setText(label_time)      
        
app = QApplication([])
window = main()
app.exec()