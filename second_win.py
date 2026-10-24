from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit,
    QSpinBox, QMessageBox, QProgressBar,)

from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self): 
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def initUI(self):
        INPUT_WIDTH = 250
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)

        self.pbar = QProgressBar(self)
        self.pbar.setRange(0, 100)
        self.pbar.setValue(0)
        self.pbar.setTextVisible(False)

        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.btn_next = QPushButton(txt_sendresults, self)

        self.line_name = QLineEdit()
        self.line_name.setPlaceholderText(txt_hintname)
        # self.line_age = QLineEdit()
        # self.line_age.setPlaceholderText(txt_hintage)
        # self.line_age.setValidator(QIntValidator(1, 120))
        self.line_age = QSpinBox()
        self.line_age.setRange(0, 120)

        # self.line_test1 = QLineEdit()
        # self.line_test1.setPlaceholderText(txt_hinttest1)
        # self.line_test2 = QLineEdit()
        # self.line_test2.setPlaceholderText(txt_hinttest2)
        # self.line_test3 = QLineEdit()
        # self.line_test3.setPlaceholderText(txt_hinttest3)

        self.line_test1 = QSpinBox()
        self.line_test1.setRange(0, 300)
        self.line_test2 = QSpinBox()
        self.line_test2.setRange(0, 300)
        self.line_test3 = QSpinBox()
        self.line_test3.setRange(0, 300)

        self.line_name.setFixedWidth(INPUT_WIDTH)
        self.line_age.setFixedWidth(INPUT_WIDTH)
        self.line_test1.setFixedWidth(INPUT_WIDTH)
        self.line_test2.setFixedWidth(INPUT_WIDTH)
        self.line_test3.setFixedWidth(INPUT_WIDTH)
        self.pbar.setFixedWidth(225)

        self.btn_test1.setEnabled(True)
        self.line_test1.setEnabled(False)
        self.btn_test2.setEnabled(False)
        self.line_test2.setEnabled(False)
        self.btn_test3.setEnabled(False)
        self.line_test3.setEnabled(False)
        self.btn_next.setEnabled(False)

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)

        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.pbar, alignment=Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.pbar.setMaximum(15)
        self.pbar.setValue(15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        total_secs = time.minute()*60 + time.second()
        self.pbar.setValue(total_secs)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
            self.line_test1.setEnabled(True)
            self.btn_test2.setEnabled(True)
    
    def timer_sits(self):
        global time
        self.pbar.setMaximum(30)
        self.pbar.setValue(30)
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        total_secs = time.minute()*60 + time.second()
        self.pbar.setValue(total_secs)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
            self.btn_test3.setEnabled(True)

    def timer_final(self):
        global time
        self.pbar.setMaximum(60)
        self.pbar.setValue(60)
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        self.line_test2.setEnabled(True)
        self.line_test3.setEnabled(True)
        global time
        time = time.addSecs(-1)
        total_secs = time.minute()*60 + time.second()
        self.pbar.setValue(total_secs)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")

        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
            self.btn_next.setEnabled(True)
    
    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        if not (self.line_name.text().strip() and self.line_age.text().strip()) or int(self.line_age.text().strip()) == 0:
            QMessageBox.warning(self, "Warning", "Please input your name and age!")
            return

        if not (self.line_test1.text().strip() and self.line_test2.text().strip() and self.line_test3.text().strip()) or int(self.line_test1.text()) == 0 or int(self.line_test2.text()) == 0 or int(self.line_test3.text()) == 0:
            QMessageBox.warning(self, "Warning", "Please enter your pulse data!")
            return

        self.hide()
        self.exp = Experiment(
            self.line_age.text(),
            self.line_test1.text(),
            self.line_test2.text(),
            self.line_test3.text()
        )
        self.fw = FinalWin(self.exp)

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = int(age)
        self.t1 = int(test1)
        self.t2 = int(test2)
        self.t3 = int(test3)
